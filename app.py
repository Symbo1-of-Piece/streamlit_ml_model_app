import streamlit as st
from model.model import ImageCaptioningModel
from utils.photo_loader import load_image
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
            background-color: #80e0a7;  /* Зеленовато-голубой фон */
            border-radius: 15px;  
            padding: 20px;
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.2);  
            color: #343a40;
            margin: 10px 0;
            font-family: 'Arial', sans-serif;  
        }
        .caption-text {
            font-weight: bold;
            font-size: 1.6rem;  /* Larger text for the "Description:" label */
            color: #1e2a47;  /* Dark blue for the label */
        }
        .image-container {
            display: flex;
            justify-content: center;
            max-width: 300px;
            align-items: center;
        }
        .gif-container {
            max-width: 300px;  /* Control GIF width */
            margin: auto;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    st.title("🖼️ Image Captioning App")

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

    if uploaded_file is not None:
        image = load_image(uploaded_file)
        image_width = image.width 
        image_height = image.height  

        gif_width = image_width // 2
        gif_height = image_height // 2

        gif_placeholder = st.empty()
        gif_placeholder.image("assets/thinking.gif", caption="Processing...", use_container_width=False, width=gif_width)

        text_placeholder = st.empty()
        text_placeholder.markdown("### Generating the image caption...")

        # Generate the caption
        with st.spinner('Please wait...'):
            time.sleep(2) 
            captions = captioning_model.predict_step([uploaded_file])

        gif_placeholder.empty() 
        text_placeholder.empty() 

        st.markdown("<br>", unsafe_allow_html=True)
        st.image(image, caption="Uploaded Image", width=500)

        st.markdown("<br>", unsafe_allow_html=True)
        for caption in captions:
            st.markdown(f'<div class="caption"><span class="caption-text">Description:</span> {caption}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    captioning_model = ImageCaptioningModel()
    main()
