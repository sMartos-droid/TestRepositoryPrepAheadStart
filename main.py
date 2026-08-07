from srcFiles.dog import Dog
from srcFiles.wordSet import WordSet
from srcFiles.employee import Employee
from srcFiles.functionsLib import FunctionsLib
from srcFiles.bankPackage.bankAccount import BankAccount
#************************
#****Exploring lists*****
#************************
'''
strList1 = ["Pepe", "Perez", "Peralta"]
strList2 = [1,2,3]
strList1.extend(strList2)
print(strList1)
print("sliced list, 1st 2 elements: ", strList1[:2])
#lists with the constructor
myGenericList = list(("Jose", 3.5, "Perez", 67))
print(myGenericList)
#working with methods of the list class
myGenericList.append("new string at the last position")
print("append a new element to the original list", myGenericList)
myGenericList.insert(1,"new string at the 1st position")
print("append a new element at the 1st element", myGenericList)
#list comprenhensions
#multiply a list easily
lMyInteger = [1,2,3,4,5,6,7,8,9,10]
lMyIntergerBy2 = [2*item for item in lMyInteger]
print("original list: ", lMyInteger)
print("original list multiply by 2: ", lMyIntergerBy2)
#list filtering with comprenhesions, only even numbers
lMyIntegerFiltered = [item for item in lMyInteger if item%2 == 0]
print("original filtered by even numbers only: ", lMyIntegerFiltered)
lMyIntegerFiltered = [item for item in lMyInteger if item%2 != 0]
print("original filtered by odd numbers only: ", lMyIntegerFiltered)
'''

#booleans logis operations
'''
boolean1 = True
boolean2 = False
if boolean1 and not boolean2:    
    print("boolean1 == true && boolean2 == false")
else:
    print("boolean1 != true && boolean2 != false")

'''

#try out string multiplication
'''
strOriginal = "my dog"
strOriginalBy4 = strOriginal * 4
print(strOriginalBy4)
'''

#Exploring membership operators
'''
isInRange = 1 not in [1,2,3,4,5]
print(isInRange)
'''

#Exploring dictionaires
'''
dDict1 = {
        "test1" : "PASSED", 
        "test2" : "PASSED",
        "test3" : "BLOCKED",
        "test4" : "FAILED"
    }

#Extracting the keys
lDictKeys = list((dDict1.keys()))
print("dDcit1 keys extracted from the list", lDictKeys)

#Extracting the values
lDicValues = list((dDict1.values()))
print("dDcit1 values extracted from the list", lDictKeys)

#Looping dictionaries
#keys
for x in dDict1.keys():
    print("Dict1 keys: ", x)
#values
for x in dDict1.values():
    print("Dict1 values: ", x)
#values pairs, by means, keys and values
for key, value in dDict1.items():
    print("Dict1 key: " + key, "Dict1 values: " + value)
'''




#Control flow 
'''
a = 7
if a < 6:
    print("variable a is < than 6")
else:
    print("variable is > than 6")

lTestForLoop = {1,2,4,5,"hola"}
for item in lTestForLoop:
    print("item: ", item)
    
aWhileLoop = 0
while aWhileLoop < 10:
    print("a inside while loop: ", aWhileLoop)
    aWhileLoop += 1
'''

#Functions
'''
def appendStrings(a, b):
    return a + b

stAppendStrings = appendStrings("Hola", " Mundo")
print ("append str", stAppendStrings)
'''
#playing with classes
'''
myDog = Dog("Boby", 4) 
print("Dog name: " + myDog.getName())
print("Dog nr of legs: ", myDog.getNrOfLegs())
myDog.setNrOfLegs(6)
myDog.setName("Pelayo")
print("##new dog attribues after using the setters##")
print("Dog name: " + myDog.getName())
'''

#strings
#slicing
'''
stTestinSlicing = "string to slice"
print ("Slicing: Original string: " + stTestinSlicing)
stOutcomeString = stTestinSlicing[len(stTestinSlicing) - 1]
print("Slicing: last char of the string: " + stOutcomeString)
stOutcomeString = stTestinSlicing[0]
print("Slicing: 1st char of the string: " + stOutcomeString)
stOutcomeString = stTestinSlicing[0:6]
print("Slicing: 1st 6 chars of the string: " + stOutcomeString)
stOutcomeString = stTestinSlicing[3:]
print("Slicing: from 3rd char till the end: " + stOutcomeString)
stOutcomeString = stTestinSlicing[:9]
print("Slicing: 1st 9 characters of the string: " + stOutcomeString)
'''
#BitWise operators
#binary data in 2 bytes
'''
#19
binDataA = 0b0000000000010011
#34
binDataB = 0b0000000000100010
#AND opeartion, the result should be
# 0b0000 0000 0000 0010 --> 2
binDataResult = binDataA & binDataB
print("Result of AND operation 0b0000 0000 0001 0011 & 0b0000 0000 0010 0010 = ", binDataResult)
#Extract the content of the bit nr 4 of binDataA
binDataResult = (binDataA & 0b10000) >> 4
print("Result of extracting the bit position nr. 4 of the data 0b0000 0000 0001 0011 = ", binDataResult)
#Extract the content of the bit nr 3 of binDataA
binDataResult = (binDataA & 0b01000) >> 3
print("Result of extracting the bit position nr. 3 of the data 0b0000 0000 0001 0011 = ", binDataResult)
'''

#Functions
'''
#A funciton to add or multiply 2 numbers
def myAritmeticFunction(operand1, operand2, operation = "add"):
    if(operation == "add"): 
        return operand1 + operand2
    if(operation == "multiply"):
        return operand1 * operand2
    else:   
        print("operation not defined")
print("1 + 2 opeartion = ", myAritmeticFunction(1,2,"add"))
print("1 * 2 opeartion = ", myAritmeticFunction(1,2,"multiply"))
print("1 / 2 opeartion (illegal) = ", myAritmeticFunction(1,2,"division"))
'''
#************************
#Anatomy of of classes***
#************************
#standard class
'''
stInputStr = str("Holo!,Mondo?, que tal estás?")
myWordSet = WordSet(stInputStr)
print("cleared string: ", myWordSet.getWordsFromTextSnipplet())
'''


#inheritance
#To explore it the target is to build:
#  1. base class --> Person
#                        - FristName 
#                        - LastName
#                        - PersonaID (only number)
#  2. child class --> Employee
#                          - personal ID (only nrs.)
                          
'''newEmployee = Employee("Pepe", "Perez", 78035947, 2)
print(newEmployee.toString())
'''

#exceptions
'''
print("division 1/0: ", FunctionsLib.division(1,0))
'''
#files operations
'''
#FunctionsLib.readTextFile("./inputFiles/testFileRead.txt")
#FunctionsLib.writeTextFile("./inputFiles/testFileWrite.txt")
FunctionsLib.readCsvFile("./inputFiles/10_02_us.csv")
'''
#Preparations for Pytest
myBankAccountNr1 = BankAccount(1, 1300)
print("BankAccount ID: ", myBankAccountNr1.getAccountID())
print("BankAccount Balance: ", myBankAccountNr1.getBalance())
myBankAccountNr1.withDraw(300)
print("BankAccount newBlance after withdrawing 300€: ", myBankAccountNr1.getBalance())
myBankAccountNr1.addMoney(300)
print("BankAccount newBlance after restoring the 300€: ", myBankAccountNr1.getBalance())
