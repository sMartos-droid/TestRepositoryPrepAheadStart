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
    with pytest.raises(ValueError, match = "invalid amount, it should be > 0€"):
        testInput.transferFundsTo(targetBbankAccount, requestedMoney)


# Additional tests to improve coverage
@pytest.mark.parametrize("account_id,balance",
                         [
                             (1, -50),
                             (0, -0.01),
                         ])
def test_constructor_negative_balance_raises(account_id, balance):
    with pytest.raises(ValueError, match="invalid amount. It must be > 0"):
        BankAccount(account_id, balance)


def test_addMoney_zero_no_change():
    acc = BankAccount(5, 200)
    acc.addMoney(0)
    assert acc.getBalance() == 200


def test_withdraw_exact_balance_to_zero():
    acc = BankAccount(6, 150)
    acc.withDraw(150)
    assert acc.getBalance() == 0


def test_transfer_to_none_raises_typeerror():
    src = BankAccount(7, 100)
    with pytest.raises(TypeError, match="target bank account not defined"):
        src.transferFundsTo(None, 10)


def test_transfer_funds_greater_than_balance_raises():
    src = BankAccount(8, 100)
    tgt = BankAccount(9, 0)
    with pytest.raises(ValueError):
        src.transferFundsTo(tgt, 200)


def test_setters_modify_state():
    acc = BankAccount(10, 300)
    acc.setBalance(400)
    acc.setAccountID(1234)
    assert acc.getBalance() == 400
    assert acc.getAccountID() == 1234

'''
Test cases generated by the Copilot IA
'''
@pytest.mark.parametrize("testInput, expectedBalance",
                         [(BankAccount(1,1300), 1300),
                          (BankAccount(0,0), 0),
                          (BankAccount(1000,500), 500)      
                          ])
def test_constructor_positive_balance_sets_balance(testInput, expectedBalance):
    assert testInput.getBalance() == expectedBalance


def test_addMoney_accepts_float_and_large_values():
    acc = BankAccount(12, 10.5)
    acc.addMoney(0.25)
    assert acc.getBalance() == pytest.approx(10.75)
    acc.addMoney(1000000)
    assert acc.getBalance() == pytest.approx(1000010.75)


def test_withDraw_zero_no_change():
    acc = BankAccount(13, 500)
    acc.withDraw(0)
    assert acc.getBalance() == 500


def test_withDraw_fractional_amount():
    acc = BankAccount(14, 10.5)
    acc.withDraw(0.5)
    assert acc.getBalance() == pytest.approx(10.0)


def test_transfer_depletes_source_and_increases_target():
    src = BankAccount(15, 250)
    tgt = BankAccount(16, 50)
    src.transferFundsTo(tgt, 250)
    assert src.getBalance() == 0
    assert tgt.getBalance() == 300


def test_sequence_of_operations():
    acc = BankAccount(17, 100)
    acc.addMoney(50)
    acc.withDraw(25)
    assert acc.getBalance() == 125
    other = BankAccount(18, 0)
    acc.transferFundsTo(other, 25)
    assert acc.getBalance() == 100
    assert other.getBalance() == 25


def test_setBalance_allows_negative_value():
    acc = BankAccount(19, 200)
    acc.setBalance(-500)
    assert acc.getBalance() == -500
