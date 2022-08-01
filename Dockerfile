FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /portal_app

COPY ./requirements.txt /portal_app

RUN pip install -r requirements.txt
RUN python -m pip install --upgrade pip

COPY . .

#EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]