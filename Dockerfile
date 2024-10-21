# Use the official Python 3.10 slim image as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Update the package index and install system dependencies
# Then clean up the apt cache to reduce image size
RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    libmariadb-dev \
    build-essential \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt /app/
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Set correct permissions for static files
RUN chmod -R 755 /app/staticfiles

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Create a startup script
RUN echo '#!/bin/bash\n\
    nginx\n\
    gunicorn video_manager.wsgi:application --bind 0.0.0.0:8000\n\
    ' > /app/start.sh && chmod +x /app/start.sh

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=video_manager.settings
ENV PYTHONUNBUFFERED=1

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the startup script
CMD ["/app/start.sh"]