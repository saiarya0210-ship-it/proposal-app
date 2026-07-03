import streamlit as st

st.title("❤️ Will You Be My Girlfriend? ❤️")
st.write("From: Sai Arya")

col1, col2 = st.columns(2)

with col1:
    if st.button("Yes ❤️"):
        st.balloons()
        st.success("🥰 Yay! You said YES! ❤️")
        st.write("💖 Thank you! You made my day!")

with col2:
    if st.button("No 💔"):
        st.snow()
        st.error("😢 Oh no! You said NO.")
        st.write("💔 Maybe someday you'll change your mind. 😊")


