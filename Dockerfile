FROM ubuntu:latest
WORKDIR /workdir
COPY . .
RUN apt update && apt install --yes \
    curl \
    git \
    python3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python
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

RUN curl --location https://github.com/neovim/neovim/releases/download/stable/nvim.appimage --output nvim.appimage && \
    chmod u+x ./nvim.appimage && \
    ./nvim.appimage --appimage-extract && \
    ln -s /workdir/squashfs-root/usr/bin/nvim /usr/bin/vim

