FROM python:3.7

WORKDIR /app

COPY . .

RUN pip install flask requests

EXPOSE 8080

CMD ["python", "frontend_app.py"]