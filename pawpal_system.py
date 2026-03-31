from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Pet:
    name: str
    type: str
    age: int
    preferences: Dict[str, str]

    def update_info(self):
        pass

    def get_summary(self):
        pass


@dataclass
class Owner:
    name: str
    available_time: int
    preferences: Dict[str, str]

    def update_preferences(self):
        pass

    def get_availability(self):
        pass


@dataclass
class Task:
    name: str
    duration: int
    priority: str
    frequency: int
    deadline: str

    def update_task(self):
        pass

    def mark_complete(self):
        pass

    def get_details(self):
        pass


class Scheduler:
    def __init__(self, total_available_time: int):
        self.tasks: List[Task] = []
        self.total_available_time: int = total_available_time
        self.scheduled_plan: List[Task] = []

    def generate_plan(self):
        pass

    def sort_tasks_by_priority(self):
        pass

    def adjust_for_constraints(self):
        pass

    def get_daily_plan(self):
        pass