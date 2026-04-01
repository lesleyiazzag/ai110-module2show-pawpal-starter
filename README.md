# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

### Smarter Scheduling
The scheduling system was enhanced to better handle real-world pet care needs. Tasks are now sorted by their deadlines using proper datetime parsing, ensuring that time-sensitive tasks are prioritized correctly. The system also detects scheduling conflicts when multiple tasks share the same deadline and logs warnings to highlight these issues.

Additionally, the scheduler accounts for time constraints by selecting tasks that fit within the owner’s available time, creating a feasible daily plan. Support for recurring tasks (daily and weekly) was added, allowing completed tasks to automatically generate future instances. Filtering capabilities were also introduced to view tasks by pet or completion status, making task management more flexible and organized.

### Testing PawPal+
To run the test suite for PawPal+, use the following command:

python -m pytest

The tests verify key system behaviors, including correct task sorting by deadline, proper handling of recurring tasks when marking a task complete, and detection of scheduling conflicts. These tests help ensure that the scheduler behaves as expected under common scenarios.

Confidence Level: ⭐⭐⭐⭐☆ (4/5) — The system is reliable based on the passing tests, with strong coverage of core scheduling functionality. However, additional edge case testing could further improve robustness.


### Features
Task Management: Add and organize pet care tasks with key attributes like duration, priority, and assigned pet.
Time-Based Sorting: Tasks are automatically sorted by deadline using datetime parsing to ensure chronological order.
Conflict Detection: The system checks for overlapping task deadlines and generates warnings to alert the user of scheduling conflicts.
Constraint-Based Scheduling: The scheduler selects tasks that fit within the owner’s available time, prioritizing feasible daily plans.
Priority Handling: Tasks are organized and considered based on priority levels (high, medium, low) to ensure important tasks are addressed first.
Recurring Tasks: Supports daily and weekly task recurrence by automatically generating the next instance when a task is marked complete.
Task Filtering: Tasks can be filtered by pet or completion status to help users manage and view relevant tasks easily.