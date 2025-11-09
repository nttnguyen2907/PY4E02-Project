
Bước 1: tạo môi trường ảo 
python -m venv venv

Bước 2: Kích hoạt môi trường ảo:

Windows:

venv\Scripts\activate


macOS / Linux:

source venv/bin/activate

Bước 3: Cài đặt thư viện
pip install -r requirements.txt

Bước 4: CHẠY ỨNG DỤNG
Trong terminal (đang ở thư mục gốc của dự án), gõ lệnh:
streamlit run streamlit_app.py


CHỨC NĂNG CHÍNH CỦA ĐỒ ÁN 
🔍 Bộ lọc dữ liệu

Giới tính (Gender)

Chế độ ăn (Diet Type)

Loại bài tập (Workout Type)

📈 Biểu đồ hiển thị
Biểu đồ	Mô tả
🔥 Calories Burned theo độ tuổi	 Hiển thị mức năng lượng đốt cháy ở các nhóm tuổi
⚖️ Mối tương quan giữa BMI và Calories	Cho thấy ảnh hưởng của chỉ số BMI tới năng lượng tiêu hao
💪 Phân bố loại bài tập	  Biểu đồ tròn thể hiện tần suất các loại bài tập
🥦 Phân bố chế độ ăn	Biểu đồ tròn thể hiện tỉ lệ các chế độ dinh dưỡng
📤 Chức năng xuất dữ liệu

Nút “Xuất báo cáo” giúp người dùng tải file .csv chứa dữ liệu đã lọc.

🧠 ỨNG DỤNG AI TRONG DỰ ÁN

Ứng dụng sử dụng mô hình học máy đơn giản để:

Phân tích mối tương quan giữa BMI và Calories Burned.

Gợi ý mức năng lượng tiêu hao mong đợi dựa trên BMI và thời gian tập luyện.
(Áp dụng trực tiếp trong phần xử lý dữ liệu bên trong streamlit_app.py.)
