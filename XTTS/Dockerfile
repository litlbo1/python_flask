FROM python:3.9
WORKDIR /main
COPY requirements.txt /main
RUN python -m pip install -r requirements.txt

COPY . /main
EXPOSE 5000

CMD ["python", "main.py"]