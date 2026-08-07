import csv
class FunctionsLib:

    @staticmethod
    def division(divisor, dividend):
        try: 
            return divisor / dividend
        except Exception as e: 
            return type(e)
    @staticmethod
    def readTextFile(fullPath):
        try:
            file = open(fullPath,'r')
            #remove \n character
            sCleanedUp = {item.replace('\n', '') for item in file}
            print(sCleanedUp)
            file.close()
        except Exception as e:
            print(type(e))
    
    @staticmethod
    def writeTextFile(fullPath):
        try:
            file = open(fullPath,'w')
            file.write("Hola Mundo\n")
            file.write("Que tal?\n")
            file.close()
        except Exception as e:
            print(type(e))
    
    @staticmethod
    def readCsvFile(fullPath):
        try:
            file = open(fullPath,'r')
            csvReader = csv.DictReader(file, delimiter='\t')
            for item in csvReader:
                print(item)
            file.close()
        except Exception as e:
            print(type(e))
    
    @staticmethod    
    def readJsonFile(fullPath):
        try:
            file = open(fullPath,'r')
            csvReader = csv.DictReader(file, delimiter='\t')
            for item in csvReader:
                print(item)
            file.close()
        except Exception as e:
            print(type(e))
    
        