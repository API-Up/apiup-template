# This Build argument will be setted automatically. Don't change it.
ARG APIKIT_IMAGE
FROM ${APIKIT_IMAGE}

# Implicit by base image
# WORKDIR /app
# COPY requirements-app.txt .
# RUN env/bin/pip install -r requirements-app.txt --no-cache-dir
# COPY ./apps* /app/apps
