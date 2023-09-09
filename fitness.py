class Exercise:
    def __init__(self, name, target_repetitions):
        self.name = name
        self.target_repetitions = target_repetitions
        self.current_repetitions = 0

    def increment_repetitions(self):
        self.current_repetitions += 1

class VirtualFitnessCoach:
    def __init__(self):
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def track_repetitions(self, exercise_name):
        for exercise in self.exercises:
            if exercise.name == exercise_name:
                exercise.increment_repetitions()
                print(f"Repetitions for {exercise.name}: {exercise.current_repetitions}/{exercise.target_repetitions}")
                break
        else:
            print(f"{exercise_name} not found.")

# Create a virtual fitness coach instance
coach = VirtualFitnessCoach()

# Create exercises and add them to the coach
push_ups = Exercise("Push-ups", 10)
coach.add_exercise(push_ups)

squats = Exercise("Squats", 15)
coach.add_exercise(squats)

# Track repetitions
coach.track_repetitions("Push-ups")  # Output: Repetitions for Push-ups: 1/10
coach.track_repetitions("Squats")    # Output: Repetitions for Squats: 1/15
coach.track_repetitions("Sit-ups")   # Output: Sit-ups not found.
