import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime
import io

# === Cấu hình trang ===
st.set_page_config(page_title="Phân tích Dinh dưỡng & Thể chất", layout="wide")
st.title("🥗 Dashboard Phân tích Dinh dưỡng & Hoạt động Thể chất")
st.caption(f"Cập nhật lần cuối: {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}")

# === Đọc dữ liệu ===
df = pd.read_csv("data/meal_metadata.csv")
df.columns = df.columns.str.strip()  # Làm sạch tên cột

# === Bộ lọc dữ liệu ===
st.sidebar.header("Bộ lọc dữ liệu")

gender = st.sidebar.multiselect("Giới tính", df["Gender"].unique(), default=df["Gender"].unique())
diet_type = st.sidebar.multiselect("Chế độ ăn", df["diet_type"].unique(), default=df["diet_type"].unique())
workout_type = st.sidebar.multiselect("Loại bài tập", df["Workout_Type"].unique(), default=df["Workout_Type"].unique())

filtered_df = df[
    (df["Gender"].isin(gender)) &
    (df["diet_type"].isin(diet_type)) &
    (df["Workout_Type"].isin(workout_type))
]

# === Biểu đồ ===
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 Calories đốt cháy theo độ tuổi")

    # Làm tròn tuổi thành số nguyên
    filtered_df["Age"] = filtered_df["Age"].round(0).astype(int)

    chart1 = (
        alt.Chart(filtered_df)
        .mark_bar(color="#4C78A8")
        .encode(
            x=alt.X("Age:O", title="Tuổi", axis=alt.Axis(labelAngle=0)),  # 0° = không xoay
            y=alt.Y("Calories_Burned:Q", title="Calories Burned"),
            tooltip=["Age", "Calories_Burned"]
        )
        .properties(height=350)
    )
    st.altair_chart(chart1, use_container_width=True)

with col2:
    st.subheader("⚖️ Mối tương quan giữa BMI và Calories Burned")
    chart2 = alt.Chart(filtered_df).mark_circle(size=100).encode(
        x=alt.X("BMI:Q", title="BMI"),
        y=alt.Y("Calories_Burned:Q", title="Calories Burned"),
        color="Gender:N",
        tooltip=["Age", "Gender", "BMI", "Calories_Burned"]
    ).interactive().properties(height=350)
    st.altair_chart(chart2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("💪 Phân bố loại bài tập")
    workout_counts = filtered_df["Workout_Type"].value_counts().reset_index()
    workout_counts.columns = ["Workout_Type", "Count"]
    chart3 = alt.Chart(workout_counts).mark_arc(innerRadius=60).encode(
        theta="Count:Q",
        color="Workout_Type:N",
        tooltip=["Workout_Type", "Count"]
    ).properties(height=400)
    st.altair_chart(chart3, use_container_width=True)

with col4:
    st.subheader("🥦 Phân bố chế độ ăn")
    diet_counts = filtered_df["diet_type"].value_counts().reset_index()
    diet_counts.columns = ["diet_type", "Count"]
    chart4 = alt.Chart(diet_counts).mark_arc(innerRadius=60).encode(
        theta="Count:Q",
        color="diet_type:N",
        tooltip=["diet_type", "Count"]
    ).properties(height=400)
    st.altair_chart(chart4, use_container_width=True)

# === Nút hành động ===
st.markdown("---")

# 🔹   nút "Xuất báo cáo"
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📊 Xuất báo cáo",
    data=csv,
    file_name=f"bao_cao_dinh_duong_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
    mime="text/csv",
)