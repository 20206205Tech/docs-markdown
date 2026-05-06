import base64

import requests


def mermaid_to_image(mermaid_code: str, output_file: str):
    # 1. Mã hóa chuỗi Mermaid sang Base64
    # mermaid.ink yêu cầu chuỗi base64 ở định dạng URL-safe
    graphbytes = mermaid_code.encode("utf-8")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("utf-8")

    # 2. Tạo URL API (có thể đổi /img/ thành /svg/ nếu muốn xuất file vector)
    url = f"https://mermaid.ink/img/{base64_string}"

    # 3. Gọi API và tải ảnh về
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(response.content)
        print(f"Đã lưu ảnh thành công tại {output_file}")
    else:
        print(f"Lỗi khi tải ảnh: {response.status_code}")


# --- Chạy thử ---
code = """


mindmap
  root((Hệ Thống Chatbot DDD))
    Core_Subdomain["Miền phụ cốt lõi (Core)"]
      Conversation_Service
        Câu hỏi gợi ý
        Nhập Text/Voice
        Chia sẻ & Lưu trữ
      Chatbot_Service
        Stream chat
        Tra cứu văn bản (RAG)
    Supporting_Subdomain["Miền phụ hỗ trợ (Supporting)"]
      Document_Service
        Tải lên tài liệu
        Theo dõi trạng thái
      Persona_Service
        Quản lý nhân vật (Admin)
        Lựa chọn nhân vật trò chuyện
    Generic_Subdomain["Miền phụ chung (Generic)"]
      Auth_Service_Supabase
        Google Login
        Profile & Avatar
        Xác thực 2FA (TOTP)
      Setting_Service
        Cấu hình UI (Dark mode)
        Cấu hình Chat (Auto-send, Audio)
      Payment_Service
        Gói dịch vụ & Giá
        Thanh toán & Lịch sử
      Admin_Dashboard


"""

mermaid_to_image(code, "architecture.png")
