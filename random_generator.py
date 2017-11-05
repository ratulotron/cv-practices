import random

characters = [
  '□',
  '■', 
  '△', 
  '▲', 
  '▽', 
  '▼', 
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

# print(create_line(line_length, characters))

paragraph = ""
for line in range(lines_number):
  paragraph = paragraph + create_line(line_length, characters)
  paragraph = paragraph + "\n"

print(paragraph)
  

# for line in lines_number:
#   for entry in line_length:
#     generated_text