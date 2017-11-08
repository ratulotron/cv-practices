import random

import sys
script = sys.argv[0]
filename = sys.argv[1]
print("Writing to file " + filename)
# print "The arguments are: " , str(sys.argv)

data = {
  "chars": ["□", "■", "△", "▲", "⬡", "⬢", "○", "●"], #, "▽", "▼"
  "width": 5,
  "blocks": 4
}

class DataGenerator:
  def __init__(self, data):
    self.characters = data["chars"]
    self.width = data["width"]
    self.blocks = data["blocks"]

  def create_row(self):
    return " ".join(random.choices(characters, k=width))

  def create_block(self):
    return "\n".join([create_row(characters) for n in range(5)])

  def create_paragraph(number_of_lines, line_length, characters):
    paragraph = ""
    for line in range(number_of_lines):
      paragraph = paragraph + create_line(line_length, characters)
      paragraph = paragraph + "\n"
      if (line+1)%5 == 0:
        paragraph = paragraph + "\n"
    return paragraph
    

# characters = [ 
#   "□", 
#   "■", 
#   "△", 
#   "▲", 
#   "⬡", 
#   "⬢", 
#   "○", 
#   "●",
#   # "▽", 
#   # "▼"
# ]

# line_length = 5
# number_of_lines = 40

# generated_text = ""

# def create_line(line_length, characters):
#   line = ""
#   for entry in range(line_length):
#     index = random.randint(1, len(characters))
#     char = characters[index-1]
#     line = line + char + " "
#   return line

def create_paragraph(number_of_lines, line_length, characters):
  paragraph = ""
  for line in range(number_of_lines):
    paragraph = paragraph + create_line(line_length, characters)
    paragraph = paragraph + "\n"
    if (line+1)%5 == 0:
      paragraph = paragraph + "\n"
  return paragraph

# print(create_line(line_length, characters))
print(create_paragraph(number_of_lines, line_length, characters))