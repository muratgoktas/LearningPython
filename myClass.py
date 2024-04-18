class Human:
    def talk(self, firstName): # parametre almak zorunda...
        print(f"{firstName} talked.")
    def walk(self):
        print("Human walked.")


# instance => örnek
human1 = Human()
human1.talk("Murat")
human1.walk()
