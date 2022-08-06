FROM python:latest

WORKDIR /work
COPY ./ /work

RUN pip install -r requirements.txt
CMD ["python", "convert.py"]
