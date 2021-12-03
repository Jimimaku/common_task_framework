FROM ubuntu:latest
USER root
WORKDIR /workdir
COPY . .

# Define variables de entorno
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/root/.cargo/bin:/root/.local/lib/shellspec:/workdir/src:$PATH"
ENV PYTHONIOENCODING=utf-8
ENV QT_QPA_PLATFORM=offscreen
ENV TZ=US/Pacific

# Instala paquetes en el sistema operativo
RUN apt update && apt full-upgrade --yes && apt install --yes \
    cargo \
    curl \
    git \
    neofetch \
    python3-pip \
    tmux
# Usa `python3` como la versión _default_ de Python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Instala modulos con pip
# mutmut is pinned to version 2.1.0 because v2.2.0 does not work with ShellSpec
RUN pip install \
    "mutmut==2.1.0" \
    black \
    cargo \
    codecov \
    flake8 \
    powerline-shell \
    pylint \
    pytest \
    pytest-cov \
    rope
# Instala ShellSpec
RUN curl \
    --fail \
    --location https://git.io/shellspec \
    --show-error \
    --silent \
    | sh -s -- --yes
RUN shellspec --init

# Insatla Vim
RUN cd ${HOME} && \
    curl --location https://github.com/neovim/neovim/releases/download/stable/nvim.appimage --output ${HOME}/nvim.appimage && \
    chmod u+x ${HOME}/nvim.appimage && \
    ${HOME}/nvim.appimage --appimage-extract && \
    ln -s ${HOME}/squashfs-root/usr/bin/nvim /usr/bin/nvim

# Importa archivos de configuración
RUN mkdir --parents ${HOME}/repos && \
    git clone --bare https://github.com/devarops/dotfiles.git ${HOME}/repos/dotfiles.git && \
    git --git-dir=${HOME}/repos/dotfiles.git --work-tree=${HOME} checkout && \
    git --git-dir=${HOME}/repos/dotfiles.git --work-tree=${HOME} config --local status.showUntrackedFiles no

# Install exa: a modern replacement for ls
RUN cargo install exa
