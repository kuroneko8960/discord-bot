from app.feature.simple.domain.x_post_meta import XPostMeta
from app.shared.use_case.action_base import ActionBase

class ConvertToFxTwitterUrlAction(ActionBase):
    def execute(self, url: str) -> str:
        """FxTwitterのURLに変換する"""
        # URLからx.comの投稿情報に変換する
        try:
            x_post_meta = XPostMeta.from_url(url)
        except ValueError:
            raise ConvertToFxTwitterFailed()

        # x.comの投稿情報からFxTwitterのURLに変換する
        fx_twitter_url = f"https://fxtwitter.com/{x_post_meta.username}/status/{x_post_meta.post_id}"  

        return fx_twitter_url


class ConvertToFxTwitterFailed(Exception):
    pass