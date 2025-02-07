import re

from pydantic import BaseModel


class XPostMeta(BaseModel, frozen=True):
    username: str
    post_id: str

    @classmethod
    def from_url(cls, url: str) -> 'XPostMeta':
        """URLからユーザ名と投稿IDを取得する"""
        # 例: https://x.com/username/status/12345
        # -> username: username, post_id: 12345

        # 正規表現を使ってURLからユーザ名と投稿IDを取得する
        pattern = r"https:\/\/x\.com\/(?P<username>[^/]+)\/status\/(?P<post_id>[0-9]+)"
        match = re.match(pattern, url)
        if not match:
            raise ValueError("URLが不正です")

        return cls(
            username=match.group("username"),
            post_id=match.group("post_id")
        )