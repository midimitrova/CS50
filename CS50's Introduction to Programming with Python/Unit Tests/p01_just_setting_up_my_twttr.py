
def main():
    my_string = input('Input: ')
    msg = shorten(my_string)
    print(f'Output: {msg}')


def shorten(word):
    word_without_vowels = ''
    for char in word:
        if not char.lower() in ['a', 'e', 'i', 'o', 'u']:
            word_without_vowels += char
    return word_without_vowels

if __name__ == "__main__":
    main()