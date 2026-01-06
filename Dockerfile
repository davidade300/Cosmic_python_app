FROM python:3.14.2-slim-trixie

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /code
COPY *.py /code/
WORKDIR /code
ENV FLASK_APP=src/cosmic_python/flask_app.py FLASK_DEBUG=1 PYTHONUNBUFFERED=1
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
