FROM python:3.11-slim
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends     ffmpeg build-essential git && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements-gradio.txt /app/requirements-gradio.txt
RUN pip install --upgrade pip
RUN pip install -r requirements-gradio.txt
COPY . /app
EXPOSE 7860
CMD ["python", "app_gradio.py"]
