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

if __name__ == "__main__":
    unittest.main()