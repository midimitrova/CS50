from p03_vanity_plates import is_valid

def main():
    test_lenght()
    test_letters()
    test_zero()
    test_numbers()
    test_punctuation()

def test_lenght():
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFG') == False

def test_letters():
    assert is_valid('AA55') == True
    assert is_valid('A5AB') == False
    assert is_valid('2AB') == False
    assert is_valid('55') == False

def test_numbers():
    assert is_valid('AA66') == True
    assert is_valid('AAA5AB') == False

def test_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

def test_punctuation():
    assert is_valid('PI.145') == False
    assert is_valid('PI!145') == False
    assert is_valid('PI 145') == False

if __name__ == '__main__':
    main()
