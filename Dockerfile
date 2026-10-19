FROM python:3.12-alpine
WORKDIR /app
COPY app/app.py .
RUN python -c "import http.server"
EXPOSE 8000
CMD ["python", "app.py"]
