from typing import Optional
from app.feature.simple.presentation.controller.godfield_controller import GodfieldController
from app.feature.simple.use_case.get_godfield_url_action import GetGodfieldUrlAction
from app.shared.infrastructure.service.system_env_service import SystemEnvService
from discord.ext import commands

def register_simple_commands(bot: commands.Bot):
    """シンプルなコマンドを登録します"""

    # services
    env_service = SystemEnvService()

    # godfieldコマンド
    get_godfield_url_action = GetGodfieldUrlAction(env_service=env_service)
    godfield_controller = GodfieldController(get_godfield_url_action=get_godfield_url_action)

    # `!godfield [passphrase]`
    @bot.command(name="godfield")
    async def godfield_command(ctx: commands.Context, passphrase: Optional[str] = None) -> None:
        await godfield_controller.get(ctx=ctx, passphrase=passphrase)