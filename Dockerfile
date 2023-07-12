FROM python:3.10

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY main.py .

EXPOSE 8704

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8704" ]
