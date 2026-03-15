# Day 2 Log

## Goal
- Become comfortable enough to read beginner-level Python code without freezing

## What I reviewed
- variables
- lists
- dictionaries
- functions
- loops
- if statements
- importing libraries
- reading and writing files

## What I practiced
- looping through a list
- counting word frequency in a sentence
- writing a function
- reading a text file
- saving results to a file

## Baekjoon problems I did
- 2557 — Hello World
- 1000 — A+B
- 1001 — A-B
- 2741 — Print N
- 2438 — Print Stars 1
- 10871 — Numbers smaller than X
- 1152 — Word Count
- 10808 — Alphabet Count

## What worked
- I reviewed the basic Python building blocks in a clear order
- I typed and ran simple examples instead of only reading them
- I got more used to how `input()` works in Baekjoon
- I practiced reading numbers from one line with `input().split()`
- I used loops and `if` statements in simple problems
- I used `split()` to count words
- I read and wrote basic files with `open(..., "r")` and `open(..., "w")`
- I finished all Day 2 exercises

## What felt hard
- Baekjoon input format was confusing at first
- I mixed up numbers, indexes, and actual characters
- I did not always know whether input was on one line or multiple lines
- I got confused about why some code caused runtime errors
- I did not understand `ord()` at first

## What I fixed / learned from mistakes

### A+B / A-B input
- I first tried reading numbers with `input()` twice
- That failed because the problem gives two numbers on one line
- I learned to use:

```python
A, B = map(int, input().split())