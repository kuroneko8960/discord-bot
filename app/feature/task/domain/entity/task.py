from datetime import datetime, timezone, timedelta
from typing import Optional

from app.feature.task.domain.error import TaskAlreadyCompletedError, TaskAlreadyStartedError
from app.feature.task.domain.value_object.task_id import TaskId
from app.feature.task.domain.value_object.personal_task_id import PersonalTaskId
from app.feature.task.domain.value_object.task_content import TaskContent
from app.feature.task.domain.value_object.task_status import TaskStatus
from app.shared.domain.value_object.discord_user_id import DiscordUserId
from app.shared.util.datetime import get_now


class Task:
    """エンティティ: タスク"""

    def __init__(
        self,
        id: TaskId,
        discord_user_id: DiscordUserId,
        personal_task_id: PersonalTaskId,
        content: TaskContent,
        status: TaskStatus,
        started_at: Optional[datetime] = None,
        completed_at: Optional[datetime] = None,
        temporary_deleted_at: Optional[datetime] = None,
        created_at: datetime = get_now(),
        updated_at: datetime = get_now(),
    ):
        self.id = id
        self.discord_user_id = discord_user_id
        self.personal_task_id = personal_task_id
        self.content = content
        self.status = status
        self.started_at = started_at
        self.completed_at = completed_at
        self.temporary_deleted_at = temporary_deleted_at
        self.created_at = created_at
        self.updated_at = updated_at


    def start(self, started_at: datetime = get_now()) -> None:
        """タスクを開始する"""

        if self.status == TaskStatus.DOING:
            raise TaskAlreadyStartedError()

        self.status = TaskStatus.DOING
        self.started_at = started_at


    def complete(self, completed_at: datetime = get_now()) -> None:
        """タスクを完了する"""

        if self.status == TaskStatus.DONE:
            raise TaskAlreadyCompletedError()

        if self.status == TaskStatus.WAITING:
            self.started_at = completed_at

        self.status = TaskStatus.DONE
        self.completed_at = completed_at

    
    def cancel(self) -> None:
        """タスクをキャンセルする"""

        self.status = TaskStatus.WAITING
        self.started_at = None
        self.completed_at = None


    def edit(self, content: TaskContent) -> None:
        """タスクの内容を編集する"""

        self.content = content


    def delete(self, deleted_at: datetime = get_now()) -> None:
        """タスクを一時削除する"""

        self.temporary_deleted_at = deleted_at
    

    def is_temporary_deleted(self) -> bool:
        """タスクが一時削除されているかどうか"""

        if self.temporary_deleted_at is None:
            # 一時削除されていない
            return False

        if self.temporary_deleted_at + timedelta(minutes=1) < get_now():
            # タスクが一時削除されてから 1分経過してたら削除として扱わない
            return False

        return True
