import pytest
from app.backend import create_exercise, create_workout

### test CREATE EXERCISE ###
def test_create_exercise_valid_input():
    # Test with valid inputs
    exercise = create_exercise(400, 5, 3, "test_exercise")
    assert exercise == {'exercise_name': 'test_exercise', 'expanded': {1: (400, 5), 2: (400, 5), 3: (400, 5)}}

def test_create_exercise_default_name():
    # Test with default exercise name
    exercise = create_exercise(400, 5, 3)
    assert exercise["exercise_name"] == "unnamed", "Default name test failed."

def test_create_exercise_invalid_name():
    # Test with a non-string name, expecting the name to be converted to string
    exercise = create_exercise(300, 5, 3, 12345)
    assert exercise["exercise_name"] == "12345", "Invalid name handling test failed."

def test_create_exercise_invalid_weight():
    # Test with invalid weight (non-integer), expecting an error message
    with pytest.raises(AssertionError):
        create_exercise("heavy", 5, 3, "test_exercise")
        

def test_create_exercise_invalid_reps():
    # Test with invalid reps (non-integer), expecting an error message
    with pytest.raises(AssertionError):
        create_exercise(300, "many", 3, "test_exercise")

def test_create_exercise_invalid_sets():
    # Test with invalid sets (non-integer), expecting an error message
    with pytest.raises(AssertionError):
        create_exercise(300, 5, "multiple", "test_exercise")


### TEST CREATE WORKOUT ###

def test_create_workout_valid_input():
    # Test with valid inputs
    ex_1 = create_exercise(400, 5, 8, ex_name="squat")
    ex_2 = create_exercise(185, 5, 5, ex_name='bbell rows')
    ex_3 = create_exercise(1500, 6, 12, ex_name='megaGIGA lift3')

    workout = create_workout('test_workout', [ex_1, ex_2, ex_3])

    assert workout  == {'workout_name': 'test_workout', 'squat': {1: (400, 5), 2: (400, 5), 3: (400, 5), 4: (400, 5), 5: (400, 5), 6: (400, 5), 7: (400, 5), 8: (400, 5)}, 'bbell rows': {1: (185, 5), 2: (185, 5), 3: (185, 5), 4: (185, 5), 5: (185, 5)}, 'megaGIGA lift3': {1: (1500, 6), 2: (1500, 6), 3: (1500, 6), 4: (1500, 6), 5: (1500, 6), 6: (1500, 6), 7: (1500, 6), 8: (1500, 6), 9: (1500, 6), 10: (1500, 6), 11: (1500, 6), 12: (1500, 6)}}
