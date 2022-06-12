class Student:
    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_student_info(self):
        '''This is an instance method, it's value will be change according to the instance '''
        return f"Myself {self.name},I am {self.age} years old."

    @classmethod
    def get_school_name(cls):
        '''This is a class method, it will not depend on any object, for all objects it's value will be same '''
        return cls.school

    @staticmethod
    def get_arbitrary_info():
        "This is static method, it will not depend on class or instance"
        return "Lorem ipsum dolor sit amet."


s1 = Student("John Doe", 25)
s2 = Student("Erin Pierce", 30)
print(Student.get_school_name())
print(Student.get_arbitrary_info())
print(s1.get_student_info())
print(s2.get_student_info())
