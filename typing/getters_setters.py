"""
Module used to retrieve and give info from and to .txt files.
Also to handle user input data.
Also to format this info & to make it ready for calculations.
"""

import calculations as cl

current_filename = ""       

def readfile():
    """
    function used to read a .txt file
    """
    try:
        with open(current_filename, encoding='utf-8') as filehandle:
            content = filehandle.read()
        return content
    except FileNotFoundError:
        return (f"File {current_filename} not found.")
    
def change_file(filename):
    """
    function used to change the file that's beeing read by readfile()
    """
    filename = filename.lower()
    global current_filename

    file_list = ["easy.txt", "medium.txt", "score.txt" ,"hard.txt"]
    #Behövs inte egentligen då jag har hårdkodat vad som skickas
    #som argument till funktionen change_file(X)
    if filename in file_list:
        current_filename = filename

def get_lines():
    """
    Returns list of lines from file given by readfile()
    """
    lines_ = readfile().split("\n")

    return lines_

def get_wrds():
    """
    gets the number of words from the current .txt file , returns an int
    """
    temp = readfile().split()
    length = len(temp)
    return length

def get_chars():
    """
    get the number of chars from the current .txt file, returns an int
    """
    temp = readfile()
    lenght = 0
    for char in temp:
        if char != " " and char != '\n':
            lenght +=1
    return lenght


def get_usr_inp():
    """
    gets the user input and stores it for analyze (?)
    """
    lines_ = get_lines()
    usr_inp = []

    for item in lines_:
        print(item)
        user_inp = input("")
        usr_inp.append(user_inp)
    return usr_inp

def get_usr_name():
    try:
        user_inp =input("Enter username to add to highscore:\n")
        user_inp = user_inp.strip()
        if user_inp:
            return user_inp
        else:
            print("Username cannot be blank, try again")
    except Exception as e:
        print(f"Error: {e} Please enter a valid username")

def set_scoreboard (calced_data):
    """
    responsible for adding the scores to the score.txt file
    """
    usrname = get_usr_name()
    wrd_prec, _, _ = calced_data

    with open("score.txt", "a") as file:
        file.write(f"{usrname:<10}{wrd_prec:10}\n")     # Makes the .txt file easily readable

def lvl_selector(user_inp):
    """
    calls all relevant functions to collect the data for the option selected in the main menu
    Responsible for user choice in main.
    """
    change_file(user_inp)
    analyzed_data = cl.wrd_char_analyzer()
    calc_data = cl.calc_prec(*analyzed_data)
    print(cl.print_form(*calc_data))
    set_scoreboard(calc_data)
    return 

def see_scores(file_inp):
    """
    Function used to return the contents of the score.txt
    """
    change_file(file_inp)
    scores = {}
    str_outp = ""

    for line in readfile().splitlines():
        parts = line.split()
        if len(parts) >= 2:
            key = " ".join(parts[:-1])
            value = float(parts[-1])
            scores[key] = value

    sorted_scores = dict(sorted(scores.items(), key = lambda item: item[1], reverse = True))
    
    for key, value in sorted_scores.items():
        str_outp += f"{key:<10} {value}\n"

    return str_outp

    