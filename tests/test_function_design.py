from lib.function_designs import *
import pytest



def test_calculate_reading_time():
    test_1 = calculate_reading_time(800)
    test_2 = calculate_reading_time(400.5)

    with pytest.raises(Exception) as e_info:
        test_3 = calculate_reading_time("Hello!")
    
    error_message = str(e_info.value)

    assert test_1 == 4
    assert test_2 == 2.0025
    assert error_message == "Wrong data type!"


def test_grammar_check():
    assert grammar_check("Hello, this sentence is formatted correctly.") == True
    assert grammar_check("   Hello, this sentence is formatted correctly.") == True
    assert grammar_check("Hello, this sentence is formatted correctly.   ") == True
    assert grammar_check("  C    .       ") == True
    assert grammar_check("hello!") == False
    assert grammar_check("Hello") == False
    assert grammar_check("hello. My name is Oliver. I am learning to code") == False
    assert grammar_check("L") == False

    with pytest.raises(Exception) as e_info:
        grammar_check([1,2,3,4,5])
    
    error_info = str(e_info.value)

    assert error_info == "Wrong data type!"

