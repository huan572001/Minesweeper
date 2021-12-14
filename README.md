# Minesweeper
I. Hướng dẫn cài đặt thư viện Pygame
- Đầu tiên các bạn vào terminal và nhập câu lệnh: "pip install pygame" để cài đặt thư viện Pygame

II. Hướng dẫn chơi game Minesweeper 
1. Mục tiêu
  - Trong Minesweeper, người chơi phải mở được tất cả các ô không có mìn trên một bảng ô vuông.
![image](https://user-images.githubusercontent.com/92346171/145825564-5fd08f69-96cd-43eb-a16d-c6fbe1b20fb1.png)

2. Luật chơi:
  - Người chơi khởi đầu với một bảng ô vuông trống thể hiện "bãi mìn".
  - Click chuột vào một ô vuông trong bảng. Nếu không may trúng phải ô có mìn (điều này thường xảy ra với người mới chơi) thì trò chơi kết thúc. Trường hợp khác là ô đó không có    mìn và một vùng các ô sẽ được mở ra cùng với những con số. Số trên một ô là lượng mìn trong 8 ô nằm quanh với ô đó.
  - Nếu chắc chắn một ô có mìn, người chơi đánh dấu vào ô đó bằng hình lá cờ (click chuột phải).
  - Khi 8 ô lân cận trong một số đã có đủ số mìn mà vẫn còn các ô khác thì những ô đó không có mìn
  - Trò chơi kết thúc với phần thắng dành cho người chơi nếu mở được tất cả các ô không có mìn.
![image](https://user-images.githubusercontent.com/92346171/145823268-09f16685-6856-4abb-9903-153f98f09c95.png)

Trò chơi chia làm ba cấp độ:
  - Dễ (beginner): bảng ô vuông 9×9 trên đó rải 10 quả mìn
  - Trung bình (intermediate): bảng ô vuông 16 × 16 trên đó rải 40 quả mìn
  - Khó (expert): bảng ô vuông 20x20 trên đó rải 60 quả mìn
 ![image](https://user-images.githubusercontent.com/92346171/145823174-88d9f52e-c2a6-4a50-9495-a48edbacd5b5.png)

 3. Tính chất:
  - Tính logic: Trò chơi dựa trên cơ sở tính toán sự phân phối (trong không gian) các quả mìn dựa trên dữ kiện là các con số hiện ra (chỉ số lượng quả mìn kề với một ô).
  - Tính ngẫu nhiên: Trong một số trường hợp, không thể xác định chính xác vị trí của mìn chỉ dựa vào những con số gợi ý; do đó trò chơi mang tính may rủi. Bên cạnh đó, một số người chơi còn thắng trực tiếp ngay với 1 click chuột đối với những ván có số lượng mìn thưa thớt (đặc biệt trong trình độ Beginner - dễ).

4. Hướng dẫn chạy game:
  Tải source code về và chạy file Minesweeper.sh
