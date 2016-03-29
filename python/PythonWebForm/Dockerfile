FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN pip install co3-24.0.1.tar.gz
#ENV resilient /Users/stevebade/Data/co3-api/python/co3
#WORKDIR /code/co3/
#RUN python setup.py install
EXPOSE 8000
CMD python /code/runserver.py 0.0.0.0:8000
