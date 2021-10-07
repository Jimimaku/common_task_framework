FROM python:3.9
WORKDIR /workdir
COPY . .
# mutmut is pinned to version 2.1.0 because v2.2.0 does not work with ShellSpec
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
RUN curl \
    --fail \
    --location https://git.io/shellspec \
    --show-error \
    --silent \
    | sh -s -- --yes
ENV PATH="/root/.local/lib/shellspec:/workdir/src:$PATH"
RUN shellspec --init
