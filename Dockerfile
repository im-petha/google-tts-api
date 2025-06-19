FROM python:3.10-slim-buster

WORKDIR /google-tts


COPY . .
# Install ffmpeg and Python packages
RUN pip install flask requests
# apt-get install -y ffmpeg && \

# apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 5000

CMD ["python", "main.py"]
