ARG PYTHON_VERSION=3.9.11-bullseye 
FROM python:${PYTHON_VERSION} 

FROM python as python-build-stage 
ARG BUILD_ENVIRONMENT=local

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev 

COPY ./requirements . 

RUN pip wheel --wheel-dir /usr/src/app/wheels \ 
    -r ${BUILD_ENVIRONMENT}.txt 

# Stage 2
FROM python as python-run-stage 
ARG BUILD_ENVIRONMENT=local 

ARG APP_HOME=/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# Install dependencies 
RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \ 
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \ 
    && rm -rf /var/lib/apt/lists/* 

COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \ 
    && rm -rf /wheels/


COPY ./docker/local/django/entrypoint /entrypoint
# Entrypoint has unix style line endings. 
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

# Ensure django server is run, and all models collected
COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start


COPY . ${APP_HOME}

# Primary command once container is launched
ENTRYPOINT [ "/entrypoint" ]
