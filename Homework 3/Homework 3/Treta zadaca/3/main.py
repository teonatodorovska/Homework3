
def count_words_in_file(filename):
    word_count = {}


    with open(filename, 'r') as file:
        text = file.read()


    words = text.lower().replace(",", "").replace(".", "").replace("'", "").replace("-", " ").split()


    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count



filename = 'ex_1.txt'


word_count = count_words_in_file(filename)
print(word_count)
