from dataclasses import dataclass, field
from typing import List, Dict
import logging

@dataclass
class Pet:
    name: str
    type: str
    age: int
    preferences: Dict[str, str]

    def update_info(self, name: str = None, type: str = None, age: int = None, preferences: Dict[str, str] = None):
        """Update pet's information."""
        if name:
            self.name = name
        if type:
            self.type = type
        if age:
            self.age = age
        if preferences:
            self.preferences.update(preferences)

    def get_summary(self):
        return f"{self.name} ({self.type}), Age: {self.age}, Preferences: {self.preferences}"


@dataclass
class Owner:
    name: str
    available_time: int
    preferences: Dict[str, str]
    pets: List[Pet] = field(default_factory=list)

    def update_preferences(self, new_preferences: Dict[str, str]):
        """Update owner's preferences."""
        self.preferences.update(new_preferences)

    def get_availability(self):
        """Return the owner's available time."""
        return self.available_time


@dataclass
class Task:
    name: str
    duration: int
    priority: str
    frequency: int
    deadline: str
    pet: Pet

    def __post_init__(self):
        if self.priority not in ["high", "medium", "low"]:
            raise ValueError("Invalid priority level")
        if self.duration <= 0:
            raise ValueError("Duration must be greater than 0")
    
    def update_task(self, name: str = None, duration: int = None, priority: str = None, frequency: int = None, deadline: str = None):
        """Update task details."""
        if name:
            self.name = name
        if duration:
            if duration <= 0:
                raise ValueError("Duration must be greater than 0")
            self.duration = duration
        if priority:
            if priority not in ["high", "medium", "low"]:
                raise ValueError("Invalid priority level")
            self.priority = priority
        if frequency:
            self.frequency = frequency
        if deadline:
            self.deadline = deadline

    def mark_complete(self):
        """Mark the task as complete."""
        logging.info(f"Task '{self.name}' for {self.pet.name} has been completed.")

    def get_details(self):
        """Return task details."""
        return {
            "name": self.name,
            "duration": self.duration,
            "priority": self.priority,
            "frequency": self.frequency,
            "deadline": self.deadline,
            "pet": self.pet.name
        }

class Scheduler:
    def __init__(self, owner: Owner, total_available_time: int):
        """Initialize the Scheduler with an owner and total available time."""
        self.owner = owner
        self.tasks: List[Task] = []
        self.total_available_time: int = total_available_time
        self.scheduled_plan: List[Task] = []

    def generate_plan(self):
        """Generate a daily plan by prioritizing tasks and adjusting for constraints."""
        # Example logic to prioritize tasks with deadlines
        self.tasks.sort(key=lambda task: task.deadline)
        self.adjust_for_constraints()

    def sort_tasks_by_priority(self):
        self.tasks.sort(key=lambda task: task.priority, reverse=True)

    def adjust_for_constraints(self):
        time_remaining = self.total_available_time
        adjusted_plan = []
        for task in self.tasks:
            if task.duration <= time_remaining:
                adjusted_plan.append(task)
                time_remaining -= task.duration
        self.scheduled_plan = adjusted_plan

    def get_daily_plan(self):
        """Return the daily plan as a list of task details."""
        return [task.get_details() for task in self.scheduled_plan]