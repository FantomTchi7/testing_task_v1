import pytest
from src.c_module import BankAccount, fibonacci, prime_factors, moving_average, normalize_scores

# C-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_fibonacci_small():
    """Test Fibonacci arvude arvutamist."""
    assert [fibonacci(i) for i in range(6)] == [0,1,1,2,3,5]
    assert fibonacci(10) == 55

def test_prime_factors_basic():
    """Test algtegurite leidmist."""
    assert prime_factors(12) == [2,2,3]
    assert prime_factors(97) == [97]

# TODO: Kirjuta ülejäänud testid ise!
# Vihje: mõned funktsioonid on vigased - sinu testid peaksid need leidma!

def test_bank_account_creation():
    account = BankAccount("Test Kasutaja", 100)
    assert account.balance() == 100

def test_bank_account_invalid_owner():
    with pytest.raises(ValueError, match="Omanik peab olema mittetühi sõne"):
        BankAccount("")
    with pytest.raises(ValueError, match="Omanik peab olema mittetühi sõne"):
        BankAccount(123)

def test_bank_account_negative_initial_balance():
    with pytest.raises(ValueError, match="Algne saldo ei tohi olla negatiivne"):
        BankAccount("Test Kasutaja", -50)

def test_deposit():
    account = BankAccount("Test Kasutaja", 100)
    account.deposit(50)
    assert account.balance() == 150

def test_deposit_invalid_amount():
    account = BankAccount("Test Kasutaja", 100)
    with pytest.raises(ValueError, match="Deposiit peab olema positiivne"):
        account.deposit(0)
    with pytest.raises(ValueError, match="Deposiit peab olema positiivne"):
        account.deposit(-50)

def test_withdraw():
    account = BankAccount("Test Kasutaja", 100)
    account.withdraw(30)
    assert account.balance() == 70

def test_withdraw_insufficient_funds():
    account = BankAccount("Test Kasutaja", 100)
    with pytest.raises(ValueError, match="Pole piisavalt raha kontol"):
        account.withdraw(150)

def test_withdraw_invalid_amount():
    account = BankAccount("Test Kasutaja", 100)
    with pytest.raises(ValueError, match="Väljamakse peab olema positiivne"):
        account.withdraw(0)
    with pytest.raises(ValueError, match="Väljamakse peab olema positiivne"):
        account.withdraw(-30)

def test_transfer_to():
    account1 = BankAccount("Saatja", 200)
    account2 = BankAccount("Saaja", 50)
    account1.transfer_to(account2, 100)
    assert account1.balance() == 100
    assert account2.balance() == 150

def test_transfer_insufficient_funds():
    account1 = BankAccount("Saatja", 100)
    account2 = BankAccount("Saaja", 50)
    with pytest.raises(ValueError, match="Pole piisavalt raha ülekandmiseks"):
        account1.transfer_to(account2, 150)

def test_transfer_invalid_target():
    account1 = BankAccount("Saatja", 100)
    with pytest.raises(ValueError, match="Teine konto peab olema BankAccount objekt"):
        account1.transfer_to("not_an_account", 50)

def test_transfer_invalid_amount():
    account1 = BankAccount("Saatja", 100)
    account2 = BankAccount("Saaja", 50)
    with pytest.raises(ValueError, match="Ülekande summa peab olema positiivne"):
        account1.transfer_to(account2, 0)
    with pytest.raises(ValueError, match="Ülekande summa peab olema positiivne"):
        account1.transfer_to(account2, -50)

def test_fibonacci_edge_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_negative_input():
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_prime_factors_edge_cases():
    assert prime_factors(2) == [2]
    assert prime_factors(8) == [2, 2, 2]
    assert prime_factors(49) == [7, 7]

def test_prime_factors_invalid_input():
    with pytest.raises(ValueError):
        prime_factors(1)
    with pytest.raises(ValueError):
        prime_factors(0)
    with pytest.raises(ValueError):
        prime_factors(-10)

def test_moving_average_basic():
    assert moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]
    assert moving_average([10, 20, 30, 40], 2) == [15.0, 25.0, 35.0]

def test_moving_average_window_size():
    values = [1, 2, 3, 4, 5]
    assert moving_average(values, 1) == [1.0, 2.0, 3.0, 4.0, 5.0]
    assert moving_average(values, 5) == [3.0]
    assert moving_average(values, 6) == []

def test_moving_average_empty_list():
    assert moving_average([], 3) == []

def test_moving_average_invalid_window():
    with pytest.raises(ValueError, match="Aken peab olema positiivne"):
        moving_average([1, 2, 3], 0)
    with pytest.raises(ValueError, match="Aken peab olema positiivne"):
        moving_average([1, 2, 3], -1)

def test_normalize_scores_basic():
    assert normalize_scores([0, 50, 100]) == [0.0, 0.5, 1.0]
    assert normalize_scores([10, 20, 30]) == [0.1, 0.2, 0.3]

def test_normalize_scores_empty_list():
    assert normalize_scores([]) == []

def test_normalize_scores_invalid_values():
    with pytest.raises(ValueError, match="Skoorid peavad olema vahemikus \\[0, 100\\]"):
        normalize_scores([0, 50, 101])
    with pytest.raises(ValueError, match="Skoorid peavad olema vahemikus \\[0, 100\\]"):
        normalize_scores([-1, 50, 100])

def test_normalize_scores_bug():
    assert normalize_scores([10, 20, 90]) == [0.1, 0.2, 0.9]