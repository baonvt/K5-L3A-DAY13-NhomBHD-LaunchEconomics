"""Lab 13 của nhóm BHD. Chạy python lab13.py trong thư mục src."""

import math
from pathlib import Path
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

GIA_VAO, GIA_RA = 26, 130  # đồng / 1.000 token
GIA_TOOL = 15
LUONG_PHUT = 2_000
BASELINE = 12_000
CO_DINH_THANG = 40_000_000
LOAI_PILOT = ("noi_dia", "hang_nang")


def ti_le_thanh_cong(p, k=None):
    """Xác suất có ít nhất một lần đúng trong tối đa k lần độc lập."""
    if not 0 <= p <= 1 or (k is not None and (not isinstance(k, int) or k < 1)):
        raise ValueError("p phải thuộc [0, 1] và k phải là số nguyên dương hoặc None")
    if k is None or p in (0, 1):
        return float(p > 0)
    return -math.expm1(k * math.log1p(-p))


def so_lan_chay_ky_vong(p, k=None):
    thanh_cong = ti_le_thanh_cong(p, k)
    if p == 0:
        return math.inf if k is None else k
    return thanh_cong / p


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    ty_le = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / ty_le if ty_le else math.inf


def kiem_tra_dap_an_biet_truoc():
    thu = (so_lan_chay_ky_vong(0.8, 2), so_lan_chay_ky_vong(0.8),
           he_so_chi_phi_moi_viec_thanh_cong(0.8, 3))
    for ket_qua, dap_an in zip(thu, (1.20, 1.25, 1.25)):
        assert abs(ket_qua - dap_an) < 1e-9, (ket_qua, dap_an)
    print("Ba phép thử đáp án biết trước: ĐẠT", " · ".join(f"{x:.2f}" for x in thu))


def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL,
            luong_phut=LUONG_PHUT, he_so_xem_lai=1.0, he_so_lam_lai=1.0,
            max_lan_chay=None):
    """Tính tiền mọi lần chạy trong phạm vi và đếm việc theo kết quả cuối."""
    traces = runs[runs.request_id.isin(reqs.request_id)]
    xu_ly = reqs
    if max_lan_chay is not None:
        traces = traces[traces.attempt <= max_lan_chay]
        # Ca cần thêm lượt được chuyển cho nhân viên. Phút trợ lý cho ca đó bằng 0.
        xu_ly = reqs[reqs.so_lan_chay <= max_lan_chay]

    token = (traces.tokens_in * gia_vao + traces.tokens_out * gia_ra) / 1000
    tool = traces.tool_calls * gia_tool
    xem_lai = xu_ly.phut_xem_lai_simulated.sum() * luong_phut * he_so_xem_lai
    lam_lai = xu_ly.phut_lam_lai_simulated.sum() * luong_phut * he_so_lam_lai
    hoa_don = token.sum() + tool.sum()
    tong = hoa_don + xem_lai + lam_lai
    thanh_cong = xu_ly.ket_qua.eq("thanh_cong").sum()
    return dict(token=token.sum(), tool=tool.sum(), chay_lai=(token + tool)[traces.attempt > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong, thanh_cong=thanh_cong,
                cps=tong / thanh_cong if thanh_cong else math.inf,
                hoa_don_moi_yc=hoa_don / len(reqs) if len(reqs) else math.nan)


def bang_chi_phi(runs, reqs, pilot):
    goc = mo_hinh(runs, reqs)
    print(f"\nA2 · {len(reqs)} yêu cầu, {len(runs)} lượt chạy, {runs.tool_calls.sum()} lần gọi tool")
    for ten, so in goc.items():
        nhan = " (simulated)" if ten in ("xem_lai", "lam_lai", "tong", "cps") else ""
        print(f"  {ten:<17} {so:12,.2f}{nhan}")
    print(f"  CPS / hóa đơn mỗi yêu cầu: {goc['cps'] / goc['hoa_don_moi_yc']:.2f}× (simulated)")
    print(f"  Làm lại / tổng chi phí: {goc['lam_lai'] / goc['tong']:.2%} (simulated)")
    print("\nA3 · Loại | yêu cầu | thành công | lượt/YC | CPS và bội số (simulated)")
    for loai, nhom in reqs.groupby("loai", sort=False):
        m = mo_hinh(runs, nhom)
        print(f"{loai:10} {len(nhom):4} {m['thanh_cong']/len(nhom):8.2%} "
              f"{nhom.so_lan_chay.mean():7.2f} {m['cps']:9,.0f} {m['cps']/BASELINE:6.2f}×")
    quoc_te = runs[runs.request_id.isin(reqs.loc[reqs.loai.eq("quoc_te"), "request_id"])]
    print("  Quốc tế, % ok theo lượt:", quoc_te.status.eq("ok").groupby(quoc_te.attempt)
          .mean().map("{:.2%}".format).to_dict())

    m = mo_hinh(runs, pilot)
    print(f"\nA4 · {len(pilot)} yêu cầu trong phạm vi, {m['thanh_cong']} thành công, "
          f"{m['tong']:,.0f} đ (simulated)")
    print("YC toàn mạng/tháng | thành công trong phạm vi | cố định/việc | CPS đủ phí (simulated) | bội số")
    for luong in (45_000, 22_500):
        xong = luong * m["thanh_cong"] / len(reqs)
        co_dinh = CO_DINH_THANG / xong
        day_du = co_dinh + m["cps"]
        print(f"{luong:8,} {xong:14,.0f} {co_dinh:16,.2f} {day_du:15,.2f} {day_du/BASELINE:7.2f}×")


def bang_do_nhay(runs, reqs, pilot):
    goc = mo_hinh(runs, reqs)["cps"]
    kich_ban = [
        ("Token ×2", dict(gia_vao=52, gia_ra=260)), ("Token ×0,5", dict(gia_vao=13, gia_ra=65)),
        ("Xem lại ×2", dict(he_so_xem_lai=2)), ("Xem lại ×0,5", dict(he_so_xem_lai=0.5)),
        ("Làm lại ×2", dict(he_so_lam_lai=2)), ("Làm lại ×0,5", dict(he_so_lam_lai=0.5)),
        ("Lương +25%", dict(luong_phut=2500)),
        ("Tối đa 2 lượt", dict(max_lan_chay=2)), ("Tối đa 1 lượt", dict(max_lan_chay=1)),
        ("B2 · Token và xem lại ×2", dict(gia_vao=52, gia_ra=260, he_so_xem_lai=2)),
    ]
    print("\nB1–B2 · Kịch bản | CPS (simulated) | thay đổi (simulated)")
    for ten, gia in kich_ban:
        cps = mo_hinh(runs, reqs, **gia)["cps"]
        print(f"{ten:28} {cps:9,.0f} {cps/goc - 1:+8.1%}")

    print("\nB3 · Lượt | tổng trợ lý | ca chưa xong | tổng hệ thống | CPS | hệ thống/YC (tiền simulated)")
    for k in (1, 2, 3):
        m = mo_hinh(runs, reqs, max_lan_chay=k)
        con_lai = len(reqs) - m["thanh_cong"]
        he_thong = m["tong"] + BASELINE * con_lai
        print(f"{k} {m['tong']:14,.0f} {con_lai:9} {he_thong:16,.0f} "
              f"{m['cps']:10,.0f} {he_thong/len(reqs):12,.0f}")

    m = mo_hinh(runs, pilot)
    tra_loi = runs.loc[runs.status.eq("ok") & runs.request_id.isin(pilot.request_id), "request_id"].nunique()
    ca_sai = pilot.ket_qua.eq("lam_lai").sum()
    phut_sai = reqs.loc[reqs.ket_qua.eq("lam_lai"), "phut_lam_lai_simulated"].mean()
    hoa_don = m["token"] + m["tool"]
    print(f"\nB4 · {tra_loi} yêu cầu có câu trả lời, {ca_sai} ca làm lại, hóa đơn {hoa_don:,.0f} đ")
    print("Phút làm lại | tổng biến phí | CPS | bội số | phút xem lại hòa vốn (kịch bản simulated)")
    for phut in (9, round(phut_sai, 1)):
        lam_lai = ca_sai * phut * LUONG_PHUT
        tong = hoa_don + lam_lai + tra_loi * 5 * LUONG_PHUT
        cps = tong / m["thanh_cong"]
        hoa_von = (BASELINE * m["thanh_cong"] - hoa_don - lam_lai) / (tra_loi * LUONG_PHUT)
        print(f"{phut:6.1f} {tong:15,.0f} {cps:10,.0f} {cps/BASELINE:6.2f}× {hoa_von:9.2f}")


def co_mau_hai_ty_le(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhánh theo công thức hai tỉ lệ, kiểm định hai phía."""
    tb = (p1 + p2) / 2
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    tu = za * math.sqrt(2 * tb * (1 - tb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil((tu / (p2 - p1)) ** 2)


def bang_co_mau():
    n = co_mau_hai_ty_le(0.70, 0.75)
    icc = 0.02
    cum = 20
    de_75 = 1 + (75 - 1) * icc
    n_tho = math.ceil(n * de_75)
    n_6 = 859  # cỡ mẫu hiệu dụng mỗi nhánh cho mức chênh 6 điểm do đề cho
    m = math.ceil(n_6 * (1 - icc) / (cum - n_6 * icc))
    de = 1 + (m - 1) * icc
    hieu_dung = cum * m / de
    power_5 = NormalIndPower().power(abs(proportion_effectsize(0.70, 0.75)), hieu_dung, alpha=0.05)
    print("\nD1 · Cỡ mẫu mỗi nhánh")
    print(f"a. Ngẫu nhiên theo yêu cầu: {n:,} yêu cầu.")
    print(f"b. 75 yêu cầu/người: DE {de_75:.2f}, cần {n_tho:,} yêu cầu, {math.ceil(n_tho/75)} người.")
    print(f"c. 20 nhân viên: trần hiệu dụng {cum/icc:,.0f}.")
    print(f"d. 6 depot: trần hiệu dụng {6/icc:,.0f}.")
    print(f"e. Chênh 6 điểm: cần {m} yêu cầu/người, {cum*m:,} mỗi nhánh, "
          f"DE {de:.2f}, hiệu dụng {hieu_dung:.2f}. Power ở 5 điểm: {power_5:.3f}.")


def bang_chi_so(reqs, pilot):
    xem = reqs[reqs.duoc_xem_lai.eq(1)]
    dong = reqs.dong_trong_24h.eq(1) & reqs.mo_lai_trong_7_ngay.eq(0)
    print("\nE1 · Chỉ số trong đợt chạy thử")
    for ten, dau_hieu in (
        ("Đóng trong 24h, không mở lại trong 7 ngày", dong),
        ("Sửa hoặc bỏ trong số yêu cầu được xem lại", xem.quyet_dinh_xem_lai.isin(["sua", "bo"])),
        ("Mở lại trong 7 ngày", reqs.mo_lai_trong_7_ngay.eq(1)),
        ("Mở lại trong phạm vi pilot", pilot.mo_lai_trong_7_ngay.eq(1)),
    ):
        print(f"{ten}: {dau_hieu.sum()}/{len(dau_hieu)} = {dau_hieu.mean():.2%}")


def main():
    kiem_tra_dap_an_biet_truoc()
    thu_muc = Path(__file__).resolve().parent
    runs = pd.read_csv(thu_muc / "logix_runs.csv")
    reqs = pd.read_csv(thu_muc / "logix_requests.csv", keep_default_na=False)
    pilot = reqs[reqs.loai.isin(LOAI_PILOT)]
    bang_chi_phi(runs, reqs, pilot)
    bang_do_nhay(runs, reqs, pilot)
    bang_co_mau()
    bang_chi_so(reqs, pilot)


if __name__ == "__main__":
    main()
