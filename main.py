from pawpal_system import Owner, Pet, Task, Scheduler

# Create an Owner
owner = Owner(name="Alex", available_time=8, preferences={"task_priority": "high"})

# Create two Pets
pet1 = Pet(name="Buddy", type="dog", age=5, preferences={"walk_frequency": "daily"})
pet2 = Pet(name="Mittens", type="cat", age=3, preferences={"feeding_schedule": "twice a day"})

# Add pets to the owner
owner.pets.extend([pet1, pet2])

# Create Tasks for the pets (two tasks with the same deadline)
task1 = Task(name="Morning Walk", duration=1, priority="high", frequency="daily", deadline="2023-11-01 09:00", pet=pet1)
task2 = Task(name="Feed Mittens", duration=0.5, priority="medium", frequency="daily", deadline="2023-11-01 09:00", pet=pet2)
task3 = Task(name="Groom Buddy", duration=2, priority="low", frequency="weekly", deadline="2023-11-01 17:00", pet=pet1)
task4 = Task(name="Evening Walk", duration=1, priority="high", frequency="daily", deadline="2023-11-01 18:00", pet=pet1)

# Create a Scheduler
scheduler = Scheduler(owner=owner, total_available_time=owner.get_availability())

# Add tasks to the scheduler
scheduler.tasks.extend([task1, task2, task3, task4])

# Sort tasks by time
scheduler.sort_by_time()

# Print sorted tasks
print("Tasks sorted by time:")
for task in scheduler.tasks:
    print(f"- {task.name} for {task.pet.name} (Deadline: {task.deadline})")

# Generate the daily plan (this will detect conflicts)
scheduler.generate_plan()

# Print "Today's Schedule"
print("\nToday's Schedule:")
for task_details in scheduler.get_daily_plan():
    print(f"- {task_details['name']} for {task_details['pet']} (Duration: {task_details['duration']} hours, Priority: {task_details['priority']})")