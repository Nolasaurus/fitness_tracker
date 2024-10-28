# backend.py
def main():
    ex_1 = create_exercise(400, 5, 8, ex_name="squat")
    ex_2 = create_exercise(185, 5, 5, ex_name='bbell rows')
    exercises = [ex_1, ex_2]

    workout = create_workout("test_workout", exercises)
    print(workout)
    print()

    for name in workout.keys():
        print(name)
        print(workout[name])


def create_exercise(weight:int, reps:int, sets:int, ex_name: str = "unnamed"):
    try: 
        ex_name = str(ex_name)
    except:
        print('Exercise Name must be a string (e.g. "Bench Press", "AaBbCc123", ...')

    try:
        assert(isinstance(weight, int) and isinstance(reps, int) and isinstance(sets, int))
        exercise = {
            "exercise_name": ex_name,
            "expanded": {set_number+1:(weight, reps) for set_number in range(sets)}
        }
    except AssertionError:
        print('Weights, Reps, and Sets must be integer values')

    return exercise


def create_workout(workout_name: str, exercises:list):
    try:
        workout_name = str(workout_name)
        assert(isinstance(workout_name, str))
    except:
        print('Workout must have a name and it must be a string (e.g. "MADCOW", "abc123", ...)')

    workout = {}
    
    for i, ex in enumerate(exercises):
        exercise_name = str(i) if ex['exercise_name'] == "unnamed" else ex['exercise_name']
        workout[exercise_name] = ex['expanded']    

    return workout


def add_exercise(workout, exercise):
    ex_name = exercise['exercise_name']
    assert ex_name.notin(workout.keys()), "Exercise with same name already exists"
    workout[ex_name] = exercise['expanded']
    
    return workout


if __name__ == '__main__':
    main()