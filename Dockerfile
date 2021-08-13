FROM python:latest
WORKDIR /workdir
COPY . .
RUN pip install \
    . \
    "black==21.6b" \
    "codecov==2.1.1" \
    "flake8==3.9.2" \
    "mutmut==2.1.0" \
    "pandas==1.3.0" \
    "pylint==2.9.0" \
    "pytest-cov==2.12.0" \
    "pytest==6.2.0" \
    "rope==0.19.0" \
    "typer==0.3.2" \
    tabulate
RUN curl -fsSL https://git.io/shellspec | sh -s -- --yes
ENV PATH="/root/.local/lib/shellspec:/workdir/src:$PATH"
RUN shellspec --init
