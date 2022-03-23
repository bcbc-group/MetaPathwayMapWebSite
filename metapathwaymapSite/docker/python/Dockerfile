From python:3.8.9

COPY ./metapathwaymapSite metapathwaymapSite

WORKDIR /metapathwaymapSite

COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt

WORKDIR /metapathwaymapSite

RUN python manage.py migrate

CMD ["./runserver.sh"]
