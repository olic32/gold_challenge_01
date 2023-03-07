#As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

def calculate_reading_time(text_length):

    if type(text_length) != int and type(text_length) != float:
        raise Exception("Wrong data type!")

    return text_length / 200

def grammar_check(text):

    if type(text) != str:
        raise Exception("Wrong data type!")

    text = text.strip()

    has_caps = False
    has_punc = False
    valid_punctuation = "!.?"

    if len(text) == 1:
        return False
    
    first_char = text[:1]
    last_char = text[-1:]

    if first_char == first_char.upper():
        has_caps = True
    
    for i in valid_punctuation:
        if i == last_char:
            has_punc = True
    

    
    if has_caps and has_punc:
        return True
    else:
        return False

