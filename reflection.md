# PawPal+ Project Reflection

## 1. System Design

Actions a user should be able to perform:
1. A user can input and manage basic information about themselves and their pet, such as the pet’s name, type, and any relevant care preferences.
2. A user can create, edit, and prioritize pet care tasks (such as feeding, walks, medication, or grooming), including specifying details like duration and importance.
3. A user can generate and view a daily care schedule that organizes tasks based on priorities and constraints, along with an explanation of why the schedule was created that way.

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

### a. Initial design

My initial UML design included four main classes: Pet, Owner, Task, and Scheduler. The Pet and Owner classes store basic information and preferences about the user and their pet. The Task class represents individual care activities, including attributes like duration, priority, and deadlines, and handles task-related updates.

The Scheduler class is responsible for managing a list of tasks and generating a daily plan based on priorities and time constraints. It also handles sorting tasks and adjusting the schedule to fit within the owner’s available time.


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

I updated the design to include clearer relationships between classes. I added a list of pets to the Owner class (Owner → pets: List[Pet]) to support managing multiple pets. I also linked each Task to a specific Pet (Task → pet: Pet) so tasks are associated with the correct animal. Finally, I connected the Scheduler to the Owner (Scheduler → owner: Owner) so scheduling decisions can account for the owner’s availability and preferences. These changes make the system more realistic and better structured.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My scheduler considers several constraints, including the owner’s available time, task duration, and task priority. It also accounts for deadlines by sorting tasks chronologically, and it ensures that tasks are only added to the daily plan if they fit within the remaining available time. Additionally, it supports task recurrence, which introduces timing constraints based on when tasks should repeat.

I decided these constraints mattered most because they directly affect whether a schedule is feasible and realistic. Time and duration are the most critical since they determine what can actually fit into a day, while priority ensures that the most important tasks are completed first. Including deadlines and recurrence adds structure and helps the system behave more like a real-world scheduling assistant.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff the scheduler makes is that it only checks for exact time matches when detecting conflicts between tasks, rather than considering overlapping durations. This means that if two tasks for the same or different pets overlap in time but do not start at the exact same moment, the conflict will not be detected. For example, a task scheduled from 09:00 to 10:00 and another from 09:30 to 10:30 would not trigger a conflict warning. This simplifies the conflict detection logic and reduces computational complexity, but it may lead to scheduling issues in scenarios where overlapping durations are significant.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used VS Code Copilot and ChatGPT to support different parts of the project, including designing the system structure, debugging errors, and improving my implementation. Copilot was especially helpful for writing boilerplate code and suggesting method implementations, while ChatGPT helped me reason through errors, refine my design decisions, and understand how different parts of the system should interact.

The most helpful prompts were those that were specific and tied to my actual code, such as asking how to fix a particular error or how to structure a method to meet test requirements.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

There were times when I did not accept AI suggestions as-is. For example, when AI suggested combining scheduling logic inside the Task class, I chose to keep that logic in the Scheduler class instead to maintain a cleaner separation of responsibilities. I evaluated suggestions by comparing them against my system design, project requirements, and test cases to ensure they aligned with the intended architecture.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested sorting correctness to ensure tasks are ordered by deadline, recurrence logic to verify that completing a task correctly creates a new future instance, and conflict detection to check that the system warns when tasks share the same deadline. These tests were important because they validate the core functionality of the scheduler, ensuring it produces reliable and predictable schedules.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am moderately confident (around 4/5) that my scheduler works correctly. The tests cover the main behaviors, including scheduling, recurrence, and conflict detection, but there are still potential edge cases that are not fully tested. If I had more time, I would test overlapping time intervals, invalid input formats, multiple pets with competing constraints, and more complex scheduling scenarios to further improve robustness.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with the overall structure of my system and how the classes interact. Separating responsibilities between Pet, Owner, Task, and Scheduler made the system easier to manage and extend. I also think the scheduling logic and recurrence feature were strong parts of the project.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had another iteration, I would improve the conflict detection system to account for overlapping time ranges instead of only exact matches. I would also enhance the scheduling logic to better prioritize tasks using a more sophisticated algorithm rather than simple sorting. Additionally, I would improve the user interface to make the schedule display more interactive and visually clear.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

One important thing I learned is that designing a system requires careful planning of class responsibilities and relationships before writing code. Working with AI is most effective when I take the role of the lead architect—guiding the structure, evaluating suggestions critically, and ensuring that all components work together cohesively. AI is a powerful tool, but it works best when combined with clear system design and human oversight.