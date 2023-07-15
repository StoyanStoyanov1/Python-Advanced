import re


def read_searched_words(file_path):
    searched_words = []
    with open(file_path) as file:
        searched_words = file.read().split()

    return searched_words


def calculate_words_count(searched_words_file_path, searched_words):
    words_count = {}
    with open(searched_words_file_path) as file:
        text = file.read()
        for word in searched_words:
            pattern = fr"\b{word}\b"
            count = len(re.findall(pattern, text, re.IGNORECASE))
            words_count[word] = count

    return words_count


def store_result(output_file_path, result):
    with open(output_file_path, "w") as file:
        sorted_result = sorted(result.items(), key=lambda x: -x[1])
        for key, value in sorted_result:
            file.writelines(f"{key} - {value}\n")


searched_words = read_searched_words("words.txt")
words_count = calculate_words_count("input.txt", searched_words)
result = store_result("output.txt", words_count)
