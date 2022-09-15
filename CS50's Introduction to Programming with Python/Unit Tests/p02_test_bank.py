from p02_home_federal_savings_bank import value

def main():
    test_zero()
    test_twenty()
    test_hundred()

def test_zero():
    assert value('hello gi') == 0
    assert value('Hello') == 0
    assert value('HelLo') == 0

def test_twenty():
    assert value('How you doing?') == 20

def test_hundred():
    assert value('What’s up') == 100


if __name__ == "__main__":
    main()