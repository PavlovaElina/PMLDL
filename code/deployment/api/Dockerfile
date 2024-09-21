# Dockerfile for FastAPI API
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the trained model and API code
COPY model.pkl /app/models/
COPY api.py /app/api.py
COPY requirements.txt /app/requirements.txt
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
