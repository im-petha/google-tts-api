FROM python:3.10-slim-buster


WORKDIR /google-tts

COPY . .

RUN pip install flask requests

EXPOSE 5000

CMD ["python", "main.py"]
