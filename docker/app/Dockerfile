FROM python:3.13-slim

# mysqlclientのインストール
RUN apt-get update && apt-get install -y default-libmysqlclient-dev

# requirements.txtをコピー
COPY ./requirements.txt /app/requirements.txt

# envをコピー
COPY ./docker.env /app/.env

# pythonのパッケージをインストール
RUN pip install --no-cache-dir -r /app/requirements.txt

# ワーキングディレクトリを指定
WORKDIR /app

# discord botの実行
CMD ["python", "-m", "app.main"]

