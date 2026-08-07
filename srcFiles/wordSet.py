'''
This class is intended to format input text snipplets. 
Requirements are:   
    1. The text snipple is a string 
    2. The Text snipplet must be stored in a set() object
    3. A method (private) to replace the following punctuation characters --> [. , ; ! ?] by a blank space
    4. A method (private) to sustitue the character "o" by "@"
    5. A method to add an additional text snipple once the orignal has been created     
    6. A method to do retrive the text snipple as a text, after processing it with the both previous things 
     
the text snipplets will be store in a set() objet
'''


class WordSet:
    #inner members, set

    #constructor
    def __init__(self, text):
            #inner fields (priavate with __)
            self.__text = text
    
    #+++++++++++++++++++++
    #+++++methods+++++++++
    #+++++++++++++++++++++
    
    #replace the special puntuation characters defined in sTargetPuntuation by " "
    #Parameters:
    #    N/A
    #Returns:
    #(str1): The string which gets clean up. 
    def __cleanPunctuation(self):
        replacements = str.maketrans({"." : " ", "," : " ", ";" : " " ,"!" : " " ,"?" : " "})
        self.__text = self.__text.translate(replacements)
        return self.__text


    #replace the character O by  "@"
    #Parameters:
    #    N/A
    #Returns:
    #(str1): The string which gets clean up. 
    def __replaceMasculineByAt(self):
        self.__text = self.__text.replace('o','@')
        return self.__text
    
    #retrieve the input text cleanned as a set of strings
    #Parameters:
    #    N/A
    #Returns:
    #(set1): The set with the input string cleaned up.
    def getWordsFromTextSnipplet(self):
        self.__cleanPunctuation()
        self.__replaceMasculineByAt()
        return set(self.__text) 