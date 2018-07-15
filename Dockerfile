FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./ .

RUN pip install pipenv

RUN pipenv install --system --deploy --three

CMD ["python3", "main.py"]