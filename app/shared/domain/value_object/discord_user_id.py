from dataclasses import dataclass

@dataclass(frozen=True)
class DiscordUserId:
    """値オブジェクト: DiscordユーザーID"""
    value: str

    def __init__(self, value: str) -> None:
        if not value:
            raise ValueError('DiscordユーザーIDは必ず指定してください')

        # DiscordユーザーIDの形式チェック
        if not value.isnumeric():
            raise ValueError('DiscordユーザーIDは数値である必要があります')
        if len(value) < 17 or len(value) > 19:
            raise ValueError('DiscordユーザーIDは17桁以上19桁以下である必要があります')


        object.__setattr__(self, 'value', value)
