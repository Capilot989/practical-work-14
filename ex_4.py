import re


def create_words_list(text: str) -> list:
    """
    Create a list of unique words from input text by removing punctuation.

    Args:
        text (str): The input text to process

    Returns:
        list: A list of words with punctuation removed
    """
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    words_list = list(set(cleaned_text.split()))
    return words_list


if __name__ == '__main__':
    text = input('Enter the text: ')
    print(create_words_list(text))
