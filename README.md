# **Streamlit ML Model App**

## **Description**
This application uses a machine learning model to generate a brief text description of image content.  
You can upload an image in **JPEG, PNG, or JPG** format into the designated field or select a file from your browser for processing.

**[Try the application online](https://appmlmodelapp-sappc9msvslzhtwkvfwdnk.streamlit.app/)**

---

## **Demo**
Link to the app:  
[Streamlit ML Model App](https://appmlmodelapp-sappc9msvslzhtwkvfwdnk.streamlit.app/)

![image](https://github.com/user-attachments/assets/60284779-3cec-436a-880c-e1473c240142)


---

## **Features**
- Upload images from the file system.
- Generate a brief text description of the image using an ML model.
- Supported image formats: **JPEG, PNG, JPG**.

---

## **Installation**

### 1. **Clone the repository**
```bash
git clone https://github.com/Symbo1-of-Piece/streamlit_ml_model_app.git
cd streamlit_ml_model_app
```

### 2. **Install dependencies**
Make sure Python 3.8 or newer is installed. Then run:  
```bash
pip install -r requirements.txt
```

### 3. **Run the application**
Run the app locally:  
```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## **Usage**
1. Visit the application link or run it locally.
2. Upload an image in **JPEG, PNG, or JPG** format into the designated field.
3. Wait for the description to be generated.
4. Download or save the result (if this option is available).

---

## **Project Structure**
```plaintext
streamlit_ml_model_app/
├── assets/                     # Supporting files (GIFs, images)
├── model/                      # Model logic
│   ├── image_to_text.py        # Image-to-text conversion module
│   └── model.py                # Core ML model
├── tests/                      # Application tests
│   ├── test_app.py             # Interface tests
├── utils/                      # Utility modules
│   ├── photo_loader.py         # Image loader
│   └── __init__.py             # Module initialization
├── app.py                      # Main Streamlit application file
├── config.py                   # Configuration file
├── requirements.txt            # Dependency list
└── README.md                   # Documentation
```

---

## **Sample Data**
The application expects images to be uploaded in one of the following formats:  
- `JPEG`
- `PNG`
- `JPG`

---

## **Known Issues**
- File upload size may be limited by server configuration.
- Low performance when processing large images.

---
