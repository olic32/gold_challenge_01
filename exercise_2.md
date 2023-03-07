# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

*** NOTES ***

Will require 1 argument: the text itself. 
Two checks, one of which checks the first letter of the string is caps, the other checks the final element is a punctuation

Will be required to take note of spaces at start and end of string

## 2. Design the Function Signature

def grammar_check(text):
    *Takes the text - 

Parameters: 
    *text - string type, all the text

Returns:
    *returns either a true, or a desciption of the issue and a false. so a boolean and a print. Or an error message if data type wrong(and a false)

Side effects:
    * needs to always return a boolean - even if a error is thrown, still needs to throw false?



## 3. Create Examples as Tests

***A sentence that starts with caps, ends with punctuation with no spaces at start or end.***

grammar_check("Hello, this sentence is formatted correctly.") -> True

***A sentence that starts or ends with a space.***

grammar_check("   Hello, this sentence is formatted correctly.") -> True
grammar_check("Hello, this sentence is formatted correctly.   ") -> True
grammar_check("  C    .       ") -> True

***A sentence that starts with lower caps, or doesn't end with punctuation***

grammar_check("hello!") -> False
grammer_check("Hello") -> False

***A sentence with suitable punctuation and caps within, but not at the ends***

grammar_check("hello. My name is Oliver. I am learning to code") -> False

***Incorrect data type***

grammar_check([1,3,5,6,7]) -> False

***If length of string is only 1, it cannot be valid***

grammar_check("L") -> False


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

