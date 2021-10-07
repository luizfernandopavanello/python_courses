"""
Text file handling

Use the Python's open() method to read the latin-lipsum.txt text file. Store it in a file variable.

After that:

    Calculate the total lines within that file and store the result in the file_lines variable.
    Calculate the total words within that file and store the result in the file_words variable.

    Warning! don't count empty lines (\n)

"""

file_lines = None
file_words = None 

with open('latin-lipsum.txt', mode='r') as file:
    lines_count = 0
    words_count = 0
    
    for line in file:
        if line != '\n':
            lines_count += 1
            words_count += len(line.split())
            
    file_lines = lines_count
    file_words = words_count
    
print(f'Lines on file: {file_lines}')
print(f'Words no file: {file_words}')
    
         
