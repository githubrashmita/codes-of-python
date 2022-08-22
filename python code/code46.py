with open('data_file.txt') as f:
    content_list = [line for line in f]

print(content_list)

# removing the characters
with open('data_file.txt') as f:
    content_list = [line.rstrip() for line in f]

print(content_list)
