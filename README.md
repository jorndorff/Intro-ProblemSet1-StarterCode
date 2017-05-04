Problem Set One
================

Written by: Computer Science Department, The Pingry School

Solved by: YOUR NAME HERE

About Problem Sets
------------------
A problem set is a series of classic problems in an introductory programming course. For these exercises, you must write your own functions from scratch. So you may not, for example, import a python function from another module, or use typecasting to make a problem trivial. You will have about a week to complete a problem set, and a small amount of class time to work on the project.


Submission
----------
This problem set will be submitted by pushing to github. Begin by accepting this assignment which will create your own repository. After cloning your repository to your local system, you can start solving the problems. The file structure is already sketched out for you.


Grading
-------
Most of the grade for a problem set will come from automated testing of the code. Examples of automated tests are available to you throughout your development, so if you want to see how your code is doing with the tests, come see me for details.

In this problem set, you must write at least two functions recursively.

|Grade Category | Points Earned|
| --- | --- |
| Automated Tests | 15 pts |
| README and .gitignore files | 2 pts |
| Progressive Commits | 1 pt |
| Coding Style and Readability | 2 pts|

| Grade Penalty | Points Deducted |
| --- | --- |
| No recursive functions | 1 pt each |
| Casting to string in numberic problems | 1 pt each |

The Problems
------------
### get_gcf
Create a function called get_gcf that takes two positive integer arguments. Your function should return an int that is the greatest common factor of the two arguments.

### largest
Create a function called largest that takes in four ints and returns the one that is the largest.

### magic_eight_ball
Create a function called magic_eight_ball that has no parameters and returns a string containing 1 of 9 possible responses to a yes or no question (ex - "Looks Doubtful", "The Answer is Yes", etc). The choice should be selected randomly. You may use the random module, but only the random.random() function. No other functions.

### ascii_name
Look at the following website: http://www.patorjk.com/software/taag/

Create a function called ascii_name that takes in no parameters and returns an ASCII art style representation of your name. If you have a long name and want to use a shorter nickname, that is fine.


### alpha_order
Create a function called alpha_order that takes in two strings as parameters and returns a single string containing both parameters concatenated in alphabetical order, separated by a space. You may use the string functions upper() or lower().

### zip_strings
Create a function called zip_strings that takes two strings as arguments and returns a string that “zips” them together. For example: “Hemingway” and “Faulkner” would become: “HFeamuilnkgnweary”. Note that if one string is longer than the other, its leftover letters are just added to the end.

### every_other
Create a function called every_other that takes in a string parameter and returns a string that is every other character in the original string, starting with the 1st character. For example: every_other(“A Farewell to Arms”) would return the string “AFrwl oAm”.

### count_lower
Create a function called count_lower that takes a string argument and returns the number of lowercase letters that string contains. You may use the isalpha(), islower(), and isupper() methods.

### x_cipher
The secret organization is worried that some of their communications may fall into the wrong hands. They want you to implement an encryption function called x_cipher that will decrypt their secret messages. The function takes a string of the cipher text and returns a string of the plain text.

