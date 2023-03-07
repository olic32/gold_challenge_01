def find_todo(str_):

    check = "#TODO"

    has_todo = False

    if type(str_) != str:
        raise Exception("Wrong data type!")
    
    str_ = str_.strip()

    if len(str_) < 5:
        return False
    
    if check in str_:
        has_todo = True



    return has_todo

