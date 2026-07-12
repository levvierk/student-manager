<<<<<<< HEAD
from grades import letter_grade


def test_letter_grade_A():
    assert letter_grade(95) == "A"


def test_letter_grade_boundaries():
       assert letter_grade(90) == "A"
       assert letter_grade(85) == "B"
       assert letter_grade(75) == "C"
       assert letter_grade(65) == "D"      
       assert letter_grade(59) == "F"



def test_letter_grade_F():
=======
from grades import letter_grade


def test_letter_grade_A():
    assert letter_grade(95) == "A"


def test_letter_grade_boundaries():
       assert letter_grade(90) == "A"
       assert letter_grade(85) == "B"
       assert letter_grade(75) == "C"
       assert letter_grade(65) == "D"      
       assert letter_grade(59) == "F"



def test_letter_grade_F():
>>>>>>> d4414a2c461874530b59813feee4314417927fc9
    assert letter_grade(0) == "F"