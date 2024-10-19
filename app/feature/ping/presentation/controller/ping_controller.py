from discord.ext.commands.context import Context

from app.feature.ping.use_case.ping_action import PingAction
from app.shared.presentation.controller_base import ControllerBase


class PingController(ControllerBase):
    def __init__(
        self,
        ping_action: PingAction
    ):
        self.ping_action = ping_action

    
    async def execute(self, ctx: Context) -> None:
        message = self.ping_action.execute()

        await ctx.send(content=message)