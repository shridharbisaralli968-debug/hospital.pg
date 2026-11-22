FROM python:3.14

WORKDIR /hospital

COPY patient.py .

CMD ["python", "patient.py"]
