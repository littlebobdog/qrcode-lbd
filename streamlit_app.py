# streamlit_app.py

import streamlit as st

# タイトルを表示
st.title("Streamlit Get Started App")

# テキスト入力
name = st.text_input("名前を入力してください")

# スライダー
age = st.slider("年齢を選択してください", 0, 100, 25)

# セレクトボックス
occupation = st.selectbox(
    "職業を選択してください",
    ["学生", "エンジニア", "デザイナー", "その他"]
)

# ボタン
if st.button("送信"):
    # 入力されたデータを表示
    st.write(f"名前: {name}")
    st.write(f"年齢: {age}")
    st.write(f"職業: {occupation}")
