FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
        python3-bs4 \
        python3-urllib3 \
        python3-flask \
	python3-flask-cors \
        git

RUN git clone https://github.com/chauncyca/eldritchify.git
COPY start.sh /start.sh
CMD [ "/start.sh" ]
