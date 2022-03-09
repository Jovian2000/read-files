# read-files
## F1.09.01.O2 - The zen of Reading Me
### The Zen of Python
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
``` python
import time
file = open('C:/Users/Gebruiker/OneDrive/Bureaublad/ICT/read-files/README.md', 'r')
content = file.readlines()
for line in content:
    print(line)
    time.sleep(1)
file.close()
```
## F1.09.01.L1 - met with
hier heb ik de progamma aangepast en with gebruikt
``` python
import time

with open("C:/Users/Gebruiker/OneDrive/Bureaublad/ICT/read-files/README.md") as file:
    for line in file:
        print(line)
        time.sleep(1)
```
## F1.09.01.O3 - Install PyYAML
pyYAML geinstalleerd
## F1.09.01.O4 - Nieuwe prijzen, dus nieuwe settings
papi-gelato is nu aangepast, dit zijn nu de prijzen
``` python
prijsBolletje = 0.95
prijsHoorntje = 1.25
prijsBakje = 0.80
prijsSlagroom = 0.55
prijsSprinkels = 0.30
prijsCaramelsausHorn = 0.60
prijsCaramelsausBak = 0.80

prijsPerLiter = 8.99
btw = 0.06 
```
dit is de code voor het lezen van het yaml bestand
``` python
with open("C:/Users/Gebruiker/OneDrive/Bureaublad/ICT/read-files/settings.yml", "r") as file:
    docs = yaml.safe_load(file)
    print(type(docs))
    for d,v in docs.items():
        print(d,v)
```
(Ik heb de oude papi gelato programma van leerpad 5 gebruikt, ik heb leerpad 8.4 nog niet gedaan.)