import re


def analyse_text(text: str) -> list:
    """
       Analyze text to count letters with and without holes, and identify words with hole letters.

       This function processes input text to:
       1. Remove punctuation characters
       2. Count letters with holes (a, b, d, e, g, o, p, q)
       3. Count letters without holes
       4. Create a dictionary of words with their hole letter counts

       Args:
           text (str): Input text to analyze

       Returns:
           list: A list containing:
               - count_wtht_holes (int): Number of letters without holes
               - cnt_holes (int): Number of letters with holes
               - words_w_holes (dict): Dictionary of words with their hole letter counts
       """
    words_w_holes = {}
    cnt_holes = 0
    all_cnt = 0

    cleaned_text = re.sub(r'[^\w\s]', '', text)
    replacement_text = re.sub(
        r'[abdegopq]', '*', cleaned_text
    )
    words = cleaned_text.split()
    repl_words = replacement_text.split()

    for ind, word in enumerate(repl_words):
        all_cnt += len(word)
        word_cnt = word.count('*')
        if word_cnt != 0:
            words_w_holes[words[ind]] = word_cnt
            cnt_holes += word_cnt

    cnt_wtht_holes = all_cnt - cnt_holes
    result = [cnt_wtht_holes, cnt_holes, words_w_holes]
    return result


def chose_words(parsed_text: list) -> list:
    """
    Select words that contain more than one letter with holes.

    Args:
        parsed_text (list): Output from analyse_text function containing:
            - Count of letters without holes
            - Count of letters with holes  
            - Dictionary of words with hole counts

    Returns:
        list: List of words that have more than one letter with holes
    """
    words = parsed_text[2]
    result = set()

    for word, cnt_letters in words.items():
        if cnt_letters > 1:
            result.add(word)
    return list(result)


if __name__ == '__main__':
    text = input('Enter the text: ')
    parsed_text = analyse_text(text)
    holes_letters = parsed_text[1]
    other_letters = parsed_text[0]
    special_words = chose_words(parsed_text)

    print(f'Number of letters with a hole: {holes_letters}\n'
          f'Number of letters without a hole: {other_letters}\n'
          f'List of words with more than 2 letters with holes: '
          f'{special_words}')
