# 🧠 CNN Image Classification API (FastAPI)

A lightweight and efficient image classification API using **FastAPI** and **ResNet18** (from TorchVision). This API allows you to classify images via direct file upload or Base64 string input and can return either the predicted **class index** or a dummy-annotated image with bounding boxes.

---

## 🚀 Features

- 🔁 Accepts both **image file uploads** and **Base64-encoded images**
- 🔢 Returns **class index** (no label)
- 🖼️ Returns **annotated image** with placeholder bounding boxes
- 📑 Interactive documentation with **Swagger UI**
- 🧪 Easy to test via **Postman** or **cURL**
- 🐳 Fully containerized with **Docker**

---


## ⚙️ Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/yourusername/CNN-api.git
cd CNN-api
````

### 📦 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

### 📥 3. Install Requirements

```bash
pip install -r requirements.txt
```

### ▶️ 4. Run the API

```bash
uvicorn app.main:app --reload
```

> Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
> Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🐳 Docker Deployment

### 🛠️ Build the Docker Image

```bash
docker build -t cnn-api .
```

### 🚀 Run the Container

```bash
docker run -p 8000:8000 cnn-api
```

> Access the API at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Postman or Swagger Testing

### 🔹 `/predict_file` – POST (Image File)

* **Body Type:** `multipart/form-data`
* **Key:** `file`
* **Returns:** JSON with class index
* ✅ Example:

  ```json
  { "predicted_class_index": 282 }
  ```

### 🔹 `/predict_base64` – POST (Base64 String)

* **Content-Type:** `application/json`
* **Body:**

  ```json
  {
    "img_base64": "<base64_string_here>"
  }
  ```
* **Returns:** JSON with class index

### 🔹 `/detect-image` – POST (Image File)

* **Body Type:** `multipart/form-data`
* **Key:** `file`
* **Returns:** PNG image with **dummy purple bounding boxes**

---

## 🖼️ Example Base64 Usage (cURL)

```bash
curl -X POST http://localhost:8000/predict_base64 \
-H "Content-Type: application/json" \
-d "{\"img_base64\": \"<your_base64_string>\"}"
```

---
