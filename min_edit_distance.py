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
    file_handle = open("Files/test_file.txt", "r", encoding='utf8')
    read_line = file_handle.readlines()
    words = []
    for line in read_line:
        line = line[: -1]
        if len(line) > 15:
            line = line[: 15]
        words.append(line)

    file_handle.close()
    return words


def get_word():
    word = input("Enter main word : ")

    if not word:
        print("You must enter non-empty word!\nProgram is terminating...")
        exit()

    elif len(word) > 15:
        word = word[: 15]

    return word


def run_min_edit_distance_for_all(most_similar_word_list, word, file_words):

    for i in range(5):
        most_similar_word_list[i].print_msw()
        print("=========================================")

    for i in range(len(file_words)):
        cost = min_edit_distance(word, file_words[i], i)

        if cost < most_similar_word_list[4].cost:
            most_similar_word_list.pop()
            new_word = MostSimilarWord(i, file_words[i], cost)
            most_similar_word_list.append(new_word)

        most_similar_word_list = sorted(most_similar_word_list, key=lambda x: x.cost)

    for i in range(5):
        most_similar_word_list[i].print_msw()
        print("=========================================")


def min_edit_distance(word_1, word_2, index):
    print("main word :", word_1, "with length : ", len(word_1))
    print("other word :", word_2, "with length : ", len(word_2))

    len_word_1 = len(word_1)  # vertical word |
    len_word_2 = len(word_2)  # horizontal word -

    table = [[0 for i in range(len_word_2 + 1)] for i in range(len_word_1 + 1)]
    table_initialization(table, len_word_1, len_word_2)

    for i in range(1, len_word_1 + 1):
        for j in range(1, len_word_2 + 1):
            if word_1[i - 1] == word_2[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 2

            table[i][j] = min(table[i][j - 1] + 1, table[i - 1][j] + 1, table[i - 1][j - 1] + substitution_cost)

    print_table(table)
    print("word_2_index :", index)
    return table[len_word_1][len_word_2]


def table_initialization(table, len_word_1, len_word_2):
    for i in range(len_word_2 + 1):
        table[0][i] = i
    for j in range(len_word_1 + 1):
        table[j][0] = j


def print_table(table):
    row = len(table)
    column = len(table[0])
    print("row :", row)
    print("column :", column)

    for i in range(row):
        print(table[i])


if __name__ == '__main__':
    random_words = read_random_file()

    # main_word = get_word()
    # other_word = get_word()
    # min_edit_distance(main_word, other_word)

    # print(random_words)
    # print(len(random_words))

    most_similar_five_words = [MostSimilarWord() for i in range(5)]

    run_min_edit_distance_for_all(most_similar_five_words, "ali", random_words)
