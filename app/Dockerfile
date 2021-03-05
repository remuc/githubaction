FROM python:3-alpine

WORKDIR /app

COPY requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["ash","-c","python apy.py"]

# docker build -t pym .
# docker run -it -p 8000:8000 pym
