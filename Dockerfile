FROM python:latest
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    flake8 \
    mutmut \
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
