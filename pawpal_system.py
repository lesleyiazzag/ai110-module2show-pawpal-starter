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


from datetime import datetime, timedelta

@dataclass
class Task:
    name: str
    duration: int
    priority: str
    frequency: str  # Updated to accept "daily" or "weekly"
    deadline: str  # Format: "YYYY-MM-DD HH:MM"
    pet: Pet

    def __post_init__(self):
        if self.priority not in ["high", "medium", "low"]:
            raise ValueError("Invalid priority level")

        if self.duration <= 0:
            raise ValueError("Duration must be greater than 0")

        # Accept both int and string frequencies
        if isinstance(self.frequency, int):
            if self.frequency <= 0:
                raise ValueError("Frequency must be positive")
        elif isinstance(self.frequency, str):
            if self.frequency not in ["daily", "weekly", "none"]:
                raise ValueError("Invalid frequency level")
        else:
            raise ValueError("Invalid frequency type")

    def mark_complete(self, scheduler):
        """Mark the task as complete and create a new instance if recurring."""
        logging.info(f"Task '{self.name}' for {self.pet.name} has been completed.")
        
        # Check if the task is recurring
        if self.frequency in ["daily", "weekly"]:
            # Parse the current deadline
            current_deadline = datetime.strptime(self.deadline, "%Y-%m-%d %H:%M")
            
            # Calculate the next deadline
            if self.frequency == "daily":
                next_deadline = current_deadline + timedelta(days=1)
            elif self.frequency == "weekly":
                next_deadline = current_deadline + timedelta(weeks=1)
            
            # Create a new task instance with the updated deadline
            new_task = Task(
                name=self.name,
                duration=self.duration,
                priority=self.priority,
                frequency=self.frequency,
                deadline=next_deadline.strftime("%Y-%m-%d %H:%M"),
                pet=self.pet
            )
            
            # Add the new task to the scheduler
            scheduler.tasks.append(new_task)
            logging.info(f"New task '{new_task.name}' created for {new_task.pet.name} with deadline {new_task.deadline}.")

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
        # Detect conflicts before generating the plan
        conflicts = self.detect_conflicts()
        if conflicts:
            logging.warning("Conflicts detected between tasks:")
            for conflict in conflicts:
                logging.warning(f"Conflict: {conflict[0].name} and {conflict[1].name} at {conflict[0].deadline}")

        # Example logic to prioritize tasks with deadlines
        self.tasks.sort(key=lambda task: task.deadline)
        self.adjust_for_constraints()

    def detect_conflicts(self):
        """Detect if two tasks are scheduled at the same time and log a warning."""
        import logging
        logging.basicConfig(level=logging.WARNING)

        for i, task1 in enumerate(self.tasks):
            for j, task2 in enumerate(self.tasks):
                if i < j and task1.deadline == task2.deadline:
                    logging.warning(f"Conflict detected: '{task1.name}' and '{task2.name}' are both scheduled at {task1.deadline}.")

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
    
    from datetime import datetime
    def sort_by_time(self):
        """Sort tasks by their deadline in 'HH:MM' format."""
        self.tasks = sorted(
            self.tasks,
            key=lambda task: datetime.strptime(task.deadline, "%Y-%m-%d %H:%M")
        )
    def filter_tasks(self, completed: bool = None, pet_name: str = None):
        """
        Filter tasks by completion status or pet name.

        :param completed: Filter tasks by their completion status (True/False).
        :param pet_name: Filter tasks by the associated pet's name.
        :return: A list of filtered tasks.
        """
        filtered_tasks = self.tasks
        if completed is not None:
            filtered_tasks = [task for task in filtered_tasks if getattr(task, 'completed', False) == completed]
        if pet_name:
            filtered_tasks = [task for task in filtered_tasks if task.pet.name == pet_name]
        return filtered_tasks
    
    def mark_task_complete(self, task):
        """Mark a task as complete and handle recurring tasks."""
        task.mark_complete()

        if task.frequency in ["daily", "weekly"]:
            from datetime import datetime, timedelta

            current_deadline = datetime.strptime(task.deadline, "%Y-%m-%d %H:%M")

            if task.frequency == "daily":
                next_deadline = current_deadline + timedelta(days=1)
            elif task.frequency == "weekly":
                next_deadline = current_deadline + timedelta(weeks=1)

            new_task = Task(
                name=task.name,
                duration=task.duration,
                priority=task.priority,
                frequency=task.frequency,
                deadline=next_deadline.strftime("%Y-%m-%d %H:%M"),
                pet=task.pet
            )

            self.tasks.append(new_task)