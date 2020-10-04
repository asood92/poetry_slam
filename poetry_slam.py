# This program reads in a poem from a text file and prints it backwards, then randomly, and lastly prints only even numbered lines - with each odd line being a randomly selected one instead of the original line
import random

# basic file IO for access
def get_file_lines(filename):
  poem = open(filename, "r")
  poem_lines = poem.readlines()
  return poem_lines

def lines_printed_backwards(lines_list):
  # iterate through the list, and print, decrementing from the last element to  -1 (not included)
  for i in range(len(lines_list)-1, -1, -1):
    print(i+1,lines_list[i])

def lines_printed_random(lines_list):
  # loop to print the whole poem
  for i in range(len(lines_list)):
    # randomly select a line between element 0 and the last element, then print
    random_line = random.randint(0,len(lines_list)-1)
    print(lines_list[random_line])


def lines_printed_custom(lines_list):
  # loop to print the whole poem
  for i in range(len(lines_list)):
    # print only even lines
    if i % 2 == 0:
      print(lines_list[i])
    # on each odd line, print a randomly selected line from the poem instead of the original line
    else:
        random_line = random.randint(0,len(lines_list)-1)
        print(lines_list[random_line])


def main():
  poem_lines = get_file_lines("poem.txt")
  lines_printed_backwards(poem_lines)
  lines_printed_random(poem_lines)
  lines_printed_custom(poem_lines)

main()