FROM python:3.10
LABEL maintainer "Rhavy Maia Guedes <rhavy.guedes@ifpb.edu.br>"

RUN apt-get update

RUN mkdir /app
WORKDIR /app
COPY . /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=true
ENV FLASK_ENV=development

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# TODO: Analisar essa parte da execução do Flask!
# running Flask as a module
CMD ["sh", "-c", "sleep 5 \ 
    # ! run init only the first time you launch the stack and when the migrations folder do not exist yet
    && flask db init \ 
    # ! To set the revision in the database to the head, without performing any migrations. You can change head to the required change you want.
    # && flask db stamp head \
    && flask db migrate \
    && flask db upgrade \ 
    && python -m flask run --host=0.0.0.0"]