"""一次性触发器"""

from typing import Optional
from vxsched.event import vxTrigger


class vxOnceTrigger(vxTrigger):
    """一次性触发器

    trigger_dt: 触发时间

    """

    __slots__ = ("_last_trigger_dt", "_end_dt")

    def __init__(self, trigger_dt):
        super().__init__()
        self._end_dt = trigger_dt

    def get_next_trigger_dt(self) -> Optional[float]:
        return None if self._last_trigger_dt else self._end_dt
