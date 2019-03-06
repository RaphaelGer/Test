
#das brauche ich später noch um die dateien mit funktionen abzurufen
"""class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmx.at"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def all(self):
        return "{} {}".format(self.fullname(), self.pay)"""

#zuerst habe ich mal einen int definiert damit die while schleife weis wie oft ich sie ausführen will
#da muss ich mir noch etwas besseres einfallen lassen vlt mit break ?!?!

i = 0

while i <= 2:
    #zuerst öffne ich meine .txt damit ich darauf zugreifen kann und "a" damit ich etwas hinzufügen kann
    new = open("Employee.txt", "a")

    #Hier frage ich diverse dinge ab die ich in meiner .txt haben möchte
    first = input("Geben sie den Vornamen ein: ")
    last = input("Geben sie den Nachnamen ein: ")
    pay = input("Geben sie ihr Gehalt ein: ")

    #Kurze bestätigung für den user, dass es funktioniert hat
    print("Angestellter " + str(i+1) + " wurde hinzugefügt")

    #dann formatiere ich den input in einer liste so wie ich ihn gerne hätte
    emp = [first, last, pay]

    #hier füge ich es der .txt. hinzu
    new.write(("Emp" + str(i+1) + " = " + str(emp)))
    new.write("\n")
    i += 1

#dann öffne ich noch einmal die .txt datei nur um sie lesen zu können
text = open("Employee.txt", "r")

#hier hätte ich gerne das er mir nun alle Zeilen ausgibt jedoch gibt er mir immer wieder eine Zeile zu wenig aus ?!
for line in text:
    print(line)

#hier schließe ich die .txt wieder
text.close()




