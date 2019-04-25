import random

class Sort:
    def createEvenNamesFrom(self, names):
        random.shuffle(names)
        random.shuffle(names)
        evenNames = []
        resultEvenNames = []
        for i in range(0, len(names)):
            if i + 1 == len(names):
                evenNames.append([i, 0])
            else:
                evenNames.append([i, i+1])
            resultEvenNames.append([names[evenNames[i][0]], names[evenNames[i][1]]])
        return resultEvenNames

    def createListOfNamesFrom(self, dict):
        listOfNames = []
        for key in dict.keys():
            listOfNames.append(key)
        return listOfNames

    
    