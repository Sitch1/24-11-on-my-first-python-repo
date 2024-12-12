
#### print ####
### !!Was ist die Print-Funktion? Mit der print-Funktion gibst du in Python eine bestimmte Nachricht auf dem Bildschirm aus.!!###

print('Hallo, Welt ! Hier erstelle ich meine ersten Codes')

#### print (berechnungen) #### 

print('Mathe aufgaben')

print(10 + 10)
print(10 - 10)
print(10 * 10)
print(10 / 10)

#### variable ####

### !!!.Eine Variable kann verschiedenen Datentypen zugeordnet werden, 
#    zum Beispiel kann einer Variable ein Text zugewiesen werden, 
#    indem dieser in einfache Anführungszeichen (' ') gesetzt wird. !!! ###

name = 'Max' (str) string                       # !!.Datentyp für Text.!! Übersetzt: (str) string = Text in python #
age =   10      (int) integer                   # !!.Datentyp für ganze Zahlen.!! Übersetzt: (int) integer = ganze Zahl in python #
taxes = 0.19    (float) floating-point number   # !!.Datentyp für Zahlen mit Dezimalstellen.!! Übersetzt: (float) floating-point number = Zahlen mit Dezimalstellen in Pyhton #
is_programmer = true / false (bool) boolean     # !!.Datentyp für Wahrheitswerte.!! Überstezt: (bool) boolean = Wahrheitswerte, wahr(true) oder falsch(false) in python #

#### ÜBUNG 1.0 ####

## !!.variable zuordnen Text und Zah.l!! ##


# Beispiel 1. #
name_1 = 'Stitch'
age = 21

print('Mein Name ist Stitch')
print('Ich bin 21 Jhare alt')

## !!.Ein Wert (name) einer variable anzeigen.!! ##
## !!.Eine Zahl zwischen zwei Texte anzeigen.!! ##

print('Mein Name ist ' + name)
print('Ich bin ' + (str)age + ' Jahre alt')      # !!.ACHTUNG.!! - Eine Zahl kann nicht im Text angezeigt werden und muss eine varibale zugeordnet werden, mit (str) oder ('') !! #  

# Beispiel 2. #
 # !!.Bewerbung z.B. Sehr geherte oder Sehr geehrter Herr.!! #


name1 = 'Max Mustermann'
my_name = 'Stitch'
age = 21
city = 'Stitch.City'

is_women = False
    
if is_women:
    print('Sehr geehrte Frau' + name1 + ',')
else:
    print('Sehr geehrter Herr' + name1 + ',')
print('')
print('Mein Name ist ' + my_name + '.')
print('Ich bin ' + str(age) + ' Jahre alt.')
print('Mein Wohnort ist in ' + city + '.')







