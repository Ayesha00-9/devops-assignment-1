# Use a specific Python version
FROM python:3.13.5-slim

# Set working directory
WORKDIR /app

# Copy requirements file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create a non-root user and give ownership
RUN useradd -m appuser && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose application port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]