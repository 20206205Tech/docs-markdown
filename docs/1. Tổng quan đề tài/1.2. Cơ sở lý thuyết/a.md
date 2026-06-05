# NGHIỆP VỤ HỆ THỐNG PHÁP LUẬT AI (REQUIREMENTS & ASSUMPTIONS)

Hệ thống hỗ trợ người dùng hỏi đáp pháp luật Việt Nam, phân tích hợp đồng và đàm thoại trực tiếp thời gian thực với trợ lý ảo pháp lý.

---

## 1. YÊU CẦU NGHIỆP VỤ (REQUIREMENTS)

- **Hiển thị thông tin dịch vụ**: Hệ thống liệt kê danh sách các nhân vật trợ lý ảo tư vấn pháp lý cùng các gói cước VIP hiện có của hệ thống.
- **Tìm kiếm thông tin**: Cho phép người dùng tìm kiếm thông tin giới thiệu và giá của các gói cước.
- **Đăng ký & Đăng nhập**: Khách vãng lai có thể đăng ký tài khoản mới và đăng nhập vào hệ thống bằng Email/Mật khẩu hoặc qua tài khoản Google.
- **Xem cuộc trò chuyện chia sẻ**: Cho phép bất kỳ ai (kể cả khách vãng lai chưa đăng nhập) xem nội dung cuộc trò chuyện được chia sẻ công khai qua liên kết.
- **Xác thực bảo mật bắt buộc**: Hệ thống bắt buộc thành viên thực hiện xác thực bảo mật 2 lớp (MFA 2FA) bằng mã OTP mỗi khi đăng nhập thành công.
- **Hỏi đáp pháp luật bằng văn bản**: Cho phép thành viên đăng ký gửi câu hỏi pháp luật bằng văn bản (Chat) và nhận phản hồi trực tiếp.
- **Đánh dấu & Lưu trữ**: Cho phép thành viên đăng ký lưu trữ tin nhắn quan trọng vào các thư mục bookmark cá nhân kèm ghi chú thích hợp.
- **Chia sẻ câu trả lời**: Cho phép thành viên đăng ký tạo liên kết chia sẻ câu trả lời tư vấn pháp lý ra ngoài hệ thống và thu hồi quyền chia sẻ khi cần.
- **Đàm thoại giọng nói (VIP)**: Cho phép thành viên VIP tham gia đàm thoại thời gian thực (Voice Chat) trực tiếp với nhân vật trợ lý AI được chọn.
- **Phân tích tài liệu (VIP)**: Cho phép thành viên VIP tải lên các tài liệu pháp lý (như hợp đồng dạng PDF) để AI tự động quét rủi ro pháp lý và đưa ra khuyến nghị sửa đổi.
- **Đăng ký gói cước VIP**: Thành viên có thể đăng ký mua gói cước VIP (1 tháng, 6 tháng, 12 tháng) thông qua liên kết thanh toán để nâng cấp tài khoản.
- **Quản trị nhân vật ảo**: Cho phép Quản trị viên thực hiện quản lý danh sách trợ lý ảo (Persona CRUD), cấu hình ảnh đại diện, lời chào mừng và giọng nói.
- **Quản trị cấu hình giọng nói**: Cho phép Quản trị viên quản lý, cấu hình các công cụ chuyển văn bản thành giọng nói (TTS Engines) và danh sách giọng nói (Voices) tích hợp trong hệ thống.
- **Quản trị gói cước**: Cho phép Quản trị viên thêm/sửa/xóa gói dịch vụ và kích hoạt thủ công VIP cho tài khoản người dùng theo mã giao dịch.
- **Vận hành dữ liệu luật**: Cho phép Quản trị viên giám sát và vận hành các quy trình nạp văn bản quy phạm pháp luật (data-pipeline cho VBPL và Pháp điển).

---

## 2. GIẢ ĐỊNH HỆ THỐNG (ASSUMPTIONS)

- **Quyền truy cập của khách vãng lai**: Khách vãng lai (chưa đăng nhập) chỉ được phép xem thông tin giới thiệu, bảng giá dịch vụ, nghe thử giọng chào của trợ lý AI và xem nội dung cuộc trò chuyện được chia sẻ công khai. Họ không được phép đặt câu hỏi, phân tích tài liệu hay kết nối Voice Chat.
- **Truy cập liên kết chia sẻ công khai**: Khách vãng lai và thành viên đều có thể mở liên kết chia sẻ để đọc nội dung tư vấn pháp lý mà không cần thực hiện đăng nhập tài khoản.
- **Quyền truy cập của thành viên đăng ký**: Thành viên đăng ký được toàn quyền sử dụng tính năng trò chuyện văn bản thông thường (Chat), chia sẻ liên kết cuộc trò chuyện công khai và sử dụng hệ thống thư mục bookmark để lưu giữ ghi chú.
- **Quyền truy cập của thành viên VIP**: Chỉ có thành viên sở hữu gói cước VIP hoạt động mới được sử dụng các tính năng nâng cao bao gồm: Trò chuyện qua Giọng nói (Voice Chat thời gian thực) và Tải lên rà soát tài liệu hợp đồng.
- **Chế độ suy luận nâng cao**: Hệ thống hỗ trợ tính năng Suy luận chuyên sâu (Reasoning Mode) để hỗ trợ trích dẫn nguồn luật chính xác, giảm thiểu hiện tượng ảo tưởng thông tin của AI.
- **Hạ tầng đàm thoại**: Tính năng Voice Chat thời gian thực yêu cầu kết nối mạng băng thông rộng ổn định của người dùng và sử dụng máy chủ LiveKit Server làm trung gian truyền phát luồng âm thanh WebRTC.
- **Định dạng tài liệu phân tích**: Tính năng phân tích tài liệu hỗ trợ các định dạng file văn bản phổ biến (như PDF) với dung lượng tệp giới hạn trong phạm vi cho phép của hệ thống.
- **Cơ sở dữ liệu pháp luật**: Dữ liệu pháp lý được cập nhật tự động định kỳ thông qua hệ thống data-pipeline đồng bộ từ nguồn Cơ sở dữ liệu quốc gia về văn bản pháp luật và hệ thống Pháp điển Việt Nam.
- **Bảo mật hai yếu tố (2FA TOTP)**: Xác thực 2FA là quy trình bắt buộc tích hợp trực tiếp vào bước Đăng nhập. Người dùng không thể truy cập các tính năng bên trong hệ thống nếu chưa hoàn tất xác thực OTP.
- **Giao dịch thanh toán**: Giao dịch nâng cấp VIP được xử lý thông qua tích hợp cổng thanh toán trực tuyến bên thứ ba.
