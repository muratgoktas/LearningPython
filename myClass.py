#self => this 

from typing import Any


class Human:
    otherName="Kayra Deniz"
    # built-in(__init__ initialize) => constructor (yapıcı blok)
    def __init__(self) -> None:
        print("Human's instance created.")

    def talk(self, firstName): # self => this ile aynı ve parametre almak zorunda...
        print(f"{firstName} talked.")
    def walk(self):
        self.talk("Recep")
        print(f"{self.otherName} walked.")
    def run(self):
        print(f"{self.otherName} runned.")


# instance => örnek
human1 = Human()
human1.talk("Murat")
human1.walk()
human1.run()
human1.otherName="Melike Tuana"
human1.run()
human1.talk("Birgül")
human1.walk()

human2=Human()
human2.otherName="Salih"
human2.run()
human2.walk()

class productDal:
    def __init__(self,name) :
        self.name=name
    def __str__(self) -> str:
        return f"STR fonksiyounudan geri dönen değer : {self.name}."      
    def  Add(self):
        print(f"{self.name} added.")
    def Delete(self):
        print(f"{self.name} deleted.")
    def Update(self):
        print(f"{self.name} updated.")

productDal1= productDal("Computer")
productDal1.Add()
productDal1.Update()

productDal2= productDal("Printer")
productDal2.Delete()

print(productDal2)
print(productDal1)