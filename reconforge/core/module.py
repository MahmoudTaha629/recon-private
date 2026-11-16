from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class Context:
    """Everything a module needs. Filled with real objects in Phase 1."""
    scan_id: int
    config: Any = None
    db: Any = None
    http: Any = None     # every request must go through here (scope + rate limit)
    dns: Any = None
    ports: Any = None
    scope: Any = None
    events: Any = None


class BaseModule(ABC):
    name: str = ""
    depends_on: list[str] = []

    @abstractmethod
    async def run(self, ctx: Context) -> None:
        """Read inputs from ctx.db, do the work, write results back to ctx.db."""
