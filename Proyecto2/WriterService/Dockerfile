
# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

ADD main.py  /
ADD data  /
CMD ["python3","main.py"]

# Para crear la imagen : docker build . -t writerservice 


#docker run writerservice

#docker run --interactive --tty --volume=${PWD}/data:/aha writerservice

