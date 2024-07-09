import streamlit as st
import qrcode
from PIL import Image
import io

def generate_qr_code(input_string):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_string)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    # PIL.Image.Image をバイト型に変換
    img_byte_arr = io.BytesIO()
    qr_img.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

def main():
    st.title("文字列をQRコードに変換するアプリ")

    input_text = st.text_input("QRコードに変換したい文字列を入力してください")
    if st.button("生成"):
        if input_text:
            qr_img_bytes = generate_qr_code(input_text)
            st.image(qr_img_bytes, caption=f"QRコード: {input_text}", use_column_width=True)
        else:
            st.warning("文字列を入力してください。")

if __name__ == "__main__":
    main()
