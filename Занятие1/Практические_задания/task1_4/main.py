def task(words: list) -> list:
    #[word.upper() for word in words]
    return list(map(str.upper, words))  # TODO перевести слова в верхний регистр c помощью map


if __name__ == "__main__":
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    print(task(list_words))
