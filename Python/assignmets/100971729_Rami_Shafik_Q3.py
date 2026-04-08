#Question 3: Encapsulation & Getters/Setters

class Student:
    def __init__(self, name, student_id, _gpa):
        self.name = name
        self.student_id = student_id
        self._gpa = _gpa

    def get_gap(self):
        return self._gpa
    
    def set_gpa(self, new_gpa):
        if new_gpa < 0.0 or new_gpa > 4.0:
            print(f"Invalid GPA!")
        else:
            self._gpa = new_gpa

s = Student("John Doe", "S12345", 3.2)
s.set_gpa(3.8)
s.set_gpa(4.5)
print(s.get_gap())