FROM python:3.10

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py" ]