# Launchpad Game List for Memory Sequence.
# Last edited 12th July, 1pm
# Latest Changes: Entire sequence modified

import B3S2_FunctionStorage as fs

def easy_add_left():
    global easy_level_input
    easy_level_input.append("L")
    print (easy_level_input)

def easy_add_right():
    global easy_level_input
    easy_level_input.append("R")
    print (easy_level_input)

def hard_add_left():
    global hard_level_input
    hard_level_input.append("L")
    print(hard_level_input)

def hard_add_right():
    global hard_level_input
    hard_level_input.append("R")
    print(hard_level_input)

def hard_add_front():
    global hard_level_input
    hard_level_input.append("F")
    print(hard_level_input)

def hard_add_back():
    global hard_level_input
    hard_level_input.append("B")
    print(hard_level_input)

def easy_level_submit():
    if easy_level_input == easy_level_answer:
        print('You win! (Easy)')
        fs.SEQ_Win()
    else:
        print('You us lose')
        fs.SEQ_Lose()

def hard_level_submit():
    if hard_level_input == hard_level_answer:
        print('You win! (Hard)')
        fs.SEQ_Win()
    else:
        print('U are lose')
        fs.SEQ_Lose()

easy_level_input = [] # Left, right (5L, 3R, 5L, 5R)
easy_level_answer = ['L', 'L', 'L', 'L', 'L', 'R', 'R', 'R', 'L', 'L', 'L', 'L', 'L', 'R', 'R', 'R', 'R', 'R'] 
hard_level_input = [] # Left, right, up, down (4F, 3B, 4R, 5L, 7F, 6B)
hard_level_answer = ['F', 'F', 'F', 'F', 'B', 'B', 'B', 'R', 'R', 'R', 'R', 'L', 'L', 'L', 'L', 'L', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'B', 'B', 'B']