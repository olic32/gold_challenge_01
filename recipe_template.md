# {{PROBLEM}} Function Design Recipe

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.



## 1. Describe the Problem

*** NOTES ***

only 1 argument - the text
1 function - check if contains #TODO
returns True or False depending on whether that exact string is found within the string


## 2. Design the Function Signature

def find_todo(str):
    *takes one argument - returns boolean*

Parameters:
    *One argument - a string (hopefully)*

Returns:
    *True or False - including error if data type is incorrect*

Side Effects:
    *Doesnt return the string, doesnt check if TODO precedes or follows an item, doesnt take into account
    any formatting,*

## 3. Create Examples as Tests

Given a short string with the correct str within:
find_todo("#TODO: Walk the dog") -> True

Given a string that contains the str within other characters etc:
find_todo("What time is it? #TODO - Check your watch!") -> True

Given a poorly formatted string that contains correct string:
find_todo("    #TODO   :    Have lunch     ") -> True

Given an incorrect data type:
find_todo([1,2,3,4,5]) -> False

Given a short string that doesnt contain the correct string:
find_todo("Hello, my name is Ollie") -> False

Givern a string that is too short:
find_todo("L") -> false



## 4. Implement the Behaviour

1st test - failed as function not defined
    *defined function, wrote most code including catches for generic wrong cases*
2nd test - failed on first check - incorrect return due to jumbled code
    *Rewrote the code checking for the correct string to be simpler after testing a different method*
3rd test - passed most except one looking for error exceptions
    *Wrote exception catching code in the test*
4th test - passed all
    *Yay!*
