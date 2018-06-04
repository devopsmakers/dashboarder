
FROM python:3

ENV FLASK_APP main.py

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

VOLUME /usr/src/app

EXPOSE 5000

CMD [ "flask", "run", "--reload", "-h", "0.0.0.0" ]
