import random

characters = [
  # '□',
  # '■', 
  # '△', 
  # '▲', 
  # '▽', 
  # '▼', 
  # '○', 
  # '●'
  '□', 
  '■', 
  '△', 
  '▲', 
  '⬡', 
  '⬢', 
  '○', 
  '●'
]

line_length = 5
lines_number = 40

generated_text = ""

def create_line(line_length, characters):
  line = ""
  for entry in range(line_length):
    index = random.randint(1, len(characters))
    char = characters[index-1]
    line = line + char + " "
  return line

def create_paragraph(number_of_lines):
  paragraph = ""
  for line in range(lines_number):
    paragraph = paragraph + create_line(line_length, characters)
    paragraph = paragraph + "\n"
    if (line+1)%5 == 0:
      paragraph = paragraph + "\n"
  return paragraph

# print(create_line(line_length, characters))
print(crea)