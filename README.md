# ML Zoomcamp Week 5 – Lead Scoring Docker App

This repository contains the homework for **ML Zoomcamp Week 5**, including a **FastAPI lead scoring app** packaged with **Docker**.

---

## **Project Overview**

* Predict the **conversion probability of leads** using a pre-trained ML pipeline.
* The app is served via **FastAPI** and can be run locally using Docker.
* Includes:

  * `pipeline_v1.bin` – pre-trained model pipeline
  * `predict_api.py` – FastAPI application
  * `Dockerfile` – Docker configuration
  * Supporting scripts for testing predictions

---

## **Running the App Locally**

### **Prerequisites**

* [Docker](https://andrewlock.net/installing-docker-desktop-for-windows/) installed on your machine.

### **Steps**

1. Open your terminal / PowerShell and navigate to the project folder.
2. Build the Docker image (optional if image is already built):

```bash
docker build -t homework-deploy .
```

3. Run the Docker container:

```bash
docker run -p 8000:8000 homework-deploy
```

4. Open your browser and access the FastAPI app:

```
http://localhost:8000/
```

* Swagger docs (API interface): `http://localhost:8000/docs`
* Redoc docs: `http://localhost:8000/redoc`

---

## **Making Predictions**

* Use the `/predict` endpoint to get the **conversion probability** for a lead.
* Example JSON payload:

```json
{
  "lead_source": "organic_search",
  "number_of_courses_viewed": 4,
  "annual_income": 80304.0
}
```

* You can test it via:

  * **Swagger UI** (`/docs`)
  * **Python requests**:

```python
import requests

url = "http://localhost:8000/predict"
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url, json=client)
print(response.json())
```

---

## **Notes**

* The app listens on **`0.0.0.0:8000` inside the container**.
* On your host machine, always access it via **`http://localhost:8000/`**.

---

## **Author**

* GitHub: [Kavengi00](https://github.com/Kavengi00)
* ML Zoomcamp Week 5 Homework

---

