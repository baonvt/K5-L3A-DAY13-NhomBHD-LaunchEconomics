# Chi phí trợ lý hoàn phí LogiX-VN

Mẫu gồm 1.200 yêu cầu và 1.624 lượt chạy. CPS là chi phí của trợ lý trên một việc thành công. Các bảng dùng đồng Việt Nam và làm tròn sau phép chia. [Mã tái lập](../../src/lab13.py)

## A1 · Ba phép thử với xác suất đúng 0,8

| Đại lượng | Kết quả |
| --- | ---: |
| Số lượt kỳ vọng, tối đa 2 lượt | 1,20 |
| Số lượt kỳ vọng, thử đến khi đúng | 1,25 |
| Hệ số chi phí trên một việc thành công, tối đa 3 lượt | 1,25 |

## A2 · Chi phí từ trace

| Khoản | Kết quả | Căn cứ |
| --- | ---: | --- |
| Token | 245.585 đ | Token vào × 26 và token ra × 130, chia 1.000 |
| Tool | 84.000 đ | 5.600 lượt gọi × 15 đ |
| Trong đó, token và tool ở lượt 2–3 | 93.804 đ | Tổng trên các dòng có `attempt > 1`, đã nằm trong hai khoản trên |
| Xem lại | 1.780.000 đ | 890 phút × 2.000 đ, simulated |
| Làm lại | 2.264.000 đ | 1.132 phút × 2.000 đ, simulated |
| Tổng chi phí trợ lý | 4.373.585 đ | Token + tool + xem lại + làm lại, simulated |
| Việc thành công | 978 | Yêu cầu có `ket_qua = thanh_cong` |
| CPS | 4.472 đ | Tổng / 978, simulated |
| Hóa đơn token và tool trên một yêu cầu | 274,65 đ | (Token + tool) / 1.200 |

CPS bằng **16,28 lần** hóa đơn trên một yêu cầu (simulated). Làm lại chiếm nhiều nhất với **51,77%** tổng chi phí (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Yêu cầu | Thành công | Lượt/yêu cầu | CPS (simulated) | CPS / 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,02% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,05% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,33% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,41% | 1,88 | 10.215 đ | 0,85× |

Quốc tế tốn 22.515 đ/việc (simulated). Trong những lượt còn phải chạy, tỉ lệ trả về `ok` lần lượt là 30,00%, 11,43% và 2,15%. Pilot ưu tiên nội địa và hàng nặng. Đối tác chỉ hoàn thành 54,41% và cần xử lý điều khoản riêng.

## A4 · Phân bổ 40 triệu đ cố định mỗi tháng

Có 900 việc thành công trong 982 yêu cầu thuộc phạm vi. Khi ngoại suy từ tổng lưu lượng toàn mạng, số việc thành công trong phạm vi bằng lưu lượng × 900/1.200. Biến phí là 3.072.513 / 900 = 3.413,90 đ/việc (simulated).

| Yêu cầu toàn mạng/tháng | Việc thành công trong phạm vi/tháng | Cố định/việc | CPS gồm cố định (simulated) | So với 12.000 đ (simulated) |
| ---: | ---: | ---: | ---: | ---: |
| 45.000 | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| 22.500 | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

Cả hai khối lượng đều dưới mốc so sánh. Giữ nguyên cơ cấu mẫu, nghiệm của 3.413,90 + 40.000.000 / (0,75 × lượng yêu cầu) = 12.000 là khoảng 6.212 yêu cầu toàn mạng/tháng (simulated). Phần nhân viên tiếp quản được tính riêng tại B3.

## B1 · Thay đổi một yếu tố trên toàn mẫu

| Kịch bản | Tham số thay đổi | CPS (simulated) | So với A2 (simulated) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ vào, 260 đ ra cho 1.000 token | 4.723 đ | +5,6% |
| Giá token giảm nửa | 13 đ vào, 65 đ ra cho 1.000 token | 4.346 đ | −2,8% |
| Xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Xem lại giảm nửa | Tiền xem lại × 0,5 | 3.562 đ | −20,3% |
| Làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Làm lại giảm nửa | Tiền làm lại × 0,5 | 3.315 đ | −25,9% |
| Lương tăng 25% | 2.500 đ/phút | 5.506 đ | +23,1% |
| Tối đa 2 lượt | Chuyển ca cần lượt 3 cho nhân viên | 4.237 đ | −5,2% |
| Tối đa 1 lượt | Chuyển ca cần lượt 2 hoặc 3 cho nhân viên | 4.111 đ | −8,1% |

Với ca vượt giới hạn, giữ tiền token và tool đã dùng đến lượt cuối cho phép. Phút xem lại và làm lại của trợ lý cho ca chuyển bằng 0 theo giả định của đề.

## B2 · Thay đổi đồng thời và xếp hạng

Gấp đôi giá token và xem lại cho CPS **6.543 đ**, tăng **46,3%** (simulated). Hai khoản cộng tuyến tính, số việc thành công giữ nguyên.

Theo mức thay đổi đã thử, ba yếu tố mạnh nhất là làm lại (+51,8%), xem lại (+40,7%) và lương (+23,1%), đều simulated.

## B3 · Chi phí của cả hệ thống

| Giới hạn | Tổng chi phí trợ lý (simulated) | Ca chưa thành công | Tổng hệ thống (simulated) | CPS trợ lý (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lượt | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lượt | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lượt | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

**Hai lượt rẻ nhất cho công ty**. Kiểm tay: 4.093.220 + 234 × 12.000 = 6.901.220 đ (simulated). Một lượt cho CPS thấp nhất nhưng để lại thêm 85 ca cho nhân viên.

Ở cấu hình ba lượt, cả hệ thống tốn 7.037.585 / 1.200 = 5.865 đ/yêu cầu, khoảng 0,49× mốc thủ công (simulated, chưa phân bổ cố định).

## B4 · Xem lại 100% trong phạm vi pilot

Trong 982 yêu cầu, 948 ca có ít nhất một lượt `ok`, 48 ca làm lại và 900 ca thành công. Hóa đơn mọi lượt là 224.513 đ. Mỗi ca có câu trả lời được xem đúng một lần trong 5 phút.

| Phút làm lại/ca | Tổng biến phí (simulated) | CPS (simulated) | CPS / 12.000 đ (simulated) | Phút xem lại hòa vốn (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 9 theo đề | 10.568.513 đ | 11.743 đ | 0,98× | 5,12 |
| 15,3 theo trung bình toàn mẫu, làm tròn một chữ số (simulated) | 11.173.313 đ | 12.415 đ | 1,03× | 4,80 |

Ví dụ hàng đầu bằng (224.513 + 948 × 5 × 2.000 + 48 × 9 × 2.000) / 900. Cộng 82 ca × 12.000 đ theo B3 rồi chia 982, hai kịch bản lần lượt tốn 11.764 và 12.380 đ/yêu cầu (simulated, chưa cộng cố định).

Pilot cần đo phút thực tế và mức xem lại có thể giảm an toàn. Chỉ riêng việc đổi giả định làm lại từ 9 lên 15,3 phút đã đưa CPS qua mốc 12.000 đ (simulated).
