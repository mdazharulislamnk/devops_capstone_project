# Use the official Python image as base
FROM python:3.9-slim

# Create a working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY service/ ./service/

# Create a non-root user and switch to it
RUN useradd --uid 1000 theia && chown -R theia /app
USER theia

# Expose port 8080
EXPOSE 8080

# Run the application using Gunicorn
CMD ["gunicorn", "--bind=0.0.0.0:8080", "--log-level=info", "service:app"]
