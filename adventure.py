from difflib import *

def response_handler(body):
    '''
    given text body string input
    Performs fuzzy matching using difflib
    http://stackoverflow.com/questions/16090060/is-there-a-standard-way-in-python-to-fuzzy-match-a-string-with-arbitrary-list-of
    returns proper response message
    '''
    message = ""

    if get_close_matches('start', [body]):
        message = classroom0()
    elif get_close_matches('take a nap', [body]):
        message = take_nap()
    elif get_close_matches('take notes' ,[body]):
        message = take_notes()
    elif get_close_matches('turn around', [body]):
        message = turn_around()
    elif get_close_matches('notes', [body]):
        message = notes()
    else:
        message = rogue()

    return message

def classroom0():
    return "You are in a boring class.  Do you 'take a nap' or 'take notes'?"

def take_nap():
    return "You fall asleep forever...and ever...and ever.  Do you want to 'start' over?"

def take_notes():
    return "You furiously take notes as the teacher drones on.  Your friend taps you on the shoulder.  Do you 'turn around' or keep looking at your 'notes'"

def turn_around():
    return "You turn around, only to find that you have just stared into the eyes of a basilisk!  Oh well...do you want to 'start' over?"

def notes():
    return "Unfortunately, this game is incomplete...please come back later for more!  Do you want to 'start' over?"

def rogue():
    return "Text a valid command (denoted by single quotes).  Or text 'start' to restart the game."