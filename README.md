# Spellcheck Exercise

This repository uses the code and data set from
https://norvig.com/spell-correct.html (with minor modifications).

## Introduction
This set of exercises is intended to introduce students to a detailed analysis
of a small-sized computer program. The goal of the exercise is to teach the
students how to follow the flow of the program in order to understand what is
happening in each step of the execution. Consequently, this will enable the
students to reason about potential weaknesses or flaws in the program.

Begin by reading the introductory section and the “How It Works: Some
Probability Theory” at https://norvig.com/spell-correct.html. Do not be troubled
if you find some parts of the text difficult to understand. While it would be
commendable to study external resources in order to fully understand the text it
is not required. Rather, be careful not to get stuck!

## Environment
If you do not have [Python](https://www.python.org/) on your machine install it.
Clone this repository onto your machine and open it with your favorite IDE (if
you do not have one consider [PyCharm](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)).

## Exercises
Answer the questions below (they are meant to be answered in the order in which
they are asked):

1. Think about what a spellchecking program in general does and briefly
explain in your own words. In addition:

    1. Briefly explain how you think a spellchecker should behave if it
    sees a perfectly correct word.
    
    2. What should spellchecker ideally do in case it sees an incorrect word?
    
    3. What does it mean for a word to be correct or incorrect?
    
2. Open the `spellcheck.py` file. Two modules are imported for use in the
spelling program – `re` and
`collections` (the `Counter` class). The first one is a collection of classes
and functions supporting the use of regular expressions. The second one offers a
couple of advanced data containers such as the `Counter`. Find the documentation
for the collections module and understand what the `Counter` class does. Explain
what the expected input to the class constructor `Counter(input)` is and what is
the expected output.

3. Look at the `words` function and understand how it works. Suppose we input
the following short text into the function (show the exact output the function
will return):
    > All opinions are subject to modification and technical correction prior to
official publication in the Connecticut Reports and Connecticut Appellate
Reports.

4. With the understanding of the `Counter` class and the `words` function
explain what happens when the `WORDS` variable is initialized.

5. Once again looking at the `WORDS` variable what do you think is its role
in the context of the whole program?

6. How does the `known` function work? What does it expect on the input and
what does it provide as an output?

7. The `edits1` function is probably the most complicated piece of the code. The
assignment of the `letters` variable is straightforward. Understanding the rest
will likely require a bit of effort:

    1. Understand what happens at the line where the `splits` variable is being
    instantiated. Assuming we input the word “artificial” into the `edits1`
    function show what exact data the `splits` variable will hold?
    
    2. Understand what happens at the line where the `deletes` variable is being
    instantiated. Assuming we take the output you arrived at in the previous
    subquestion (7.i) show what exact data will the variable `deletes` hold. In
    the context of the whole code why do you think this data is useful?
    
    3. Understand what happens at the line where the `transposes` variable is
    being instantiated. Assuming we take the output you arrived at in the
    subquestion 7.i show what exact data the variable `transposes` will hold.
    In the context of the whole code why do you think this data is useful?
    
    4. Understand what happens at the line where the `replaces` variable is
    being instantiated. Assuming we take the output you arrived at in the
    subquestion 7.i show the first 10 elements of the exact data that the
    variable `replaces` holds. In the context of the whole code why do you think
    this data is useful? Referring back to the `letters` variable how does the
    method work with respect to the words that contain other letters than the
    standard English set of 26 characters. How could one solve this deficiency?
    What could be a possible problem if the set of characters we use would be
    really large (say, several millions)?
    
    5. Understand what happens at the line where the `inserts` variable is being
    instantiated. Assuming we take the output you arrived at in the previous
    subquestion (7.i) show the first 10 elements of the exact data that the
    variable `inserts` hold. In the context of the whole code why do you think
    this data is useful? Referring back to the letters variable how does the
    method work with respect to the words that contain other letters than the
    standard English set of 26 characters.
    
    6. Given your answers to the previous subquestions (7.i – 7.v) explain what
    is going to be the output of the `edits1` function.
    
8. Explain how the function `edits2` works. What does it expect as an input
and what does it provide as an output?

9. Explain how the function `candidates` works. What does it expect as an
input and what does it provide as an output?

10. Explain how the function `correction` works. What does it expect as an input
and what does it provide as an output? *HINT: Focus on the optional `key` argument
in the `max` function.*

11. Run the program (i.e., the `correction` function) using the file
`./data/big.txt` to instantiate the `WORDS` variable for the below words.
Indicate when the ideal output is obtained and when not.

    1. advrnture (ideally returns “adventure”)
    
    2. copyrlght (ideally returns “copyright”)
    
    3. litogation (ideally return “litigation”)
    
    4. colusion (ideally returns “collusion”)
    
    5. amlcus (ideally returns “amicus”)
    
    6. caselpad (ideally returns “caseload”)

12. What is the reason for not getting the ideal output for some of the
words in question 11? How could one eliminate or mitigate the issue?

13. Are we guaranteed to get the ideal output for the words where the issue
we identified in question 12 does not exist?

14. Open the `tests.py` file. The `unit_tests` function makes an extensive
use of the `assert` statement? What does the statement do?

15. Explain what is being tested by the first 9 tests (`assert` statements) in
the `unit_test` function. Then explain what is being tested by the following 8
tests (separate explanation for each).

16. Run the `unit_test` function. Did all the tests pass? How did you determine
that? What does it mean if all the tests pass?

17. Elaborate on what role functions like the `unit_tests` could play in
programming?