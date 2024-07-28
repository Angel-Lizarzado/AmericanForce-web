FROM python:3.11-slim
WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m venv $VIRTUAL_ENV

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD reflex run --env prod --backend-only