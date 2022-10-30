from p01_seasons import check_date


def main():
    test_check_date()


def test_check_date():
    assert check_date('1995-02-03') == ('1995', '02', '03')
    assert check_date('1995-2-3') == None
    assert check_date('February 3, 1995') == None


if __name__ == '__main__':
    main()
