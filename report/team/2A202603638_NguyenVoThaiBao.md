# Báo cáo cá nhân · Nguyễn Võ Thái Bảo

## 1. Thông tin thành viên

2A202603638 · baonguyenvothai@gmail.com · Nhóm trưởng, phụ trách mô hình chi phí.

## 2. Phần việc phụ trách

Phần A–B trong `src/lab13.py`, tích hợp hồ sơ của Duy và Hiệp và giữ phiếu chấm nhóm bạn.

## 3. Đóng góp cụ thể

Mô hình trong commit `0da18d4` tính tiền token và tool trên mọi lượt chạy. Khi hạ giới hạn lượt, mô hình giữ chi phí các lượt đã chạy, chuyển yêu cầu còn dang dở cho nhân viên và tính riêng chi phí làm thay.

## 4. Bằng chứng

Ba phép thử A1 cho 1,20 · 1,25 · 1,25. Ở B3, giới hạn 2 lượt có 234 ca cần nhân viên và tổng chi phí 6.901.220 đ (simulated). [Mã nguồn](../../src/lab13.py)

## 5. Công cụ AI đã dùng

Codex hỗ trợ viết, chạy mô hình và soạn patch. Cách kiểm tay B3 là cộng 4.093.220 đ (simulated) với 234 × 12.000 đ, rồi đối chiếu dòng 2 lượt.

## 6. Tự đánh giá

Đối chiếu do Codex thực hiện sau khi gộp: ba phép A1 đạt. Giới hạn 1 lượt giảm CPS xuống 4.111 đ nhưng để lại 319 ca. Giới hạn 2 lượt còn 234 ca và cho tổng chi phí hệ thống thấp nhất, 6.901.220 đ (các số chi phí là simulated).

Nhận xét cá nhân của Bảo chờ xác nhận.
