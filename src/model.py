from torchvision import models, transforms
from PIL import Image
import torch
import io
import base64

# Load model once globally
model = models.resnet18(pretrained=True)
model.eval()

# Define preprocessing
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

def predict_image(img: Image.Image) -> int:
    img_t = preprocess(img).unsqueeze(0)
    with torch.no_grad():
        output = model(img_t)
    probs = torch.nn.functional.softmax(output[0], dim=0)
    _, class_id = torch.max(probs, 0)
    return class_id.item()

def decode_base64_image(b64_string: str) -> Image.Image:
    img_bytes = base64.b64decode(b64_string)
    return Image.open(io.BytesIO(img_bytes)).convert("RGB")
