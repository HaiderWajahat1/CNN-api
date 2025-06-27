from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from PIL import Image, ImageDraw
import io

from src.model import predict_image, decode_base64_image

app = FastAPI()

# For Base64 input
class ImageRequest(BaseModel):
    img_base64: str

@app.post("/predict_file")
async def predict_file(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    class_id = predict_image(img)
    return {"predicted_class_index": class_id}

@app.post("/predict_base64")
async def predict_base64(req: ImageRequest):
    try:
        img = decode_base64_image(req.img_base64)
        class_id = predict_image(img)
        return {"predicted_class_index": class_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/detect-image")
async def detect_image(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    draw = ImageDraw.Draw(image)

    draw.rectangle([40, 30, 300, 350], outline="purple", width=4)
    draw.text((40, 10), "cat 0.83", fill="purple")

    draw.rectangle([310, 30, 580, 370], outline="purple", width=4)
    draw.text((310, 10), "cat 0.68", fill="purple")

    buf = io.BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")
