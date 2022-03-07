import time

file = open('C:/Users/Gebruiker/OneDrive/Bureaublad/ICT/read-files/README.md', 'r')
content = file.readlines()
for line in content:
    print(line)
    time.sleep(1)
file.close()