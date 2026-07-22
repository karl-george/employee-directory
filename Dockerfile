FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY app/requirements.txt ./requirements.txt

RUN pip install \
    --no-cache-dir \
    --disable-pip-version-check \
    --requirement requirements.txt

COPY app/ ./

RUN addgroup --system employee-app \
    && adduser \
        --system \
        --ingroup employee-app \
        --home /app \
        employee-app \
    && chown -R employee-app:employee-app /app

USER employee-app

EXPOSE 8000

CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "app:app"]