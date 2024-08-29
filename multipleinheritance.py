class Theory:
    def get_theory_marks(self):
        print("this is thoeory marks")


class Sessional:
    def get_sessional_marks(self):
        print("this is sessional marks")

class Result(Theory,Sessional):
    pass

r=Result()
r.get_theory_marks()
r.get_sessional_marks()