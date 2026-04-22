# Xây dựng ứng dụng tư vấn pháp luật sử dụng AI

Yêu cầu chức năng dự kiến:

- [x] Ghi lại thông tin request (request logs)

- [ ] ~~Ghi lại thông tin response: có request_id, code, success, message, data, total~~

- [x] Cài đặt người dùng (user-settings)
  - [ ] Bật tắt Dark mode
  - [ ] Bật tắt Tự động phát âm thanh khi trả lời
  - [ ] Cấu hình Model mặc định (Cấp 1, 2, 3) về độ chính xác/tốc độ
  - [ ] Cài đặt "Bối cảnh cá nhân" (Tự nhập thêm ai prompt)
  - [ ] ~~Bật tắt Xác thực 2FA (có thể thêm sau)~~

- [x] Xác thực (auth - dùng supabase)
  - [x] Người dùng đăng nhập bằng google
    - [ ] ~~Hệ thống gửi email để xác nhận~~
    - [ ] ~~Người dùng xác nhận email~~
  - [x] Xem thông tin cá nhân (profile)
    - [ ] Đếm thông tin số lượng sử dụng Token để tạo thống kê như github
    - [x] Cập nhật ảnh avatar
  - [ ] ~~Chuyển 1 user thành admin (cần Role ADMIN)~~
  - [ ] ~~Xác thực 2FA bằng TOTP (có thể thêm sau)~~

- [x] Thanh toán Token (dùng VNPAY sandbox)
  - [x] Hiển thị các mức giá ~~(mua nhiều được giảm %)~~
  - [x] Người dùng mua số lượng Token
  - [x] Lưu lịch sử giao dịch
  - [ ] Mỗi lần chat, hệ thống sẽ tính số lượng token (prompt đầu vào và response đầu ra)
  - [ ] Cửa sổ bật lên thông báo khi hết lượt dùng

- [x] Lựa chọn nhân vật để trò chuyện
  - [x] CRUD nhân vật (cần Role ADMIN)
  - [x] Người dùng lựa chọn nhân vật để trò chuyện

- [ ] Cuộc trò chuyện (chat)
  - [ ] Đầu vào INPUT
    - [ ] Giao diện có phần input nhập văn bản
      - [ ] Có 1 số câu hỏi gợi ý mặc định
    - [ ] Có thể thêm micro giọng nói
      - [ ] Sóng âm (waveform animation)
    - [ ] Tải lên file tài liệu văn bản (.pdf)
  - [ ] Đầu ra OUTPUT
    - [ ] Trích xuất các nguồn tài liệu liên quan
    - [ ] Lịch sử cuộc trò chuyện
  - [ ] Chia sẻ cuộc trò chuyện (CRUD)
  - [ ] Ghi chú (note)
    - [ ] Người dùng có thể thả tim yêu thích cuộc trò chuyện
    - [ ] Cho phép người dùng phân loại theo chủ đề (labels)

- [ ] Thông báo (notification) - Worker
  - [ ] Gửi email chào mừng đăng ký người dùng mới
  - [ ] Thông báo cho người dùng dữ liệu văn bản mới (qua mail)
  - [ ] Thông báo cho người dùng về thanh toán (sắp hết số lượng, thành công)

- [ ] Chức năng Dashboard của ADMIN
  - [ ] Tổng số người dùng hệ thống
  - [ ] Tổng số người dùng hôm nay
  - [ ] Thống kê chi phí Token API (tiền trả cho OpenAI/Anthropic/Google...).
  - [ ] Thống kê doanh thu theo ngày/tháng từ VNPAY.
