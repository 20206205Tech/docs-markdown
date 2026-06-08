import os


def create_markdown_files():
    # Thư mục đích
    folder = r"C:\Users\Admin\Documents\git\docs-markdown\temp_service"

    # Nội dung đầu vào
    text = """
# Dịch vụ xác thực (auth service - dùng supabase)
# Dịch vụ cài đặt (setting service - dùng neon api)
# Dịch vụ thanh toán (payment service)
# Dịch vụ trò chuyện (conversation service)
# Dịch vụ chatbot (chatbot service)
# Dịch vụ văn bản (document service)
# Dịch vụ nhân vật (persona service)
    """.strip()

    # Tạo thư mục nếu chưa tồn tại
    os.makedirs(folder, exist_ok=True)

    # Tách chuỗi thành các dòng và loại bỏ các dòng trống
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    # Duyệt qua từng dòng và tạo file
    for index, line in enumerate(lines, start=1):
        file_name = f"{index}.md"
        file_path = os.path.join(folder, file_name)

        # Đảm bảo nội dung là thẻ h1 (Heading 1)
        h1_text = line if line.startswith("#") else f"# {line}"

        # Ghi nội dung vào file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"{h1_text}\n")

        print(f"Đã tạo thành công: {file_name}")


if __name__ == "__main__":
    create_markdown_files()
