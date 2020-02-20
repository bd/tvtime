FROM python:3.7
RUN mkdir /app
WORKDIR /app
ENV PYTHONPATH /app
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD ./tvtime /app/
EXPOSE 8000