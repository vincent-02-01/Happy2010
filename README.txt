THIỆP 20/10 - MATRIX RAIN MÀU HỒNG
====================================

1. MỞ NGAY
   - Giải nén thư mục.
   - Mở file index.html bằng Chrome, Safari, Edge hoặc trình duyệt điện thoại.
   - Nhấn “Mở món quà ♡”.
   - Trên điện thoại: xoay ngang để gần giống video.

2. CHỈNH NỘI DUNG
   - Mở index.html bằng VS Code/Notepad.
   - Tìm SETTINGS.messages để đổi các câu và thời gian.
   - Dùng ký tự \n để xuống dòng trong nội dung.
   - SETTINGS.finalText: chữ ở giữa trái tim.
   - SETTINGS.finalCaption: câu ghi phía dưới.
   - SETTINGS.rainColor: màu RGB của mưa ký tự.

3. NHẠC
   - File nhac-nen.mp3 đi kèm là nhạc nền tạo riêng cho mẫu demo.
   - Có thể thay bằng nhạc MP3 khác nhưng phải giữ tên nhac-nen.mp3.
   - Nhấn “Bật nhạc / Tắt nhạc” sau khi xem hết hoặc bật tắt theo ý muốn.
   - Trình duyệt di động chỉ tự phát nhạc sau khi người xem chạm vào nút bắt đầu.

4. CHIA SẺ BẰNG QR NHƯ VIDEO
   - Đưa cả index.html và nhac-nen.mp3 lên GitHub Pages / Netlify.
   - Tạo QR code trỏ đến đường dẫn web vừa công khai.
   - In QR trên thiệp, quét bằng điện thoại để mở hiệu ứng.
   - Nếu chỉ mở file local trên máy, mã QR không thể làm người khác truy cập file đó.

Công nghệ: HTML/CSS/JavaScript Canvas, không cần framework hay thư viện.

5. TỰ TẠO THIỆP QR IN GIẤY (TÙY CHỌN)
   - Cài Python, chạy: pip install pillow "qrcode[pil]"
   - Chạy: python tao-qr.py "https://duong-dan-web-cua-ban"
   - Sẽ tạo file thiep-qr-20-10.png để in/đăng bài.
   - QR chuẩn dạng hình vuông nằm trong đồ họa trái tim, nhằm giữ khả năng quét tốt.
   - Bạn phải có URL công khai trước khi tạo QR chia sẻ cho người khác.
