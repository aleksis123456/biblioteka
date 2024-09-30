''''from termcolor import colored
text = colored('Hello, word!', 'red', attrs=['bord'])
print(text)

import wikipedia 
wikipedia.set_lang("LV")
print(wikipedia.summary ("Riga"))
print()

from prettytable import PrettyTable
table=PrettyTable()
table.field_names=['Name', 'Age','City']
table.add_row (['Tom', '15', 'Riga'])
print(table)'''
 
import matplotlib.pyplot as plt

plt.plot([1,2,3,4])
plt.ylabl('Funkcijas grafiks')
plt.show()

plt.plot([4,7,2,16,3])
plt.ylable('Funkcija')
plt.show()