import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

# Initialize session state for Owner, Pets, and Tasks
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan", available_time=8, preferences={})
if "pets" not in st.session_state:
    st.session_state.pets = []
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add a Pet
st.subheader("Add a Pet")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
pet_age = st.number_input("Pet age", min_value=0, max_value=30, value=3)

if st.button("Add Pet"):
    new_pet = Pet(name=pet_name, type=species, age=pet_age, preferences={})
    st.session_state.pets.append(new_pet)
    st.success(f"Added pet: {new_pet.name} ({new_pet.type}, Age: {new_pet.age})")

if st.session_state.pets:
    st.write("Current pets:")
    for pet in st.session_state.pets:
        st.write(f"- {pet.get_summary()}")

st.divider()

# Add a Task
st.subheader("Add a Task")
col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

selected_pet = st.selectbox(
    "Assign to Pet", [pet.name for pet in st.session_state.pets] if st.session_state.pets else []
)

if st.button("Add Task"):
    if not st.session_state.pets:
        st.error("Please add a pet first.")
    else:
        # Find the selected pet object
        pet = next(p for p in st.session_state.pets if p.name == selected_pet)
        new_task = Task(
            name=task_title,
            duration=duration,
            priority=priority,
            frequency=1,
            deadline="N/A",
            pet=pet,
        )
        st.session_state.tasks.append(new_task)
        st.success(f"Added task: {new_task.name} for {new_task.pet.name}")

if st.session_state.tasks:
    st.write("Current tasks:")
    for task in st.session_state.tasks:
        st.write(f"- {task.get_details()}")

st.divider()

# Build Schedule
st.subheader("Build Schedule")
st.caption("This button calls your scheduling logic.")

if st.button("Generate schedule"):
    if not st.session_state.tasks:
        st.warning("No tasks to schedule. Add tasks first.")
    else:
        scheduler = Scheduler(owner=st.session_state.owner, total_available_time=8)
        scheduler.tasks.extend(st.session_state.tasks)
        scheduler.sort_by_time()
        scheduler.generate_plan()
        scheduler.detect_conflicts()
        st.warning("Conflict detection ran. Check logs for details if any conflicts exist.")
        plan = scheduler.get_daily_plan()
        if plan:
            st.success("Schedule generated successfully!")

            st.subheader("Today's Schedule")

            st.table(plan)
        else:
            st.warning("No tasks could be scheduled within the available time.")