#
# Discord Bot Entry Point
#
import os

from app.feature.simple.presentation.simple_command import register_simple_commands
from dotenv import load_dotenv

from app.feature.ping.presentation.ping_command import register_ping_command
from app.shared.presentation.discord_bot import DiscordBotSuite


def main(): 
    # .envファイルを読み込む
    load_dotenv()

    # Bot Tokenを環境変数から取得
    token = os.getenv("DISCORD_BOT_TOKEN")
    if token is None:
        raise Exception("DISCORD_BOT_TOKEN is not set")

    # Botを初期化
    bot_suite = DiscordBotSuite()
    bot = bot_suite.get_bot()

    # コマンド登録
    register_ping_command(bot)
    register_simple_commands(bot)

    # Botを起動
    bot_suite.boot(token)


if __name__ == "__main__":
    main()
