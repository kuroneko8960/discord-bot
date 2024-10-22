class TaskNotStartedError(Exception):
    """タスクがすでに未着手の場合のエラー"""
    pass

class TaskAlreadyStartedError(Exception):
    """タスクがすでに開始されている場合のエラー"""
    pass

class TaskAlreadyCompletedError(Exception):
    """タスクがすでに完了している場合のエラー"""
    pass

class TaskNotFoundError(Exception):
    """タスクが存在しない場合のエラー"""
    pass
