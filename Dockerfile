FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app

RUN git clone https://gitlab.com/MichelJuillard/repec_pubdb.git
RUN cd repec_pubdb && python3 -m venv venv && . venv/bin/activate && pip install flask && python3 setup.py install

COPY ./app /app
COPY ./app/local_config.py /app/repec_pubdb/pubdb
