#Created    by Erik Rutyna -    March 8, 2020
#Last Edit  by Erik Rutyna -    March 8, 2020
# https://dota2.gamepedia.com/Table_of_hero_attributes

#First call preprocessing on the hero data master sheet - edit out misc strings

import csv
import os
#------------------------------------#
#Creating initial hero attribute table
#------------------------------------#

#Remove edited hero table...
if os.path.isfile("heroTableEdit.csv"):
    os.remove("heroTableEdit.csv")

initialTable = open('herodata.csv')
initialTableREAD = csv.reader(initialTable)

heroTable = open("heroTableEdit.csv", "a+")
heroTableWRITE = csv.writer(heroTable)
heroTableREAD = csv.reader(heroTable)

#Find the first hero in the list - as of March 8, 2020: "Abaddon"
i = 0 #row counters
j = 1
for row in initialTableREAD:
    i+=1
    if row[0] == "Abaddon minimap icon.png�Abaddon":
        firstRow = row
        break
#print(i)

#Bring us back to the top of the file
initialTable.seek(0)

#Now deleate the rows before the first hero
for row in initialTableREAD:
    #Forces the write of a new hero table to skip over initial rows
    if j < i:
        j+=1
        #print(j)
        continue
    #----------------------------------------------------------------------#
    #Postprocessing out spaces/misc wording and additional "useless" columns
    #----------------------------------------------------------------------#
    else:
        #Cleans up the hero name by slicing out anything after the name
        row[0] = row[0][0 : row[0].find(" minimap")]
        #Cleans up primary attribute by slicing out anything after the name
        row[1] = row[1][0 : row[1].find(" attribute")]
        heroTableWRITE.writerow(row)

#Close the tables        
initialTable.close()
heroTable.close()

print("Successful run!\n")
