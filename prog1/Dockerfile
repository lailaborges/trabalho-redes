# prog1/Dockerfile

FROM python:3.12

WORKDIR /app

COPY prog1.py .

RUN pip install numpy

CMD ["python", "prog1.py", "m=5", "n=3", "f=1", "port=5001"]