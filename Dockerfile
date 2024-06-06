FROM python:3.10-buster

RUN useradd -m -u 1000 user

USER user

COPY --chown=user . /app/commandr-api-local

WORKDIR /app/commandr-api-local

# COPY . .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
