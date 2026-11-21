# Bảng lỗi và cách khắc phục

## Nhãn cho 20 ca

Duy phụ trách cột thứ nhất, Hiệp phụ trách cột thứ hai. Cả hai cột xuất phát từ nhãn Codex điền dựa trên mô tả từng ca và bảng nhãn tham khảo của lab. [Đề gốc](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx) · [Nhãn tham khảo](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhãn-tham-khảo-cho-20-ca)

<table>
<thead><tr><th>Ca</th><th>Tình huống</th><th>Nhãn Duy</th><th>Nhãn Hiệp</th></tr></thead>
<tbody>
<tr>
  <td>1</td>
  <td>Số tài khoản thiếu hai chữ số</td>
  <td>
    Do người dùng
  </td>
  <td>
    Do người dùng
  </td>
</tr>
<tr>
  <td>2</td>
  <td>Tra bảng giá thường cho kiện 28 kg</td>
  <td>
    Hệ thống
  </td>
  <td>
    Hệ thống
  </td>
</tr>
<tr>
  <td>3</td>
  <td>Khách đợi tiền về ngân hàng, hệ thống hoàn về ví</td>
  <td>
    Ngữ cảnh
  </td>
  <td>
    Ngữ cảnh
  </td>
</tr>
<tr>
  <td>4</td>
  <td>Thiếu dữ liệu chặng giao ở nước ngoài</td>
  <td>
    Giới hạn hệ thống
  </td>
  <td>
    Giới hạn hệ thống
  </td>
</tr>
<tr>
  <td>5</td>
  <td>Đối soát mẫu mới phát hiện hoàn theo giá trước giảm</td>
  <td>
    Ngầm
  </td>
  <td>
    Ngầm
  </td>
</tr>
<tr>
  <td>6</td>
  <td>Khách chọn giao trễ khi hàng bị vỡ</td>
  <td>
    Do người dùng
  </td>
  <td>
    Do người dùng
  </td>
</tr>
<tr>
  <td>7</td>
  <td>Sổ cái trả 503 nhưng thông báo đã hoàn</td>
  <td>
    Hệ thống
  </td>
  <td>
    Hệ thống
  </td>
</tr>
<tr>
  <td>8</td>
  <td>Trích dẫn điều khoản 7.2 không tồn tại</td>
  <td>
    Hệ thống
  </td>
  <td>
    Hệ thống
  </td>
</tr>
<tr>
  <td>9</td>
  <td>Nhập mã sàn thay cho mã vận đơn</td>
  <td>
    Do người dùng
  </td>
  <td>
    Do người dùng
  </td>
</tr>
<tr>
  <td>10</td>
  <td>Giao trễ do bão trong khi ứng dụng vẫn hẹn 24 giờ</td>
  <td>
    Ngữ cảnh
  </td>
  <td>
    Ngữ cảnh
  </td>
</tr>
<tr>
  <td>11</td>
  <td>Trợ lý chỉ đọc văn bản, khách gửi tin thoại</td>
  <td>
    Giới hạn hệ thống
  </td>
  <td>
    Giới hạn hệ thống
  </td>
</tr>
<tr>
  <td>12</td>
  <td>Chi phí tại D05 tăng gấp ba suốt ba tuần mới được phát hiện</td>
  <td>
    Ngầm
  </td>
  <td>
    Ngầm
  </td>
</tr>
<tr>
  <td>13</td>
  <td>Yêu cầu hoàn phí bảo hiểm ngoài phạm vi</td>
  <td>
    Giới hạn hệ thống
  </td>
  <td>
    Giới hạn hệ thống
  </td>
</tr>
<tr>
  <td>14</td>
  <td>Khách bấm nhầm xác nhận đã nhận tiền</td>
  <td>
    Do người dùng
  </td>
  <td>
    Do người dùng
  </td>
</tr>
<tr>
  <td>15</td>
  <td>Nhân viên bắt lỗi hoàn 100% thay vì 50%</td>
  <td>
    Hệ thống
  </td>
  <td>
    Hệ thống
  </td>
</tr>
<tr>
  <td>16</td>
  <td>Thông báo đúng quy trình nhưng gửi lúc 2:14 sáng</td>
  <td>
    Ngữ cảnh
  </td>
  <td>
    Ngữ cảnh
  </td>
</tr>
<tr>
  <td>17</td>
  <td>Bảng giá cũ làm lệch tiền 212 đơn, không ai mở lại</td>
  <td>
    Ngầm
  </td>
  <td>
    Ngầm
  </td>
</tr>
<tr>
  <td>18</td>
  <td>Tính đúng 15.000 đ nhưng tin nhắn thiếu cách tính</td>
  <td>
    Ngữ cảnh
  </td>
  <td>
    Ngữ cảnh
  </td>
</tr>
<tr>
  <td>19</td>
  <td>Đơn 14 tháng vượt giới hạn tra cứu 12 tháng</td>
  <td>
    Giới hạn hệ thống
  </td>
  <td>
    Giới hạn hệ thống
  </td>
</tr>
<tr>
  <td>20</td>
  <td>Lệnh gửi lại thiếu khóa chống trùng, tiền hoàn hai lần</td>
  <td>
    Hệ thống
  </td>
  <td>
    Hệ thống
  </td>
</tr>
</tbody>
</table>

Hai cột sau khi gộp commit trùng 20/20 ca (100%). Kết quả này đối chiếu các nhãn có cùng nguồn. Hồ sơ còn thiếu bằng chứng hai thành viên đã gắn nhãn độc lập trước khi so sánh theo yêu cầu Nhiệm vụ C.

## Khắc phục 5 ca, mỗi loại một ca

| Ca | Loại lỗi theo tình huống trong đề | Phát hiện và ngưỡng đề xuất | Khắc phục | Người phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Đếm số tài khoản sai độ dài trước khi gửi ngân hàng. Cảnh báo khi vượt 2% yêu cầu nhập tài khoản trong ngày. | Kiểm tra độ dài theo ngân hàng, chỉ rõ trường cần sửa và yêu cầu xác nhận lại. | Chủ sản phẩm hoàn phí |
| 7 | Hệ thống | Mỗi giờ nối thông báo đã hoàn với giao dịch sổ cái theo yêu cầu. Báo động ngay từ 1 thông báo thiếu giao dịch thành công. | Chỉ gửi xác nhận sau khi sổ cái ghi thành công. Lỗi 503 chuyển trạng thái chờ đối soát. | Kỹ sư trưởng tích hợp |
| 18 | Ngữ cảnh | Hằng tuần đếm ca mở lại vì số tiền trong các ca đã xác minh tính đúng. Rà mẫu tin nếu có từ 3 ca/tuần. | Ghi phí ban đầu, tỉ lệ áp dụng và số hoàn trên cùng thông báo. | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Mỗi ngày kiểm mọi yêu cầu quá 12 tháng. Báo khi có ít nhất 1 ca thiếu bản ghi chuyển người xử lý. | Nêu giới hạn tra cứu và chuyển mã đơn, thời điểm, lý do cho nhân viên có quyền tra kho lưu trữ. | Trưởng vận hành CSKH |
| 17 | Ngầm | Đối soát 100 đơn dưới 2 kg mỗi tuần với bảng giá có hiệu lực tại ngày xử lý. Điều tra ngay từ 1 ca lệch. | Ghi phiên bản bảng giá vào trace, vô hiệu bộ nhớ đệm khi đổi giá và đối soát lại các đơn bị ảnh hưởng. | Kế toán trưởng |
