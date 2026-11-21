# Báo cáo nhóm BHD · Kinh tế của trợ lý hoàn phí LogiX-VN

## 1. Thông tin nhóm

K5–L3A · Nguyễn Võ Thái Bảo, Nguyễn Trường Duy, Đoàn Văn Hiệp. [Phân công](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Đề xuất **Go có điều kiện** cho pilot nội địa và hàng nặng. Mẫu có 1.200 yêu cầu, 1.624 lần chạy. Bảng chi phí dùng kết quả cuối theo yêu cầu, còn hóa đơn ghi cả lượt lỗi.

## 3. Giải pháp

| Nhiệm vụ | Cách làm và hồ sơ |
| --- | --- |
| A–B | Tái tính bốn khoản chi phí, tách bốn loại yêu cầu, đổi từng giả định và tính cả phần nhân viên làm thay. [Bảng chi phí](bang_chi_phi.md) |
| C | Duy và Hiệp đã commit riêng hai cột nhãn cho 20 ca. Hai cột dùng chung nhãn do Codex soạn theo tài liệu lab. [Bảng lỗi](bang_loi.md) |
| D | Chia ngẫu nhiên theo nhân viên trong 12 depot, cân bằng 20 người mỗi nhánh. [Kế hoạch pilot](pilot_plan.yaml) |
| E | Đăng ký chỉ số, sơ đồ event, luật dừng và điều kiện ra quyết định. [Chỉ số](chi_so.md) · [Hồ sơ Gate 2a](ho_so_launch_v0.md) |

## 4. Kết quả

- Trợ lý hoàn thành 978/1.200 yêu cầu với 4.472 đ/việc (simulated). Nếu cộng 222 ca nhân viên làm thay, cả hệ thống tốn 5.865 đ/yêu cầu ở giới hạn ba lượt (simulated).
- Nội địa và hàng nặng hoàn thành 900/982 ca. Khi xem lại 100%, tổng chi phí gồm ca thủ công và cố định là 12.850–13.466 đ/yêu cầu (simulated) theo lưu lượng A4, vượt mốc tự làm 12.000 đ/yêu cầu.
- Codex đã chạy `python -X utf8 lab13.py` trong `src/` ở môi trường hiện tại và đối chiếu ba phép A1, bảng A–B, D1 và E1. YAML đọc được bằng `yaml.safe_load` và có bốn luật dừng. Kiểm tra trên máy thành viên khác còn chờ xác nhận.
- Hồ sơ còn thiếu hai bản nhãn lập độc lập trước khi so sánh và kết quả duyệt chéo mà BHD nhận. Phiếu để BHD chấm nhóm được phân công còn chờ hồ sơ của nhóm đó. [Bảng lỗi](bang_loi.md) · [Phiếu chấm](phieu_cham.md)

## 5. Khó khăn và cách xử lý

Chi phí trên việc thành công và chi phí trên yêu cầu dùng hai mẫu số. B3 tính cả 234 ca chuyển sang nhân viên theo giả định của đề khi giới hạn hai lượt.

## 6. Tổng hợp đóng góp

Bảo phụ trách A–B và tích hợp, Duy phụ trách kiểm số và bảng lỗi, Hiệp phụ trách phép tính D–E và hồ sơ pilot. Bảng lỗi ghi rõ nguồn AI của hai cột nhãn. [Thông tin nhóm](../../TEAM.md)

## 7. Hạn chế và hướng cải thiện

Các phút công là simulated. Pilot cần đo phút thực và chờ đủ cửa sổ mở lại 7 ngày. Mẫu chạy thử ở 6 depot thiếu đối chứng đồng thời, nên 82,83% đóng đúng hạn và không mở lại chỉ là mức quan sát.

## 8. Tài liệu tham khảo

Đề gốc, hai CSV và công thức đều do lab cung cấp. [Đề Lab 13](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx) · [Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md) · [Mã tái lập](../../src/lab13.py)
