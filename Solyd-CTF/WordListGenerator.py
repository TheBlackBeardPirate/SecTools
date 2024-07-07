
def num_gen():
    with open('num.txt', 'a') as file:
        for i in range(10000):
            num = '{0:04}\n'.format(i)
            file.write(num)


def word_gen():
    with open('words.txt', 'r') as file:
        words = file.readlines()

    with open('num.txt', 'r') as file:
        nums = file.readlines()

    with open('wordlist.txt', 'a') as file:
        for word in words:
            new_word = word.replace(' ', '')
            new_word = new_word.lower()

            for num in nums:
                passwd = new_word.strip() + num
                file.write(passwd)


if __name__ == "__main__":
    num_gen()
    word_gen()
