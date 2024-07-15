import streamlit as st
import qrcode
import io

st.set_page_config(
    page_title="qrcode-lbd",
    page_icon=":dog:",
    layout="wide",
    initial_sidebar_state="expanded",
)

if 'history' not in st.session_state:
    st.session_state['history'] = []

if 'history' not in st.session_state:
    st.session_state.history = []

def generate_qr_code(input_text, qr_version, box_size, border, 
                     fill_color, back_color, error_correction):
    qr = qrcode.QRCode(
        version=qr_version,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr.add_data(input_text)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img_byte_arr = io.BytesIO()
    qr_img.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

@st.experimental_dialog("Result")
def display_qr_code(input_text, qr_version, box_size, border, fill_color, back_color, error_correction):
    if input_text:
        qr_img_bytes = generate_qr_code(input_text, qr_version, box_size, border, fill_color, back_color, error_correction)
        st.image(qr_img_bytes, caption=f"input_text: {input_text}", use_column_width=True)
        st.success("QR code generated successfully.")
    else:
        st.error("Please input text and apply.")

def main():
    qrcode_url = "more info: https://pypi.org/project/qrcode/"

    with st.sidebar:
        st.title("Settings")
        st.info("Config generator settings.Here is default settings.")
        color1, color2 = st.columns(2)
        qr_version = st.number_input("QR version", value=10, min_value=1, max_value=40, step=1, 
                                         help=qrcode_url)
        error_correction_string = st.selectbox("Error correction", 
                                                   ["ERROR_CORRECT_L", "ERROR_CORRECT_M", 
                                                    "ERROR_CORRECT_Q",  "ERROR_CORRECT_H"], help=qrcode_url)
        box_size = st.slider("Box size", value=20, min_value=1, step=1, help=qrcode_url)
        border = st.slider("Border", value=4, min_value=0, step=1, help=qrcode_url)
        color1, color2 = st.columns(2)
        fill_color = color1.color_picker("Fill color", value="#000000", help=qrcode_url)
        back_color = color2.color_picker("Back color", value="#FFFFFF", help=qrcode_url)

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

    st.title("QR code generator")
        
    generate_tab, history_tab = st.tabs(["Generate", "History"])

    col1, col2 = generate_tab.columns([4, 1], vertical_alignment="bottom")
    input_text = col1.text_input("Input", placeholder="Input text here", 
                                 help=qrcode_url)
    col2.button("popup", on_click=display_qr_code, args=(input_text, qr_version, box_size, border, fill_color, back_color, error_correction))

    if input_text != "":
        qr_img_bytes = generate_qr_code(input_text, qr_version, box_size, border, fill_color, back_color, error_correction)
        generate_tab.image(qr_img_bytes, caption=f"input_text: {input_text}")
        generate_tab.success("QR code preview successfully.")
        st.session_state.history.append(input_text)
        st.toast("generate success and added to history")
        st.balloons()

    with history_tab.expander("Session History (Delete by closing the browser)"):
        for text in st.session_state.history:
            history_tab.write(text)

if __name__ == "__main__":
    main()
