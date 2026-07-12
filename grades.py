<<<<<<< HEAD
def letter_grade(score):
    if not (0 <= score <= 100):
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
=======
def letter_grade(score):
    if not (0 <= score <= 100):
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
>>>>>>> d4414a2c461874530b59813feee4314417927fc9
