from abc import ABCMeta, abstractmethod

from app.feature.task.domain.entity.task import Task
from app.feature.task.domain.value_object.personal_task_id import PersonalTaskId
from app.shared.domain.value_object.discord_user_id import DiscordUserId


class TaskRepository(metaclass=ABCMeta):
    """タスクのリポジトリインターフェース"""

    @abstractmethod
    def find_by_personal_task_id(
        self,
        discord_user_id: DiscordUserId,
        personal_task_id: PersonalTaskId
    ) -> Task:
        """個人タスクIDからタスクを取得する"""


    @abstractmethod
    def save(self, task: Task) -> None:
        """タスクを保存する"""


    @abstractmethod
    def delete(self, task: Task) -> None:
        """タスクを削除する"""