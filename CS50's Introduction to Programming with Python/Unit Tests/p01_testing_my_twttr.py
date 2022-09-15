from p01_just_setting_up_my_twttr import shorten


def main():
    test_upper_lower_case()
    test_numbers()
    test_punctuation()

def test_upper_lower_case():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwitTeR') == 'TwtTR'

def test_numbers():
    assert shorten('123') == '123'

def test_punctuation():
    assert shorten('.,!') == '.,!'


if __name__ == '__main__':
    main()

