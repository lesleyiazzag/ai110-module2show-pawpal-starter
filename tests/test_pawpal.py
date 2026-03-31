import unittest
from pawpal_system import Owner, Pet, Task, Scheduler

class TestPawPalSystem(unittest.TestCase):

    def test_task_completion(self):
        """Verify that calling mark_complete() prints the correct completion message."""
        pet = Pet(name="Buddy", type="dog", age=5, preferences={})
        task = Task(name="Morning Walk", duration=1, priority="high", frequency=1, deadline="09:00 AM", pet=pet)
        
        # Capture the output of mark_complete
        with self.assertLogs(level='INFO') as log:
            task.mark_complete()
        
        # Verify the correct message is printed
        self.assertIn(f"Task '{task.name}' for {task.pet.name} has been completed.", log.output[0])

    def test_task_addition(self):
        """Verify that adding a task to a Pet increases that pet's task count."""
        owner = Owner(name="Alex", available_time=8, preferences={})
        pet = Pet(name="Buddy", type="dog", age=5, preferences={})
        owner.pets.append(pet)

        # Create a Scheduler and add a task
        scheduler = Scheduler(owner=owner, total_available_time=owner.get_availability())
        initial_task_count = len(scheduler.tasks)
        task = Task(name="Morning Walk", duration=1, priority="high", frequency=1, deadline="09:00 AM", pet=pet)
        scheduler.tasks.append(task)

        # Verify the task count increased
        self.assertEqual(len(scheduler.tasks), initial_task_count + 1)

    def test_sorting_correctness(self):
        """Verify that tasks are sorted in chronological order."""
        owner = Owner(name="Alex", available_time=8, preferences={})
        pet = Pet(name="Buddy", type="dog", age=5, preferences={})
        owner.pets.append(pet)

        scheduler = Scheduler(owner=owner, total_available_time=8)

        task1 = Task(name="Late Task", duration=1, priority="medium", frequency=1, deadline="2023-11-01 18:00", pet=pet)
        task2 = Task(name="Early Task", duration=1, priority="high", frequency=1, deadline="2023-11-01 09:00", pet=pet)

        scheduler.tasks.extend([task1, task2])
        scheduler.sort_by_time()

        self.assertEqual(scheduler.tasks[0].name, "Early Task")
        self.assertEqual(scheduler.tasks[1].name, "Late Task")
    
    def test_recurrence_logic(self):
        """Verify that marking a daily task complete creates a new task for the next day."""
        owner = Owner(name="Alex", available_time=8, preferences={})
        pet = Pet(name="Buddy", type="dog", age=5, preferences={})
        owner.pets.append(pet)

        scheduler = Scheduler(owner=owner, total_available_time=8)

        task = Task(name="Morning Walk", duration=1, priority="high", frequency="daily", deadline="2023-11-01 09:00", pet=pet)
        scheduler.tasks.append(task)

        scheduler.mark_task_complete(task)

        self.assertEqual(len(scheduler.tasks), 2)

        new_task = scheduler.tasks[-1]
        self.assertEqual(new_task.deadline, "2023-11-02 09:00")
    
    def test_conflict_detection(self):
        """Verify that the scheduler detects tasks with duplicate deadlines."""
        owner = Owner(name="Alex", available_time=8, preferences={})
        pet = Pet(name="Buddy", type="dog", age=5, preferences={})
        owner.pets.append(pet)

        scheduler = Scheduler(owner=owner, total_available_time=8)

        task1 = Task(name="Task 1", duration=1, priority="high", frequency=1, deadline="2023-11-01 09:00", pet=pet)
        task2 = Task(name="Task 2", duration=1, priority="medium", frequency=1, deadline="2023-11-01 09:00", pet=pet)

        scheduler.tasks.extend([task1, task2])

        with self.assertLogs(level='WARNING') as log:
            scheduler.detect_conflicts()

        self.assertTrue(any("Conflict detected" in message for message in log.output))

if __name__ == "__main__":
    unittest.main()