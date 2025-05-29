FROM python:3.9

WORKDIR /app 

COPY requirements.txt . 
RUN pip install -r requirements.txt

RUN python -m pip install --upgrade setuptools

RUN addgroup --gid 1234 teste && \
    adduser --uid 1234 --ingroup teste --shell /bin/false --no-create-home --disabled-password thullyo
USER thullyo

COPY . . 
CMD ["python", "app.py"]

EXPOSE 5000