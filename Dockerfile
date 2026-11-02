# Use official lightweight Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_ENV=production

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application codebase
COPY . .

# Create directory for SQLite instance storage
RUN mkdir -p /app/instance

# Create a non-root user for container security
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Expose port for the application
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/ || exit 1

# Production WSGI command with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--access-logfile", "-", "--error-logfile", "-", "wsgi:app"]
