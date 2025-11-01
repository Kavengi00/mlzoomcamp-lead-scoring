# Start from the prebuilt model image
FROM agrigorev/zoomcamp-model:2025

# Set working directory
WORKDIR /code

# Copy pyproject.toml to install dependencies
COPY pyproject.toml .
COPY pipeline_v1.bin .

# Install Python dependencies
RUN pip install --no-cache-dir fastapi uvicorn pydantic scikit-learn==1.6.1

# Copy your FastAPI script(s)
COPY predict_api.py .

# Expose port
EXPOSE 8000

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "predict_api:app", "--host", "0.0.0.0", "--port", "8000"]
