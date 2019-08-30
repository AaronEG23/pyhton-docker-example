FROM python:alpine3.7

ADD httpserver.py /
ADD index.html /
ADD common.js /
ADD form.js /
ADD passiveRate.js /

EXPOSE 5001

CMD [ "python", "./httpserver.py" ]

