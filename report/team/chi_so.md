# Chỉ số và rủi ro kinh tế của pilot

## E1 · Chỉ số trong đợt chạy thử

| Loại | Chỉ số | Tử số / mẫu số theo yêu cầu duy nhất | Kết quả |
| --- | --- | --- | ---: |
| Chính | Đóng trong 24 giờ và không mở lại trong 7 ngày | Số ca có `dong_trong_24h=1` và `mo_lai_trong_7_ngay=0` / tổng ca | 994/1.200 = 82,83% |
| Dùng | Bỏ qua gợi ý | Số quyết định cuối là sửa hoặc bỏ / số ca đã xem lại | (41 + 7)/177 = 27,12% |
| An toàn | Mở lại trong 7 ngày, chỉ báo lỗi lọt | Số ca mở lại trong cửa sổ / tổng ca | 51/1.200 = 4,25% |
| Dùng | Nhân viên mở gợi ý | Số ca can thiệp có nhân viên mở gợi ý / số ca đủ điều kiện trong nhánh can thiệp | Đo trong pilot |
| An toàn | Sai số tiền qua đối soát mẫu | Số ca kiểm có số tiền ghi sổ khác số tiền đúng / số ca được kiểm | Đo trong pilot |

Mẫu chạy thử thiếu đối chứng đồng thời. Mức 82,83% mô tả đợt chạy thử. Baseline 70% là giả định lập cỡ mẫu. Trong phạm vi pilot, tỉ lệ mở lại là 39/982 = 3,97%.

## Event và cách nối

Mỗi event có `event_id` chống đếm trùng, `occurred_at`, `request_id` và `trace_id`. Dịch vụ tiếp nhận cấp trace cho cả yêu cầu đối chứng. Đếm chỉ số theo yêu cầu, nối lượt chạy bằng `request_id` và `trace_id`.

| Event | Bên ghi | Thuộc tính ngoài khóa chung | Thời điểm ghi |
| --- | --- | --- | --- |
| request_created | Dịch vụ tiếp nhận | trace_id, staff_id, depot, loai, arm, eligible | Khi nhận yêu cầu, trước xử lý |
| agent_run_completed | Trợ lý | trace_id, attempt, tokens_in, tokens_out, tool_calls, status | Khi kết thúc mỗi lượt, kể cả lỗi |
| suggestion_opened | Giao diện CSKH | trace_id, staff_id, suggestion_id | Khi nhân viên thực sự mở gợi ý |
| review_decided | Giao diện CSKH | trace_id, staff_id, decision, review_minutes | Khi chốt giữ, sửa hoặc bỏ |
| rework_completed | Giao diện CSKH | trace_id, staff_id, rework_minutes, reason | Khi nhân viên hoàn tất làm lại |
| ledger_write | Dịch vụ sổ cái | trace_id, order_id, refund_key, amount, status | Mỗi lần ghi hoặc nhận lại lệnh trùng |
| refund_notice_sent | Dịch vụ thông báo | trace_id, order_id, refund_key, message_status | Khi gửi trạng thái hoàn cho khách |
| handed_to_staff | Bộ điều phối | trace_id, reason, staff_id | Khi chuyển sang luồng thủ công |
| ticket_closed | Hệ thống ticket | trace_id, resolution, handler | Khi đóng yêu cầu |
| ticket_reopened | Hệ thống ticket | trace_id, reason | Khi mở lại yêu cầu |
| audit_checked | Kế toán | trace_id, ledger_amount, correct_amount, tariff_version | Khi hoàn tất đối soát ca được chọn mẫu |

| Chỉ số | Event dùng để tái tính |
| --- | --- |
| Đóng trong 24 giờ, giữ đóng 7 ngày | Lấy `request_created` làm mẫu số. Kiểm lần đóng đầu trong 24 giờ qua `ticket_closed`, rồi tìm `ticket_reopened` trong 7 ngày sau đóng. Chốt khi toàn bộ lứa ca đã đủ thời gian quan sát. |
| Bỏ qua gợi ý | Lấy quyết định cuối trên mỗi yêu cầu trong `review_decided`. Đếm sửa + bỏ chia cho giữ + sửa + bỏ. |
| Mở lại trong 7 ngày | Theo lứa `request_created`, dùng `ticket_closed` và `ticket_reopened` để đếm mỗi ca mở lại một lần trong 7 ngày sau đóng. Ca chưa đóng sau 24 giờ trượt chỉ số chính. |
| Nhân viên mở gợi ý | Nối `suggestion_opened` với `request_created` có `arm=can_thiep` và `eligible=true`. |
| Sai số tiền | Đếm một kết quả `audit_checked` cuối trên mỗi yêu cầu được chọn từ sổ cái rồi so hai số tiền. |

## E2 · Rủi ro kinh tế

| Rủi ro | Tác động theo bảng độ nhạy | Dấu hiệu theo dõi | Hành động | Phụ trách |
| --- | --- | --- | --- | --- |
| Làm lại tăng gấp đôi | Toàn mẫu lên 6.787 đ/việc, tăng 51,8% (simulated) | Tỉ lệ làm lại trong phạm vi vượt 7%/tuần, so với 48/982 = 4,89% ở mẫu | Rà 20 trace làm lại, xác định loại và lỗi lặp, tạm giữ bậc | PM trợ lý hoàn phí |
| Phải xem lại mọi câu trả lời | B4 đạt 11.743–12.415 đ/việc (simulated), tùy phút làm lại | Cuối tuần đầu, đo thời gian trên mỗi ca đã xem và so với ngưỡng hòa vốn 4,80–5,12 phút (simulated) | Đối soát tiền trước khi giảm tỉ lệ xem lại cho ca rủi ro thấp, tiếp tục kiểm mẫu sau giảm | Trưởng nhóm CSKH |

Chi phí được tính lại từ thời gian thực ghi ở hai event `review_decided` và `rework_completed`. [Bảng A–B và giả định](bang_chi_phi.md)
