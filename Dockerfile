FROM python:3.8

WORKDIR /

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD python s3-sys.py