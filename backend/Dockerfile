FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app
RUN apt update && apt install -y netcat

COPY . /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .
ENTRYPOINT [ "./entrypoint.sh" ]
