# FROM python:3.10-slim-buster

# WORKDIR /google-tts


# COPY . .
# # Install ffmpeg and Python packages
# RUN pip install flask requests
# # apt-get install -y ffmpeg && \

# # apt-get clean && rm -rf /var/lib/apt/lists/*

# EXPOSE 5000

# CMD ["python", "main.py"]

FROM python:3.10-slim-buster

# Set working directory
WORKDIR /google-tts

# Copy requirement file first (better for Docker caching)
COPY requirement.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of the app
COPY . .

# Expose port
EXPOSE 5000

# Start with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--access-logfile", "-", "main:app"]
