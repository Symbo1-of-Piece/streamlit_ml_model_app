import streamlit as st
import requests
from PIL import Image
import io
import time

def main():
    st.set_page_config(page_title="Image Captioning App", layout="wide")

    st.markdown(
        """
        <style>
        .main {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        .title {
            color: #1e2a47;
            font-family: 'Roboto', sans-serif;
            font-size: 3rem;
            text-align: center;
            margin-bottom: 20px;
        }
        .file-uploader {
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
        }
        .description {
            color: #495057;
            font-size: 1.2rem;
        }
        .caption {
            font-size: 1.6rem;  
            background-color: #80e0a7;
            border-radius: 15px;  
            padding: 20px;
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.2);  
            color: #343a40;
            margin: 10px 0;
            font-family: 'Arial', sans-serif;  
        }
        .caption-text {
            font-weight: bold;
            font-size: 1.6rem;
            color: #1e2a47;
        }
        .image-container {
            display: flex;
            justify-content: center;
            max-width: 300px;
            align-items: center;
        }
        .gif-container {
            max-width: 300px;
            margin: auto;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    st.title("🖼️ Image Captioning App (API Version)")

    API_URL = "http://localhost:8000"
    PREDICT_ENDPOINT = "/predict"

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image_width = image.width 
        image_height = image.height  

        gif_width = image_width // 2
        gif_height = image_height // 2

        gif_placeholder = st.empty()
        gif_placeholder.image("assets/thinking.gif", caption="Processing...", use_container_width=False, width=gif_width)

        text_placeholder = st.empty()
        text_placeholder.markdown("### Generating the image caption...")

        # Отправка изображения в API
        with st.spinner('Please wait...'):
            try:
                files = {"file": uploaded_file.getvalue()}
                response = requests.post(
                    f"{API_URL}{PREDICT_ENDPOINT}",
                    files=files
                )
                
                if response.status_code == 200:
                    result = response.json()
                    caption = result.get("description", "No description generated")
                else:
                    caption = f"API Error: {response.text}"
                
                time.sleep(1)  # Для плавности анимации

            except Exception as e:
                caption = f"Connection Error: {str(e)}"

        gif_placeholder.empty() 
        text_placeholder.empty() 

        st.markdown("<br>", unsafe_allow_html=True)
        st.image(image, caption="Uploaded Image", width=500)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f'<div class="caption"><span class="caption-text">Description:</span> {caption}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()