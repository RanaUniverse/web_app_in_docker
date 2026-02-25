# This is the Dockerfile here i will write the instructions 
# to build the image to run the applicaion's containers

FROM python:3.14-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:0.10.6 /uv /uvx /bin/

ARG APP_DIR=/rana
WORKDIR ${APP_DIR}

COPY .python-version pyproject.toml uv.lock ./

RUN uv sync

COPY . ./

EXPOSE 8001

CMD [ "uv", "run", "gunicorn", "main:app" ]