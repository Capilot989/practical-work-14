import re


def sort_text() -> list:
    """
        Process input text and return words sorted by frequency and occurrence order.

        This function reads multiple lines of text from standard input until an empty
        line is encountered. It processes the text by:
        1. Removing all punctuation characters
        2. Converting words to lowercase
        3. Counting word frequencies while preserving first occurrence order
        4. Sorting words by descending frequency, then by first appearance

        Args:
            None

        Returns:
            List: A list of words sorted by frequency and
                  first appearance order for words with equal frequency
        """
    words = {}
    order = []

    while True:
        line = input()
        if line == '':
            break

        clean_string = re.sub(r'[^\w\s]', '', line)
        line_words = clean_string.split()

        for word in line_words:
            word_lower = word.lower()
            if word_lower not in words:
                order.append(word_lower)
                words[word_lower] = 0
            words[word_lower] += 1

    sorted_words = sorted(order, key=lambda w: words[w], reverse=True)
    return sorted_words


if __name__ == '__main__':
    for word in sort_text():
        print(word)
