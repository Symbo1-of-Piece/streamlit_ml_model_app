from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
from model.model import ImageCaptioningModel

app = FastAPI(
    title="Image Captioning API",
    description="API для генерации текстовых описаний изображений",
    version="1.0.0"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Инициализация модели при старте приложения
caption_model = ImageCaptioningModel()

@app.post("/predict", summary="Генерация подписи к изображению")
async def predict_image(file: UploadFile = File(...)):
    """
    Принимает изображение и возвращает текстовое описание его содержимого.
    
    Поддерживаемые форматы: JPEG, PNG
    """
    try:
        # Проверка формата файла
        if file.content_type not in ["image/jpeg", "image/png"]:
            raise HTTPException(status_code=400, detail="Неподдерживаемый формат изображения. Используйте JPEG или PNG")

        # Чтение и обработка изображения
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        # Конвертация в RGB если необходимо
        if image.mode != "RGB":
            image = image.convert("RGB")

        # Сохранение во временный файл для обработки моделью
        temp_path = "temp_image.jpg"
        image.save(temp_path)

        # Генерация описания
        captions = caption_model.predict_step([temp_path])
        
        return JSONResponse({
            "status": "success",
            "description": captions[0],
            "image_size": f"{image.width}x{image.height}"
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)