# prog2/Dockerfile

FROM python:3.12

WORKDIR /app

COPY prog2.py .

RUN pip install numpy

CMD ["python", "prog2.py", "port_on=5001", "port_to=5003"]