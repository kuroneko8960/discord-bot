from datetime import datetime, timezone

def get_now():
    """現在日時を取得する"""
    return datetime.now(tz=timezone.utc)