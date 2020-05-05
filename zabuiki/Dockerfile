# pull official base image
FROM python:3.6.9-alpine as builder

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create directory for the zabuiki user
RUN mkdir -p /home/zabuiki

# create the zabuiki user
RUN addgroup -S zabuiki && adduser -S zabuiki -G zabuiki

# create the appropriate directories
ENV HOME=/home/zabuiki
ENV APP_HOME=/home/zabuiki/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apk update \
    && apk add  \
    build-base \
    python3-dev \
    # wget dependency
    openssl \
    # dev dependencies
    git \
    bash \
    sudo \
    # Pillow dependencies
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev \
    postgresql-dev \
    gcc \
    python3-dev \ 
    musl-dev \
    libpq \
    libxml2-dev \
    libxslt-dev

RUN pip install --upgrade pip

# copy entrypoint-prod.sh
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

RUN chown -R zabuiki:zabuiki $APP_HOME


RUN pip install -r requirements.txt --no-cache-dir
RUN chown -R zabuiki:zabuiki /usr/local/
# chown all the files to the zabuiki user


# change to the zabuiki user
USER zabuiki

# run entrypoint.prod.sh
ENTRYPOINT ["/home/zabuiki/web/entrypoint.sh"]