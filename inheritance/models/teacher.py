from inheritance.models.person import Person

class Teacher(Person):

    def __init__(self):
        super().__init__()
        self.subject = None