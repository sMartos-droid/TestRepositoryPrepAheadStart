from typing import Literal

from srcFiles.bankPackage.bankAccount import BankAccount
import pytest

@pytest.mark.parametrize("testInput, expectedBalance",
                         [(BankAccount(1,1300), 1300),
                          (BankAccount(0,0), 0),
                          (BankAccount(1000,500), 500)      
                          ])
def test_getBalance(testInput, expectedBalance):
    assert testInput.getBalance() == expectedBalance
    
@pytest.mark.parametrize("testInput, expectedAccountID",
                         [(BankAccount(1,1300), 1),
                          (BankAccount(0,0), 0),
                          (BankAccount(1000,500), 1000)      
                          ])
def test_getAccountID(testInput, expectedAccountID):
    assert testInput.getAccountID() == expectedAccountID

#****AddMoney**** 
#positive testing
@pytest.mark.parametrize("testInput, addedMoney",
                         [(BankAccount(1,1300), 1000),
                          (BankAccount(0,0), 500),
                          (BankAccount(1000,500), 2000)      
                          ])
def test_addMoney(testInput, addedMoney):
    originalBalance = testInput.getBalance()
    testInput.addMoney(addedMoney)
    assert (originalBalance + addedMoney) == testInput.getBalance()
    
#negative testing
@pytest.mark.parametrize("testInput, addedMoney",
                         [(BankAccount(1,1300), -1301),
                          (BankAccount(0,0), -500),
                          (BankAccount(1000,500), -2000)      
                          ])
def test_Minus_addMoney(testInput, addedMoney):
    with pytest.raises(ValueError, match = "invalid amount. It must be > 0"):
        testInput.addMoney(addedMoney)


#****Withdraw**** 
#inrange testing*
@pytest.mark.parametrize("testInput, requestedMoney",
                         [(BankAccount(1,1300), 300),
                          (BankAccount(0,0), 0),
                          ])
def test_withDraw(testInput, requestedMoney):
    originalBalance = testInput.getBalance()
    testInput.withDraw(requestedMoney);
    assert testInput.getBalance() == (originalBalance - requestedMoney)
#boundary + 1
@pytest.mark.parametrize("testInput, requestedMoney",
                         [(BankAccount(1,1300), 1301),
                          (BankAccount(0,0), 1),
                          ])
def test_withDraw_boundary_plus_1(testInput, requestedMoney):
    with pytest.raises(ValueError, match = "invalid amount, it is > than the available balance"):
        testInput.withDraw(requestedMoney)
    
#boundary - 1
@pytest.mark.parametrize("testInput, requestedMoney",
                         [(BankAccount(1,1300), 1299),
                          (BankAccount(0,100), 99),
                          ])
def test_withDraw_boundary_minus_1(testInput, requestedMoney):
    originalBalance = testInput.getBalance()
    testInput.withDraw(requestedMoney);
    assert testInput.getBalance() == (originalBalance - requestedMoney)
#withdraw negative values
@pytest.mark.parametrize("testInput, requestedMoney",
                         [(BankAccount(1,1300), -1300),
                          (BankAccount(0,0), -0.1),
                          ])
def test_withDraw_negative_amount(testInput, requestedMoney):
    with pytest.raises(ValueError, match = "invalid amount, it is < 0€"):
        testInput.withDraw(requestedMoney)
        
#****TransferFundsTo**** 
@pytest.mark.parametrize("testInput, requestedMoney",
                         [(BankAccount(1,1300), 1300),
                          (BankAccount(0,0), 0),
                          (BankAccount(0,10000), 500),
                          ])
#nominal case
def test_transferFundsTo(testInput, requestedMoney):
    targetBbankAccount = BankAccount(10,0)
    testInput.transferFundsTo(targetBbankAccount, requestedMoney)
    assert targetBbankAccount.getBalance() == requestedMoney
#transfer negative funds

@pytest.mark.parametrize("testInput, requestedMoney",
                         [(BankAccount(1,1300), -1300),
                          (BankAccount(0,0), -1),
                          (BankAccount(0,10000), -10),
                          ])
def test_transferFundsTo_negative(testInput, requestedMoney):
    targetBbankAccount = BankAccount(10,0)
    with pytest.raises(ValueError, match = "invalid amount, it is < 0€"):
        testInput.transferFundsTo(targetBbankAccount, requestedMoney)


