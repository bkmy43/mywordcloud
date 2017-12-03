FROM python:3-alpine

RUN apk update
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --no-cache --update-cache add gcc python python-dev postgresql-dev musl-dev py-pip build-base libjpeg jpeg-dev openjpeg-dev libxft-dev freetype-dev libpng-dev openblas-dev
RUN apk add git
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install git+git://github.com/amueller/word_cloud.git

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]