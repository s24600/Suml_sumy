FROM python:3.9

WORKDIR /app
EXPOSE 8501

COPY app.py ./
COPY model_prediction.py ./
COPY requirements.txt ./
COPY model_train.py ./
COPY prepare_csv.py ./
COPY run.sh ./

RUN pip install -r requirements.txt

CMD ["./run.sh"]
