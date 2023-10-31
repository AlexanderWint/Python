"""
Module holds the functions responsible for the calculations and
comparasions between txt output & user input
"""
import getters_setters as gtst


def wrd_char_analyzer():
    """
    Carries out the calculations and analyzing the differences between the .txt file & user input.
    Returns the number of words that's incorrect and a dict that keeps the incorrect characters
    """
    lines_txt = gtst.get_lines()
    lines_usr = gtst.get_usr_inp()
   
    score_words_counter = 0
    score_char_counter = 0
    char_dict = {}

    for item_line_txt, item_line_usr in zip(lines_txt, lines_usr):
        words_txt = item_line_txt.split()
        words_usr = item_line_usr.split()
        if len(words_txt) > len(words_usr):
            while len(words_txt) > len(words_usr):
                words_usr.append(" ")
        if len(words_txt) < len(words_usr):
            score_words_counter += len(words_usr) - len(words_txt)
            extra_words = words_usr[len(words_txt):]
            for word in extra_words:
                score_char_counter += len(word)

        for word_txt, word_usr in zip(words_txt, words_usr):
            if word_txt != word_usr:
                score_words_counter += 1

                char_txt = list(word_txt)
                char_usr = list(word_usr)
                if len(char_txt) > len(char_usr):
                    while len(char_txt) > len(char_usr):
                        char_usr.append(" ")
                if len(char_txt) < len(char_usr):
                    extra_chars = char_usr[len(char_txt):]
                    for char in extra_chars:
                        score_char_counter += 1

                for char_t, char_u in zip(char_txt, char_usr):
                    if char_t != char_u:
                        score_char_counter += 1
                        if char_t not in char_dict:
                            char_dict[char_t] = 1
                        else:
                            char_dict[char_t] += 1

    return score_words_counter, score_char_counter, char_dict


def calc_prec(wrds, chars, char_dict):
    """
    Function performs calculations for word precision, character precision,
    and sort the misspelled character - dict
    """

    total_wrds = gtst.get_wrds()
    total_chars = gtst.get_chars()
    dict_sorted = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))

    wrd_precision = round(100*(total_wrds - wrds) / total_wrds,2)
    wrd_precision =  max(wrd_precision,0)
    char_precision = round(100*(total_chars - chars) / total_chars,2)
    char_precision = max(char_precision,0)
    
    return wrd_precision, char_precision, dict_sorted


def print_form(wrds, chars, char_dict):
    """
    Function used to format the output that's given to the main module
    """
    str_out=(f"\nOrdprecision: {wrds}% \nTeckenprecision: {chars}% \nFelstavade tecken: ")
    for key, value in char_dict.items():
        str_out+=f"\n{key}: {value}"
    str_out += "\n"
    
    return str_out
