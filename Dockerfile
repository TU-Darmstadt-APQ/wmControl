FROM alpine:3.18 as builder

ARG BUILD_CORES
ARG GIT_REPOSITORY

# Install the build dependencies
RUN COLOUR='\e[1;93m' && \
  test -n "$GIT_REPOSITORY" || (echo "\e[0;31mGIT_REPOSITORY  not set.\e[0m" && false) && \
  echo -e "${COLOUR}Installing build dependencies...\e[0m" && \
  apk --no-cache add --virtual=build-dependencies \
    build-base \
    py3-pip \
    git && \
  echo -e "${COLOUR}Done.\e[0m"

# Define the python virtual environment. This will be copied to the worker later
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD https://api.github.com/repos/${GIT_REPOSITORY}/git/refs/heads/master version.json
RUN COLOUR='\e[1;93m' && \
  echo -e "${COLOUR}Installing HighFinesse SCPI server...\e[0m" && \
  git clone https://github.com/${GIT_REPOSITORY} app && \
  pip install -r /app/requirements.txt && \
  echo -e "${COLOUR}Done.\e[0m"

FROM alpine:3.18
LABEL maintainer="Patrick Baus <patrick.baus@physik.tu-darmstadt.de>"
LABEL description="HighFinesse Wavemeter SCPI deamon."

ARG WORKER_USER_ID=5555

# Upgrade installed packages,
# add a user called `worker`
# Then install Python dependency
RUN apk --no-cache upgrade && \
    addgroup -g ${WORKER_USER_ID} worker && \
    adduser -D -u ${WORKER_USER_ID} -G worker worker && \
    apk --no-cache add python3

COPY --from=builder /opt/venv /opt/venv

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

COPY --from=builder /app /app
RUN chown -R worker:worker /app

USER worker

CMD python3 -OO -u /app/server.py
