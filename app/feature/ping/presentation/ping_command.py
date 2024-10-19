from app.feature.ping.presentation.controller.ping_controller import PingController
from app.feature.ping.use_case import ping_action
from app.feature.ping.use_case.ping_action import PingAction
from discord.ext import commands

def register_ping_command(bot: commands.Bot) -> None:
    """Pingコマンドを登録します"""
    
    # Pingコマンドに対応するコントローラーを作成
    ping_action = PingAction()
    ping_controller = PingController(ping_action=ping_action)

    @bot.command(name="ping")
    async def ping_command(ctx: commands.Context) -> None:
        await ping_controller.execute(ctx=ctx)