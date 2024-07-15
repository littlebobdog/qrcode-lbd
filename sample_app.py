import streamlit as st
import qrcode
import io

def generate_qr_code(input_string, qr_version, box_size, border, 
                     fill_color, back_color, error_correction):
    qr = qrcode.QRCode(
        version=qr_version,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr.add_data(input_string)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img_byte_arr = io.BytesIO()
    qr_img.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

@st.experimental_dialog("QR Code Generator")
def display_qr_code(input_string, qr_version, box_size, border, 
                    fill_color, back_color, error_correction):
    if input_string:
        qr_img_bytes = generate_qr_code(input_string, qr_version, box_size, border, 
                                        fill_color, back_color, error_correction)
        st.image(qr_img_bytes, caption=f"input_text: {input_string}", use_column_width=True)
    else:
        st.warning("Please input text and apply.")

def main():
    qrcode_url = "more info: https://pypi.org/project/qrcode/"

    st.sidebar.title("menu")
    color1, color2 = st.sidebar.columns(2)
    qr_version = st.sidebar.number_input("QR version", value=10, min_value=1, max_value=40, step=1, 
                                         help=qrcode_url)
    error_correction_string = st.sidebar.selectbox("Error correction", 
                                                   ["ERROR_CORRECT_L", "ERROR_CORRECT_M", 
                                                    "ERROR_CORRECT_Q",  "ERROR_CORRECT_H"], help=qrcode_url)
    box_size = st.sidebar.number_input("Box size", value=20, min_value=1, step=1, help=qrcode_url)
    border = st.sidebar.number_input("Border", value=4, min_value=0, step=1, help=qrcode_url)
    color1, color2 = st.sidebar.columns(2)
    fill_color = color1.color_picker("Fill color", value="#000000", help=qrcode_url)
    back_color = color2.color_picker("Back color", value="#FFFFFF", help=qrcode_url)

    st.title("QR code generator")
    col1, col2 = st.columns([4, 1], vertical_alignment="bottom")
    input_text = col1.text_input("Input", placeholder="Apply to preview", 
                                 help=qrcode_url)
    show_dialog_button = col2.button("show dialog")

    error_correction = qrcode.constants.ERROR_CORRECT_M
    match error_correction_string:
        case "ERROR_CORRECT_L":
            error_correction = qrcode.constants.ERROR_CORRECT_L
        case "ERROR_CORRECT_M":
            error_correction = qrcode.constants.ERROR_CORRECT_M
        case "ERROR_CORRECT_Q":
            error_correction = qrcode.constants.ERROR_CORRECT_Q
        case "ERROR_CORRECT_H":
            error_correction = qrcode.constants.ERROR_CORRECT_H

    if show_dialog_button:
        display_qr_code(input_text, qr_version, box_size, border, fill_color, back_color, error_correction)
    elif input_text != "":
        qr_img_bytes = generate_qr_code(input_text, qr_version, box_size, border, fill_color, back_color, error_correction)
        st.image(qr_img_bytes, caption=f"input_text: {input_text}", use_column_width=True)

if __name__ == "__main__":
    main()
