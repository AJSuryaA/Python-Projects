import random
import string

CHOICES = {
    "upper_case": list(string.ascii_uppercase),
    "lower_case": list(string.ascii_lowercase),
    "special_char": list(string.punctuation),
    "numbers": list(string.digits)
}

class Generate_password:
    def __init__(self):
        self.password= []
        self.final_password= None

    def generate(self):
        self.password= [random.sample(CHOICES[x],random.choice([2,3,4])) for x in CHOICES]
        self.password = [char for sublist in self.password for char in sublist]
        random.shuffle(self.password)
        self.final_password = "".join(self.password)
        return self.final_password


passw = Generate_password()
passw.generate()