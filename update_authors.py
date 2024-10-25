import os

# Tên tác giả mới
new_author = "DemonGod"

# Đọc dữ liệu từ file "authors.txt" chứa đường dẫn đến file và tên cũ
with open('authors.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Duyệt qua từng cặp dòng trong file authors.txt (một dòng là đường dẫn, một dòng là tên tác giả)
for i in range(0, len(lines), 2):  # Mỗi tác giả nằm trên 2 dòng (đường dẫn file và dòng chứa tác giả)
    file_path = lines[i].strip()  # Đường dẫn đến file cần sửa

    # Sử dụng os.path để chuẩn hóa đường dẫn
    file_path = os.path.normpath(file_path)
    
    old_author_line = lines[i + 1].strip()  # Dòng chứa thông tin tác giả cũ
    
    # Thay thế dòng "author: ..." bằng dòng với tên tác giả mới
    if 'author:' in old_author_line:
        new_author_line = f'author: "{new_author}"'
        
        # Kiểm tra nếu file tồn tại trước khi mở
        if os.path.exists(file_path):
            # Đọc nội dung của file gốc
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Thay thế author cũ bằng author mới
            new_content = content.replace(old_author_line, new_author_line)
            
            # Ghi lại file với nội dung đã thay thế
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"Đã thay đổi '{old_author_line}' thành '{new_author_line}' trong file {file_path}")
        else:
            print(f"File '{file_path}' không tồn tại.")
