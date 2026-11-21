# Báo cáo cá nhân · Đoàn Văn Hiệp

## 1. Thông tin thành viên

2A202603565 · hiep24042002@gmail.com · Phụ trách cột nhãn thứ hai, viết phần tính D–E và giữ hồ sơ.

## 2. Phần việc phụ trách

Tính cỡ mẫu D1 và chỉ số E1, lập kế hoạch pilot, ghép hồ sơ Gate 2a và rà soát 20 ca trong cột Hiệp.

## 3. Đóng góp cụ thể

Bản bàn giao gồm phép tính cỡ mẫu, kế hoạch chia 20 + 20 nhân viên, luật dừng, danh sách event và hồ sơ đề xuất. Patch của Hiệp điền 20 ô ở cột Hiệp. Mỗi ô có thể sửa trước khi commit.

## 4. Bằng chứng

20 × 299 / [1 + 298 × 0,02] = 859,20 yêu cầu hiệu dụng/nhánh. Mẫu chạy thử có 39/982 ca mở lại trong phạm vi pilot. [Kế hoạch](pilot_plan.yaml) · [Chỉ số](chi_so.md) · [Hồ sơ](ho_so_launch_v0.md)

## 5. Công cụ AI đã dùng

Codex hỗ trợ soạn phép tính, YAML, hồ sơ và điền cột nhãn theo tài liệu tham khảo của lab. Hiệp đối chiếu D1 với phép tính tay trên, chạy `yaml.safe_load` và ghi kết quả thực tế khi duyệt.

## 6. Tự đánh giá

- **Đánh đổi giữa mức chênh 5 và 6 điểm:** Khi phân cụm theo nhân viên với hệ số tương quan nội cụm ICC = 0,02 trên 20 nhân viên/nhánh, trần cỡ mẫu hiệu dụng tối đa chỉ đạt 1.000 (K / ICC = 20 / 0,02 = 1.000). Mức chênh lệch mục tiêu 5 điểm (MDE = 0,05) đòi hỏi tới 1.251 yêu cầu hiệu dụng nên về mặt toán học không thể đạt đủ power 80% với 20 nhân viên/nhánh (power thực tế chỉ đạt ~0,642). Nhóm chấp nhận đánh đổi nới MDE lên 6 điểm phần trăm (MDE = 0,06) để giảm cỡ mẫu hiệu dụng mục tiêu xuống 859 yêu cầu/nhánh, tương ứng cần 299 yêu cầu/nhân viên (5.980 yêu cầu thô/nhánh, DE = 6,96). Thiết kế này hoàn toàn khả thi về mặt vận hành (40 nhân viên trong 12 depot chạy trong khoảng 6 tuần), dù phải chấp nhận rủi ro giảm lực phát hiện nếu hiệu quả thực tế chỉ tăng 5 điểm.
- **Rà soát 20 ca ở cột Hiệp:** Đã rà soát kỹ lưỡng toàn bộ 20 ô trong cột Hiệp. Tất cả 20 nhãn đều trùng khớp 100% với nhãn tham khảo của lab và trùng khớp với cột của Duy. Trong đó, Ca 18 ("Tính đúng 15.000 đ nhưng tin nhắn thiếu cách tính") là ca cần lưu ý nhất: đây là lỗi "Ngữ cảnh", dễ nhầm với lỗi "Hệ thống" hoặc "Do người dùng". Hệ thống đã tính đúng 15.000 đ theo chính sách và khách hàng không nhập sai thông tin, nhưng khách khiếu nại vì tin nhắn thiếu diễn giải cách tính (30.000 đ × 50% = 15.000 đ), do đó giả định của hệ thống về việc khách tự hiểu là không khớp với ngữ cảnh người dùng. Ca 12 ("Chi phí tại D05 tăng gấp ba suốt 3 tuần mới phát hiện") cũng là ca cần lưu ý thuộc loại "Ngầm" do hệ thống vẫn xử lý xong yêu cầu nhưng chi phí vận hành bị đội lên âm thầm mà không ai phát hiện trước khi đối soát.
