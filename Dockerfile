# Use official lightweight Python image.
FROM python:3.9-slim

# Set working directory.
WORKDIR /app

# Copy local code to the container image.
COPY . .

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Run the streamlit app on container startup.
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
