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
    assert letter_grade(0) == "F"