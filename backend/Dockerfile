FROM python:alpine3.7

ADD constant.py /
ADD dataManager.py /
ADD processPasiveRateHTML.py /
ADD resource.py /

ADD testdb /

RUN pip install bs4
RUN pip install urlopen
RUN pip install flask 
RUN pip install flask-cors

EXPOSE 5000

CMD [ "python", "./resource.py" ]

