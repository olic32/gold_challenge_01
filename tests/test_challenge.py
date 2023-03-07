from lib.challenge import *
import pytest

def test_challenge_function():
    assert find_todo("#TODO: Walk the dog") == True
    assert find_todo("What time is it? #TODO - Check your watch!") == True
    assert find_todo("    #TODO   :    Have lunch     ") == True

    with pytest.raises(Exception) as e_info:
        find_todo([1,2,3,4,5])
    
    error_message = str(e_info.value)


    assert error_message == "Wrong data type!"
    assert find_todo("Hello, my name is Ollie") == False