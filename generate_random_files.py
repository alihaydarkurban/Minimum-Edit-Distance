import random

DATASET_WORDS = 1140208  # It is the number of words that dataset has.
RANDOM_FILE_WORDS = 1000  # It is the number of words that random file has.


# This function is for generating random numbers.
# These random numbers represent the line number for random words.
def generate_random_line_numbers():
    random_list = random.sample(range(0, DATASET_WORDS), RANDOM_FILE_WORDS)  # Random sampling without replacement.
    random_list.sort()
    return random_list


# This function is for generating five random files from the main dataset.
# The main dataset is .../Files/dataset.txt
# The five random files are .../Files/random_file_1.txt
#                           .../Files/random_file_2.txt
#                           .../Files/random_file_3.txt
#                           .../Files/random_file_4.txt
#                           .../Files/random_file_5.txt
def generate_random_files():
    file_dataset = open("Files/dataset.txt", "r", encoding='utf8')
    file_names = ["Files/random_file_1.txt", "Files/random_file_2.txt", "Files/random_file_3.txt",
                  "Files/random_file_4.txt", "Files/random_file_5.txt"]

    # This loop is for generating five random files.
    for i in range(len(file_names)):
        file_dataset.seek(0, 0)  # Sets the file's current position to the beginning.
        dataset_read_line = file_dataset.readlines()
        line_number = 0
        exit_file_reading = 0
        random_line_numbers = generate_random_line_numbers()
        random_file = open(file_names[i], "w", encoding='utf8')

        # It reads random 1000 words from the dataset.txt
        # and writes back to the random_files_X.txt.
        for line in dataset_read_line:
            if line_number in random_line_numbers:
                exit_file_reading = exit_file_reading + 1
                random_file.write(line)

            line_number = line_number + 1

            # It controls that if the number of reading words reach 1000.
            if exit_file_reading >= len(random_line_numbers):
                random_file.close()
                break

    file_dataset.close()


if __name__ == '__main__':
    print("Random files generation can take a long time...")
    # Random files are generated. Do not need to run it again.
    # generate_random_files()
    print("Random files generation is over. Please check the \"Files\" directory.")
