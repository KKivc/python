FROM python:3.12

WORKDIR ./app
COPY healthcheck.py config.json ./
RUN pip install requests
CMD ["python", "healthcheck.py"]