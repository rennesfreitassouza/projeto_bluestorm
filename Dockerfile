# syntax=docker/dockerfile:1
FROM python:3.10.7-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN git clone https://github.com/rennesfreitassouza/projeto_bluestorm.git
WORKDIR /projeto_bluestorm
RUN pip install -r requirements.txt
ENV FLASK_APP=bluestorm_api

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
