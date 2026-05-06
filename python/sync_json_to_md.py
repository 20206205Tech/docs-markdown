import os

# Dữ liệu thuật ngữ
DATA = [
    {"abbr": "AI", "eng": "Artificial Intelligence", "vie": "Trí tuệ nhân tạo"},
    {
        "abbr": "API",
        "eng": "Application Programming Interface",
        "vie": "Giao diện lập trình ứng dụng",
    },
    {"abbr": "LLM", "eng": "Large Language Model", "vie": "Mô hình ngôn ngữ lớn"},
    {
        "abbr": "RAG",
        "eng": "Retrieval Augmented Generation",
        "vie": "Tạo tăng cường truy xuất",
    },
    {"abbr": "DDD", "eng": "Domain Driven Design", "vie": "Thiết kế hướng miền"},
    {"abbr": "MSA", "eng": "Microservices Architecture", "vie": "Kiến trúc vi dịch vụ"},
]


# <!-- NLP,Natural Language Processing,Xử lý ngôn ngữ tự nhiên -->

# <!-- JSON,JavaScript Object Notation,Ký hiệu đối tượng JavaScript -->

# <!-- UML -->


def generate_markdown():
    # Path relative to the root of the repository
    md_path = os.path.join("docs", "0", "1.md")

    # Sắp xếp theo Từ viết tắt (A-Z)
    sorted_data = sorted(DATA, key=lambda x: x["abbr"])

    # Tạo nội dung Markdown
    md_content = "# Danh sách viết tắt\n\n"
    md_content += "| Từ viết tắt | Tên tiếng Anh | Nghĩa tiếng Việt |\n"
    md_content += "| --- | --- | --- |\n"

    for item in sorted_data:
        md_content += f"| {item['abbr']} | {item['eng']} | {item['vie']} |\n"

    # Ghi ra file markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"Successfully updated {md_path}")


if __name__ == "__main__":
    generate_markdown()
