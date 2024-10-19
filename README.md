# Discord Bot (ChenBot v2)

身内向けのDiscord Botのリポジトリです。

コードの閲覧は自由ですが、利用する際はMIT Licenseに準拠します。

## Feature

- :white_check_mark: 実装済み
  - ping
- :wrench: 実装予定
  -  TODO管理
  - ダイスロール

## インストール

> [!NOTE]
> python 3.11以降が実行できる環境が必要になります。

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
