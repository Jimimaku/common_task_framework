FROM python:latest
WORKDIR /workdir
COPY . .
RUN pip install \
    . \
    "mutmut==2.1.0" \
    black \
    codecov \
    flake8 \
    pandas \
    pylint \
    pytest \
    pytest-cov \
    rope \
    tabulate \
    typer
RUN curl -fsSL https://git.io/shellspec | sh -s -- --yes
ENV PATH="/root/.local/lib/shellspec:/workdir/src:$PATH"
RUN shellspec --init
