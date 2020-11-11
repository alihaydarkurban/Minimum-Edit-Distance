import random
DATASET_WORDS = 1140208
RANDOM_FILE_WORDS = 1000


def generate_random_line_numbers():
    random_list = random.sample(range(0, DATASET_WORDS), RANDOM_FILE_WORDS)  # random sampling without replacement
    random_list.sort()
    return random_list


def generate_random_files():
    file_dataset = open("Files/dataset.txt", "r", encoding='utf8')
    file_names = ["Files/random_file_1.txt", "Files/random_file_2.txt", "Files/random_file_3.txt",
                  "Files/random_file_4.txt", "Files/random_file_5.txt"]

    for i in range(len(file_names)):
        file_dataset.seek(0, 0)
        dataset_read_line = file_dataset.readlines()
        line_number = 0
        exit_file_reading = 0
        random_line_numbers = generate_random_line_numbers()
        random_file = open(file_names[i], "w", encoding='utf8')

        for line in dataset_read_line:
            if line_number in random_line_numbers:
                exit_file_reading = exit_file_reading + 1
                random_file.write(line)

            line_number = line_number + 1

            if exit_file_reading >= len(random_line_numbers):
                random_file.close()
                break

    file_dataset.close()


if __name__ == '__main__':
    print("Random files generation can take a long time...")
    # generate_random_files()
    print("Random files generation is over. Please check the \"Files\" directory.")