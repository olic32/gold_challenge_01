# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem


As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

*** NOTES ***

Will require 1 thing only - the length of the text. Function will then divide by 200, which will evaluate the minutes required.


## 2. Design the Function Signature

def calculate_reading_time(text_length):
    *All we need is the length of the text. The reading speed is given ***

Parameters: 
    *text_length - an integer

Returns:
    *an integer or float

Side effects:
    *will return in decimals. for example, 1 minute and 30 secs will not return as 1:30, but instead 1.5. May be clearer to convert into a time and seconds
    *no accounting for errors if other input is recieved. Will also need to return an error if this occurs




## 3. Create Examples as Tests

Given a integer of any size
It returns a number, that may or may not be a decimal, which accounts for minutes taken to read

calculate_reading_time(800) -> 4

Given a float of any size
It returns, again, a float or int. However, the answer would clearly be in response to a error, as no word is a decimal point long

calculate_reading_time(400.5) -> 2.0025

Given any other data type
It will return an error

calculate_reading_time("Hello!") -> Error message






## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

