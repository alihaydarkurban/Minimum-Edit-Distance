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


if __name__ == '__main__':
    random_words = read_random_file()
    print(random_words)
    print(len(random_words))
