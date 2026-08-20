class BankAccount:
    def __init__(self, accountId, balance):
        #inner fields (priavate with __)
        if balance < 0:
            raise ValueError("invalid amount. It must be > 0")
        else:      
            self.__balance = balance
        #6 digits (numerical)
        self.__accountID = accountId
        
    #getters
    """
    Returns the account´s balance
        Parameters:
            N/A
        Returns:
            (float): current account balance
    """    
    def getBalance(self):
        return self.__balance
    """
    Returns the account´s ID
        Parameters:
            N/A
        Returns:
            (int): with the account ID
    """
    def getAccountID(self):
        return self.__accountID
        
    #setters
    def setBalance(self, amount):
        self.__balance = amount
    def setAccountID(self, idNr):
        self.__accountID = idNr
            
    #methods
    '''
    Add founds to the account
        Parameters:
            (double) the amount to be added to the account balance
        Returns:
            (exception): ValueError in case the amount is not inside the valid range. 
    '''
    def addMoney(self, amount):
        if(amount<0):
            raise ValueError("invalid amount. It must be > 0")
        else:
            self.__balance += amount
    '''
    Withdraw founds from the account
        Parameters:
            (double) the amount to be wirthdrawed from the account balance
        Returns:
            (exception): ValueError in case of:
                - The amount > balance available 
                - The amount is < 0
            N/A in case the operation is sucsessful
    '''
    def withDraw(self, amount):        
        if amount > self.__balance:
            raise ValueError("invalid amount, it is > than the available balance")
        if amount < 0:
            raise ValueError("invalid amount, it is < 0€")
        self.__balance -= amount
    '''
    Transfer founds to a different account
        Parameters:
            (BankAccount) object witht the target account
            (double) funds to be transfer from the original account to the target one
        Returns:
            (exception): ValueError in case of:
                - The amount > balance available 
                - The amount is < 0
            N/A in case the operation is sucsessful
    '''             
    def transferFundsTo(self, targetBankAccount, funds):
        if targetBankAccount is None:
            raise TypeError("target bank account not defined")
        if funds < 0:
            raise ValueError("invalid amount, it should be > 0€")
        if funds > self.__balance: 
            raise ValueError("invalid amount, it is > than the available balance")      
        self.withDraw(funds)
        targetBankAccount.addMoney(funds)

    