Hỏi file => không hiểu => phải cho ai hiểu metadata, STATE => thêm tool

Do cần thời gian phản hồi nhanh cả gRPC và voice: tôi muốn chủ đề topic = null. Sau đó sẽ được xử lý sau?

Tương tự tôi nghĩ cần bỏ summarize_history và sẽ chạy việc đó sau

<!-- Cần chỉnh lại phần chia sẻ vì có thêm phần nước suy luận và nguồn tài liệu -->

http://localhost:3000/share/01ee2872-36bb-4491-8c4f-283f09e5eee5/undefined

http://localhost:3000/share/ec392f3c-57f1-4150-b6e8-6a7052568249/undefined

<!-- cd ~/Documents/GitHub/docs-markdown && code . -->

<!-- Tắt mic khi RAG -->
<!-- Khả năng đợi xác nhận: text x, voice y -->

Xử lý ngắt lời => dừng RAG

<!--  -->

await context.session.say("Let me search for that...")
context.disallow_interruptions()

<!--  -->

Xử lý Ngắt lời (Barge-in) khi đang chạy Tool

LiveKit hỗ trợ ngắt TTS khá tốt khi người dùng nói chen vào. Tuy nhiên, nếu Agent đang trong quá trình thực thi một chuỗi reasoning dài hoặc đang thực hiện các tác vụ nặng ở background, việc người dùng đổi ý và ngắt lời cần phải dừng luôn cả các tiến trình logic đó.

Xử lý: Cần đảm bảo các task bất đồng bộ trong chuỗi reasoning có hỗ trợ "cancellation token" hoặc check trạng thái bị ngắt để tránh việc Agent tốn token API để tính toán một kết quả mà người dùng không còn quan tâm nữa.

<!--  -->

Tắt bằng câu nói?

Xác nhận bằng câu nói

Nút xác nhận continue

<!--  -->

- **`agent_false_interruption` / `overlapping_speech**`: Xảy ra khi hệ thống nhận diện việc ngắt lời (người dùng nói xen vào khi AI đang nói).

Hướng dẫn ứng dụng

agent_false_interruption

overlapping_speech

=> dừng RAG

<!--  -->

ặc "Xác nhận", trong đó khách hàng gửi một chuỗi dữ liệu cụ thể để buộc tổng đài viên bắt đầu xử lý giọng nói

<!--  -->

BUG:

<!-- chuyển nhân vật: Đang Nữ => chuyển Nam, phải hiện nam -->
<!--, chat hiện mặc định => đúng -->

<!--  -->

Có tài liệu Pháp điển=> nhưng AI lại bảo không biết

<!--  -->

DOMAIN DRIVEN DESIGN

cron và redis : dùng domain, application

<!--  -->

<!-- kafka? -->
<!-- Sự kiện... cộng dồn => chỉ lưu update -->
<!-- Queue lỗi gửi lỗi nhận -->

RAGAs
