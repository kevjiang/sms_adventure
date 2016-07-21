from scrapers import *
from adventure import *
from time import *

def response_handler(body):
    '''
    given text body string input
    If body = "nytimes needle", searches nytimes for needle
    Otherwise plays adventure game
    returns proper response message
    '''
    message = ""

    # prompt for a search of word on NYT
    if "nytimes" in body.split():
        needle = body.split()[1]
        total_nyt_count = nyt_all_text_count(needle)
        message = "%s: nytimes.com homepage currently includes %d mentions of %s" % (strftime("%Y-%m-%d %I:%M:%S"), total_nyt_count, needle)
    elif 'start' == body:
        message = classroom0()
    elif 'take a nap' == body:
        message = take_nap()
    elif 'take notes' == body:
        message = take_notes()
    elif 'turn around' == body:
        message = turn_around()
    elif 'notes' == body:
        message = notes()
    else:
        message = rogue()

    return message