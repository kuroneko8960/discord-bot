from typing import Optional

from discord.ext import commands

from app.feature.simple.presentation.controller import yahtzee_controller
from app.feature.simple.presentation.controller.godfield_controller import GodfieldController
from app.feature.simple.presentation.controller.yahtzee_controller import YahtzeeController
from app.feature.simple.use_case.get_godfield_url_action import GetGodfieldUrlAction
from app.feature.simple.use_case.get_yahtzee_url_action import GetYahtzeeUrlAction
from app.shared.infrastructure.service.build_in_base64_service import BuildInBase64Service
from app.shared.infrastructure.service.system_env_service import SystemEnvService


def register_simple_commands(bot: commands.Bot):
    """シンプルなコマンドを登録します"""

    # services
    env_service = SystemEnvService()
    base64_service = BuildInBase64Service()

    # godfieldコントローラー
    get_godfield_url_action = GetGodfieldUrlAction(env_service=env_service)
    godfield_controller = GodfieldController(get_godfield_url_action=get_godfield_url_action)

    # `!godfield [passphrase]`
    @bot.command(name="godfield")
    async def godfield_command(ctx: commands.Context, passphrase: Optional[str] = None) -> None:
        await godfield_controller.get(ctx=ctx, passphrase=passphrase)

    # yahtzeeコントローラー
    get_yahtzee_url_action = GetYahtzeeUrlAction(
        env_service=env_service,
        base64_service=base64_service
    )
    yahtzee_controller = YahtzeeController(
        get_action=get_yahtzee_url_action
    )

    # `!yahtzee [room-name]`
    @bot.command(name="yahtzee")
    async def yahtzee_command(ctx: commands.Context, room_name: Optional[str] = None) -> None:
        await yahtzee_controller.get(ctx=ctx, room_name=room_name)