def read_random_file():
    file_handle = open("Files/random_file_1.txt", "r", encoding='utf8')
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


def min_edit_distance(word_1, word_2):
    print("main word :", word_1, "with length : ", len(word_1))
    print("other word :", word_2, "with length : ", len(word_2))

    len_word_1 = len(word_1)  # vertical word |
    len_word_2 = len(word_2)  # horizontal word -

    table = [[0 for i in range(len_word_2 + 1)] for i in range(len_word_1 + 1)]
    table_initialization(table, len_word_1, len_word_2)

    for i in range(1, len_word_1 + 1):
        for j in range(1, len_word_2 + 1):
            if word_1[i - 1] == word_2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
                substitution_cost = 0 + table[i - 1][j - 1]
            else:
                substitution_cost = 2 + table[i - 1][j - 1]

            insert_or_delete_cost = min(table[i][j - 1], table[i - 1][j]) + 1

            table[i][j] = min(substitution_cost, insert_or_delete_cost)

    print_table(table)


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
    # random_words = read_random_file()

    main_word = get_word()
    other_word = get_word()
    min_edit_distance(main_word, other_word)

    # print(random_words)
    # print(len(random_words))
