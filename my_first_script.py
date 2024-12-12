
















print ("Hallo Welt")

first_name = "Dustin"
last_name = "P."



# print() gibt den Befehl wieder was in der Klammer steht

print (first_name + " " + last_name)





# input(), erstellt ein Eingabefehlt im Skript, wie beim z.B Dein Name anschließend läuft der Skript weiter
name = input("Wie heisst du? ")
print("Hallo, " + name + "!")


alter = int(input("Wie alt bist du? ")) 
print("Du bist " + str(alter) + " Jahre alt.")

##### Berechnungen #######

zahl1 = 31
zahl2 = 32

print("zahl 1 + zahl 2:", zahl1 +  zahl2)
print("zahl 1 - zahl 2:", zahl1 + zahl2)
print("zahl 1 * zahl 2:", zahl1 * zahl2)
print("zahl 1 / zahl 2:", zahl1 / zahl2)


###### !Aufgabe 2! #######

Note1 = 3
Note2 = 4
note3 = 4

Note1 = float(input("Erste Zahl eingeben:"))
Note2 = float(input("Zweite Zahl eingeben:"))
note3 = float(input("Dritte Zahl eingeben:"))

###### !Durchschnitt berechnen! ###### result

# durchschnitt = (Note1+Note2+note3) / 3
# print("ergebiss ist" , durchschnitt)  funktoniert gleich 

 
 z = Note1 + Note2 + note3
print("durchschnitt", z/3)


##### !Aufgabe 3.3! ######

KOPIERT selber noch nicht verstanden...


a = input("Wie viele Kilometer sollen in Meilen umgerechnet werden?")
b="10"
def km_to_miles(km):
    x = float(km)
    c = float(0.621371)
    d=x*c
    return d

print (a, "Kilometer entsprechen: ", km_to_miles(a), "Meilen")
print (b, "Kilometer entsprechen: ", km_to_miles(b), "Meilen")











