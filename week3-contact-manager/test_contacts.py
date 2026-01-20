from contacts_manager import valid_phone, valid_email

def test_phone():
    assert valid_phone("1234567890") == True
    assert valid_phone("12345") == False
    assert valid_phone("abc123") == False


def test_email():
    assert valid_email("test@example.com") == True
    assert valid_email("testexample.com") == False
    assert valid_email("test@com") == False


print("All tests passed.")
