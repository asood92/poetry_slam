import random


def get_file_lines(filename):
  poem_file = filename
  poem = open(poem_file, "r")
  poem_lines = poem.readlines()
  return poem_lines

def lines_printed_backwards(lines_list):
  count = len(lines_list)
  while count >= 0:
    print(count+1,lines_list[count-1])
    count -= 1

def lines_printed_random(lines_list):
  for i in range(len(lines_list)):
    random_line = random.randint(0,len(lines_list)-1)
    print(lines_list[random_line])

def lines_printed_custom(lines_list)


def main():
  poem_lines = get_file_lines("poem.txt")
  lines_printed_backwards(poem_lines)
  lines_printed_random(poem_lines)

main()