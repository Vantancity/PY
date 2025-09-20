class People:
    def __init__(self, name = "Roman", work = "Developer"):
        self.work = work
        self.name = name
        
    def ruturned(self):
        return f"{self.name} человек, работает {self.work}"

people = People() 
print(people.ruturned())
