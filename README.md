# I. Hướng dẫn cài đặt
1. Cài đặt python3: https://www.python.org/downloads/
2. Clone code về máy
```
git clone git clone https://github.com/nguyenthang0111/auto-grade-output.git cd auto_grade_input
```

3. Cài đặt gói selenium
```
pip3 install selenium
```
4. Cài đặt trình duyệt Chrome(nếu chưa có)

# II. Auto lấy điểm từ Ctt
1. Chuẩn bị nội dung file csv có 2 giá trị user và password.
Ví dụ về nội dung file csv như sau:
```
{"user": "12345678", "password": "abc123"}
```
Với user là MSSV do trường cấp
    password là mật khẩu để đăng nhập vào hệ thống ctt-sis

2. Mở cmd của thư mục hiện tại và chạy code
```
`python main.py`
```

3. Nhập mã captcha: có 8 giây để đọc và gõ mã captcha vào ô. Gõ xong chờ đủ 8 giây để chương trình tiếp tục chạy. Nhớ **KHÔNG** được ấn nút **Đăng nhập**! 
4. Mọi thứ tiếp tục được chạy tự động, không can thiệp vào cửa sổ trình duyệt trong quá trình chạy. Sau khi bot chạy xong, bảng điểm sẽ được hiển thị trong file result.csv
