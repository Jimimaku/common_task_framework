FROM python:latest
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    flake8 \
    mutmut \
    panda \
    pylint \
    pytest \
    pytest-cov \
    rope \
    typer
RUN curl -fsSL https://git.io/shellspec | sh -s -- --yes
ENV PATH="/root/.local/lib/shellspec:/workdir/src:$PATH"
