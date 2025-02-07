from discord.ext.commands import Context
from app.feature.simple.use_case.convert_to_fxtwitter_url_action import ConvertToFxTwitterFailed, ConvertToFxTwitterUrlAction

class FxController:
    def __init__(self, action: ConvertToFxTwitterUrlAction):
        self.action = action

    async def convert_to_fx_twitter_url(
        self,
        ctx: Context,
        url: str
    ) -> None:
        try:
            response = self.action.execute(url=url)

            # 変換したURLを送信
            await ctx.send(content=f"{response} (by {ctx.author.mention})")
        except ConvertToFxTwitterFailed:
            # URLの変換に失敗した場合はエラーメッセージを送信
            await ctx.send(content=f"{ctx.author.mention} URLの変換に失敗しました。")