FROM python:3.9

WORKDIR /app
EXPOSE 8501

COPY app.py ./
COPY model_prediction.py ./
COPY requirements.txt ./
COPY prepare_csv.py ./
COPY run.sh ./
COPY AutogluonModel/ ./AutogluonModel/

RUN pip install -r requirements.txt

CMD ["./run.sh"]
