MAX_LENGTH = 15
TOP_FIVE = 5
EXPENSIVE_WORD = -1


class MostSimilarWord:
    def __init__(self, index=-1, word="?", cost=100):
        self.index = index
        self.word = word
        self.cost = cost

    def print_msw(self):
        print("==================")
        print("Index :", self.index)
        print("Word :", self.word)
        print("Cost :", self.cost)
        print("==================")


def read_random_file():
    file_handle = open("Files/random_file_6.txt", "r", encoding='utf8')
    read_line = file_handle.readlines()
    words = []
    for line in read_line:
        line = line[: -1]
        if len(line) > MAX_LENGTH:
            line = line[: MAX_LENGTH]
        words.append(line)

    file_handle.close()
    return words


def get_word():
    word = input("Enter main word : ")

    if not word:
        print("You must enter non-empty word!\nProgram is terminating...")
        exit()

    elif len(word) > MAX_LENGTH:
        word = word[: MAX_LENGTH]

    return word


def min_edit_distance(word_1, words_of_file, top_5_words):
    number_of_words = len(words_of_file)
    table = [[[None for x in range(MAX_LENGTH + 1)] for y in range(MAX_LENGTH + 1)] for z in range(number_of_words)]

    len_word_1 = len(word_1)  # vertical word |
    len_word_2 = 0  # horizontal word -

    table_initialization(table, number_of_words)

    # i (1,16) # It represents the main word
    #     k (1000) # It is the total numbers of table
    #         j (1,16) # It represents the word is in the file

    for i in range(1, len_word_1 + 1):
        for k in range(number_of_words):
            word_2 = words_of_file[k]
            len_word_2 = len(word_2)
            for j in range(1, len_word_2 + 1):
                if table[k][0][0] < 0:
                    break

                if word_1[i - 1] == word_2[j - 1]:
                    substitution_cost = 0
                else:
                    substitution_cost = 2

                table[k][i][j] = min(table[k][i][j - 1] + 1, table[k][i - 1][j] + 1,
                                     table[k][i - 1][j - 1] + substitution_cost)

                if j == len_word_2:
                    top_5_words = sorted(top_5_words, key=lambda x: x.cost)
                    can_min = abs(table[k][i][j] - (len_word_1 - i))
                    can_max = abs(table[k][i][j] + (len_word_1 - i))

                    appendable = True
                    if can_max < top_5_words[TOP_FIVE - 1].cost:
                        new_word = MostSimilarWord(k, word_2, can_max)

                        for msw in top_5_words:
                            if msw.index == new_word.index:
                                appendable = False
                                if msw.cost != new_word.cost:
                                    msw.cost = new_word.cost

                        if appendable:
                            top_5_words.pop()
                            top_5_words.append(new_word)

                    if can_min > top_5_words[TOP_FIVE - 1].cost:
                        table[k][0][0] = EXPENSIVE_WORD  # EXPENSIVE_WORD = -1

    for i in range(number_of_words):
        print_table(table[i])
        print("INDEX :", i)
        print("Main Word :", word_1)
        print("Other Word :", words_of_file[i])
        if table[i][0][0] != -1:
            print("================================================="
                  "==========================="
                  "===================================COST :", table[i][len_word_1][len(words_of_file[i])])
        print("*******************************************************")

    for i in range(TOP_FIVE):
        top_5_words[i].print_msw()

    calculate_percentage(table, number_of_words)


def calculate_percentage(table, x):

    num_of_None = 0
    for k in range(x):
        for i in range(MAX_LENGTH + 1):
            for j in range(MAX_LENGTH + 1):
                if table[k][i][j] is None:
                    num_of_None = num_of_None + 1

    total_usage = ((MAX_LENGTH + 1) * (MAX_LENGTH + 1) * x) - num_of_None
    percentage = (total_usage * 100.0) / ((MAX_LENGTH + 1) * (MAX_LENGTH + 1) * x)

    print("PERCENTAGE : ", percentage)


def table_initialization(table, word_of_file_count):
    for k in range(word_of_file_count):
        for j in range(MAX_LENGTH + 1):
            table[k][0][j] = j
        for i in range(MAX_LENGTH + 1):
            table[k][i][0] = i


def print_table(table):
    row = len(table)
    for i in range(row):
        print(table[i])


if __name__ == '__main__':
    random_words = read_random_file()

    # main_word = get_word()
    # other_word = get_word()
    # min_edit_distance(main_word, other_word)

    # print(random_words)
    # print(len(random_words))

    most_similar_five_words = [MostSimilarWord() for i in range(TOP_FIVE)]
    min_edit_distance("ali", random_words, most_similar_five_words)
