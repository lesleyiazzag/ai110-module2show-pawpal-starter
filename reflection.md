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

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff the scheduler makes is that it only checks for exact time matches when detecting conflicts between tasks, rather than considering overlapping durations. This means that if two tasks for the same or different pets overlap in time but do not start at the exact same moment, the conflict will not be detected. For example, a task scheduled from 09:00 to 10:00 and another from 09:30 to 10:30 would not trigger a conflict warning. This simplifies the conflict detection logic and reduces computational complexity, but it may lead to scheduling issues in scenarios where overlapping durations are significant.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
