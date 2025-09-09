import streamlit as st
from datetime import datetime

st.title("🌸 Nhật ký nhỏ cho Em 🌸")

st.write("Trả lời vài câu hỏi nhé:")

q1 = st.text_area("Hôm nay em thấy thế nào?")
q2 = st.text_area("Gấu có thể giúp được gì cho em?")
q3 = st.text_area("Em có muốn ăn gì không?")
q4 = st.text_area("Em yêu Gấu nhé?")

if st.button("💌 Gửi bạn nhỏ"):
    note_content = f"""
Ngày {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Hôm nay em thấy thế nào? {q1}
Gấu có thể giúp được gì cho em? {q2}
Em có muốn ăn gì không? {q3}
Em yêu Gấu nhé? {q4}

---------------------------------
"""

    # Ghi vào file local
    with open("Note.txt", "a", encoding="utf-8") as f:
        f.write(note_content)

    st.success("🌞 Chúc em một ngày mới thật tốt lành!\n\n💖 Gấu yêu em nhiều lắm! 💖")

# --- Khu vực chỉ cho bạn ---
st.markdown("---")
st.subheader("🔒 Khu vực quản trị (chỉ dành cho Gấu)")

password = st.text_input("Nhập mật khẩu để tải Note.txt", type="password")

if password == "gauyeuem":  # đổi mật khẩu ở đây
    with open("Note.txt", "r", encoding="utf-8") as f:
        st.download_button(
            label="📥 Tải Note.txt về",
            data=f,
            file_name="Note.txt",
            mime="text/plain"
        )
