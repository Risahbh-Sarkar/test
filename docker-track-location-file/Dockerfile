FROM  python:3.9

WORKDIR /docker-track-location-container

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./python-project ./python-project

CMD [ "python", "./python-project/main.py" ]