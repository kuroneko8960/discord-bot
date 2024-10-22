from abc import ABCMeta, abstractmethod
from typing import Optional, List

from app.feature.task.domain.entity.task import Task
from app.feature.task.domain.value_object.task_content import TaskContent
from app.feature.task.domain.value_object.task_status import TaskStatus
from app.feature.task.domain.value_object.personal_task_id import PersonalTaskId
from app.shared.domain.value_object.discord_user_id import DiscordUserId

class TaskQueryService(metaclass=ABCMeta):
    """タスクを検索するサービスのインターフェース"""

    @abstractmethod
    def fetch(
        self,
        status: Optional[TaskStatus] = None,
        content: Optional[TaskContent] = None,
        page: int = 1, 
        per_page: int = 10
    ) -> List[Task]:
        """
        タスクを検索する

        Args:
            status (Optional[str]): ステータス
            content (Optional[str]): タスク内容
            page (int): ページ数
            per_page (int): 1ページあたりの表示数
        Returns:
            List[Task]: タスク一覧
        """

        pass

    @abstractmethod
    def next_personal_task_id(self, discord_user_id: DiscordUserId) -> PersonalTaskId:
        """
        次の個人タスクIDを取得します
        
        Args:
            discord_user_id (DiscordUserId): DiscordユーザID
        Returns:
            PersonalTaskId: 個人タスクID
        """
        pass