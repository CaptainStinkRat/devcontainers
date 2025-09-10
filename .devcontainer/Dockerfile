FROM ubuntu:noble
RUN apt-get update && apt-get install -y sudo
RUN apt-get fish
RUN apt-get update && apt-get install -y \
     ca-certificates \
     curl \
     gnupg \
     lsb-release
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null
RUN apt-get update -y && \
    apt-get install gh -y

RUN echo "ubuntu ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/ubuntu

# Switch to the non-root user.
USER ubuntu
ENTRYPOINT ["bash"]
