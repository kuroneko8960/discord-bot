# Discord Bot (ChenBot v2)

身内向けのDiscord Botのリポジトリです。

コードの閲覧は自由ですが、利用する際はMIT Licenseに準拠します。

## Feature

- :white_check_mark: 実装済み
  - `!ping`
  - `!godfield` - ゴッドフィールドのURLを取得
  - `!yahtzee [room-name]` - ヨットゲームのURLを取得
- :wrench: 実装予定
  - TODO管理
  - タイマー
  - ダイスロール

## インストール

> [!NOTE]
> python 3.13.0以降が実行できる環境が必要になります。

1. このリポジトリをClone
2. 仮想環境を作成
```
python -m venv env
```
3. パッケージをインストール
```
pip install -r requirements.txt
```
4. `.env.example` をコピー
```
cp .env.example .env
```
5. `.env`の中にDiscord BotのTokenを入力
```.env
DISCORD_BOT_TOKEN=<enter your discord bot token>
```

## 実行

```
python -m app.main
```

> [!TIP]
> デーモン化は行ってないので必要の場合は別途、自身で対応してください。

## テストの実行

```
pytest
```

## Git hookの登録について

push時にpytestが実行できるように、pre-commitを導入しています。

以下のコマンドでGit hookの登録ができます

```bash
pre-commit install -t pre-push
```

## Dockerによる実行

Dockerコンテナを利用してbotを立ち上げることができます。

### 事前準備

1. `.env.example` をコピー
```sh
cp .env.example docker.env
```
2. `docker.env` の DISCORD_BOT_TOKEN の値を書き換え
3. ビルドを行う
```sh
docker compose -f ./docker/docker-compose.yaml build
```

> [!NOTE]
> ./docker以下のファイル や requirements.txt、または docker.env を変更した場合は、
> 再度ビルドを行う必要があります。

### Dockerコンテナの実行

```sh
docker compose -f ./docker/docker-compose.yaml up -d
```

