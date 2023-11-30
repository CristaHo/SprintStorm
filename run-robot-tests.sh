#!/bin/bash

# käynnistetään Flask-palvelin taustalle
./start.sh &

# odetetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:8000/ping)" != "200" ]];
  do sleep 1;
done

# suoritetaan testit
poetry run robot tests

status=$?

# pysäytetään Flask-palvelin portissa 5001
kill $(lsof -t -i:8000)

exit $status
