MAX_LENGTH = 15  # It is for limitation the word of length.
TOP_FIVE = 5  # It is for most similar five words.
EXPENSIVE_WORD = -1  # It specifies the word can not be in the most similar five words.


# It holds information about the word.
# index, specifies the line number of the word inside the file.
# word, specifies the word of the file.
# cost, specifies the edit-distance cost between the main word and the word inside the file.
class MostSimilarWord:

    # It is constructor of the class.
    def __init__(self, index=-1, word="?", cost=100):  # Default values for the properties.
        # Assign the properties.
        self.index = index
        self.word = word
        self.cost = cost

    # It prints the information about the class object
    def print_msw(self):
        print("-------------------------")
        print("Word :", self.word)
        print("Cost :", self.cost)
        print("-------------------------")


# It reads the file line by line and fill the list with the words.
# It returns the list that has words of the file.
# file_name is the path of the file that will be read.
def read_random_file(file_name):
    file_handle = open(file_name, "r", encoding='utf8')
    read_line = file_handle.readlines()
    words = []
    for line in read_line:
        line = line[: -1]
        if len(line) > MAX_LENGTH:
            line = line[: MAX_LENGTH]
        words.append(line)

    file_handle.close()
    return words


# It gets the main word from the user and returns it.
# It can terminate the program, if the main word is null.
# If the main word has more than 15 letters, it ignores the rest.
def get_word():
    word = input("Enter main word : ")
    if not word:
        print("You must enter non-empty word!\nProgram is terminating...")
        exit()
    elif len(word) > MAX_LENGTH:
        word = word[: MAX_LENGTH]

    return word


# It is an enhanced version of edit distance algorithm.
# It can decide that whether the current word will not in the most similar five words.
# It does do it without filling the whole distances between the words.
# It assigns EXPENSIVE_WORD which is -1 to the table of the word which has more cost.
# word_1 is the main word that was entered by the user.
# words_of_file holds the words that was read from the file.
# top_5_words holds the most similar five words.
# Cost of insertion is 1.
# Cost of deletion is 1.
# Cost of substitution is 2.
def min_edit_distance(word_1, words_of_file, top_5_words):
    number_of_words = len(words_of_file)
    table = [[[0 for x in range(MAX_LENGTH + 1)] for y in range(MAX_LENGTH + 1)] for z in range(number_of_words)]  # Create 3D table.

    len_word_1 = len(word_1)  # vertical word |
    len_word_2 = 0  # horizontal word -
    used_place_count = 0  # It is a counter for the used places.
    table_initialization(table, number_of_words)
    total_place = 0  # It is the for the total number of all places for words.
    # This loop finds the total number of places that can be used.
    for word in words_of_file:
        total_place = total_place + (len_word_1 * len(word))

    # i (1,16) # It represents the main word.
    #     k (1000) # It represents the total number of the words in the file.
    #         j (1,16) # It represents a word which is in the file.

    for i in range(1, len_word_1 + 1):
        for k in range(number_of_words):
            word_2 = words_of_file[k]
            len_word_2 = len(word_2)
            for j in range(1, len_word_2 + 1):
                if table[k][0][0] < 0:  # It checks whether the table has assigned as expensive cost.
                    break
                if word_1[i - 1] == word_2[j - 1]:
                    substitution_cost = 0
                else:
                    substitution_cost = 2

                table[k][i][j] = min(table[k][i][j - 1] + 1, table[k][i - 1][j] + 1,
                                     table[k][i - 1][j - 1] + substitution_cost)

                used_place_count = used_place_count + 1  # Increment the used_place_count.

                # It checks if the cost of X was calculated. (cost of 1, cost of 2,.. cost of X)
                if j == len_word_2:
                    top_5_words = sorted(top_5_words, key=lambda x: x.cost)  # Sorts the similar words based on the cost.
                    can_min = abs(table[k][i][j] - (len_word_1 - i))  # Calculates the minimum cost that can be.
                    can_max = abs(table[k][i][j] + (len_word_1 - i))  # Calculates the maximum cost that can be.

                    appendable = True
                    # It checks if the can_max cost is smaller than the most similar five words costs.
                    if can_max < top_5_words[TOP_FIVE - 1].cost:
                        new_word = MostSimilarWord(k, word_2, can_max)  # Creates a new object of the MostSimilarWord

                        for msw in top_5_words:
                            # If the word is already in the top_5_word do not append it again.
                            # If the cost of it had changed then update the cost of it.
                            if msw.index == new_word.index:
                                appendable = False
                                if msw.cost != new_word.cost:
                                    msw.cost = new_word.cost

                        # If it is had to append to the top_5_words, firstly remove the last item of it.
                        # And then append the new item.
                        if appendable:
                            top_5_words.pop()
                            top_5_words.append(new_word)

                    # It checks if the can_min cost is bigger than the most similar five words costs.
                    if can_min > top_5_words[TOP_FIVE - 1].cost:
                        table[k][0][0] = EXPENSIVE_WORD  # EXPENSIVE_WORD = -1

    percentage_of_used_place = calculate_percentage(used_place_count, total_place)  # Calculate the percentage of used places.
    return top_5_words, percentage_of_used_place  # Returns the most similar five words and the percentage.


# It calculates the percentage of used places of the 3D table.
def calculate_percentage(total_usage, total_place):
    percentage_of_used_place = (total_usage * 100.0) / total_place
    return percentage_of_used_place


# It does initialization of the all first row and all first column of the 3D table.
def table_initialization(table, word_of_file_count):
    for k in range(word_of_file_count):
        for j in range(MAX_LENGTH + 1):
            table[k][0][j] = j
        for i in range(MAX_LENGTH + 1):
            table[k][i][0] = i


# It prints the 3D table based on the 2D table version.
def print_table(table):
    row = len(table)
    for i in range(row):
        print(table[i])


if __name__ == '__main__':
    random_file_names = ["Files/random_file_1.txt", "Files/random_file_2.txt",
                         "Files/random_file_3.txt", "Files/random_file_4.txt",
                         "Files/random_file_5.txt"]
    random_words = read_random_file(random_file_names[4])
    print("======================================================================")
    print("It is an ENHANCED version of minimum edit distance algorithm.")
    print("======================================================================")
    main_word = get_word()
    most_similar_five_words = [MostSimilarWord() for i in range(TOP_FIVE)]
    most_similar_five_words, percentage = min_edit_distance(main_word, random_words, most_similar_five_words)

    print("======================================================================")
    print("The Most Similar Five Words :")

    for msfw in most_similar_five_words:
        msfw.print_msw()

    print("======================================================================")
    print("Percentage of the Table :", percentage)
    print("======================================================================")

    print("======================================================================")
    print("Created by Ali Haydar KURBAN")
    print("======================================================================")
