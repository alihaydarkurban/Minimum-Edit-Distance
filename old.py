MAX_LENGTH = 15
TOP_FIVE = 5


class MostSimilarWord:
    def __init__(self, index=-1, word="?", cost=30):
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
    file_handle = open("Files/random_file_5.txt", "r", encoding='utf8')
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

    for k in range(number_of_words):
        word_2 = words_of_file[k]
        len_word_2 = len(word_2)

        for i in range(1, len_word_1 + 1):
            for j in range(1, len_word_2 + 1):
                if word_1[i - 1] == word_2[j - 1]:
                    substitution_cost = 0
                else:
                    substitution_cost = 2

                table[k][i][j] = min(table[k][i][j - 1] + 1, table[k][i - 1][j] + 1,
                                     table[k][i - 1][j - 1] + substitution_cost)

        cost = table[k][i][j]
        if cost < top_5_words[TOP_FIVE - 1].cost:
            top_5_words.pop()
            new_word = MostSimilarWord(k, word_2, cost)
            top_5_words.append(new_word)

        top_5_words = sorted(top_5_words, key=lambda x: x.cost)

        print("Total Cost :", cost)
        print("main word :", word_1)
        print("other word :", word_2)
        print_table(table[k])
        print("*******************************************************")

    calculate_percentage(table, number_of_words)
    return top_5_words


def calculate_percentage(table, x):

    num_of_None = 0
    for k in range(x):
        for i in range(MAX_LENGTH + 1):
            for j in range(MAX_LENGTH + 1):
                if table[k][i][j] is None:
                    num_of_None = num_of_None + 1

    total_usage = ((MAX_LENGTH + 1) * (MAX_LENGTH + 1) * x) - num_of_None - (((2 * MAX_LENGTH) + 1) * x)
    # total_usage = ((MAX_LENGTH + 1) * (MAX_LENGTH + 1) * x) - num_of_None
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
    most_similar_five_words = min_edit_distance("testedildi", random_words, most_similar_five_words)

    for i in range(TOP_FIVE):
        most_similar_five_words[i].print_msw()

    # a = 4
    # min_cost_dict = {i: 100 for i in range(10)}
    #
    # min_cost_dict = sorted(min_cost_dict.items(), key=lambda x: x[1])
    #
    # for i in range(10):
    #     if min_cost_dict[i][0] == a:
    #         print(min_cost_dict[i])

    # a = [5, 10,1,4,6,7]
    # a.sort()
    # print(a)

