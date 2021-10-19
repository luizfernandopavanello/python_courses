""" 
Calling the read Method with an Integer

In the code you saw earlier, the call to f.read() had no arguments passed to it. This defaults to reading all the remainder of the file from its current position - the whole file. If you pass the read method an integer argument, it will read up to that number of characters, output all of them, and keep the 'window' at that position ready to read on.

Let's see this in an example that uses the following file, camelot.txt:

We're the knights of the round table
We dance whenever we're able

Here's a script that reads in the file a little at a time by passing an integer argument to .read().

with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

Outputs:

We
're the 
knights of the round table
We dance whenever we're able

You can try out this example by creating your own camelot.txt and example.py files with the text above.

Each time we called read on the file with an integer argument, it read up to that number of characters, outputted them, and kept the 'window' at that position for the next call to read. This makes moving around in the open file a little tricky, as there aren't many landmarks to navigate by.

- Reading Line by Line

\ns in blocks of text are newline characters. The newline character marks the end of a line, and tells a program (such as a text editor) to go down to the next line. However, looking at the stream of characters in the file, \n is just another character. 

Conveniently, Python will loop over the lines of a file using the syntax for line in file. I can use this to create a list of lines in the file. Because each line still has its newline character attached, I remove this using .strip().

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)

Outputs:

["We're the knights of the round table", "We dance whenever we're able"]

Quiz: Flying Circus Cast List

You're going to create a list of the actors who appeared in the television programme Monty Python's Flying Circus.

Write a function called create_cast_list that takes a filename as input and returns a list of actors' names. It will be run on the file flying_circus_cast.txt (this information was collected from imdb.com). Each line of that file consists of an actor's name, a comma, and then some (messy) information about roles they played in the programme. You'll need to extract only the name and add it to a list. You might use the .split() method to process each line.

"""

def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)

    return cast_list

cast_list = create_cast_list('/flying_circus_cast.txt')
for actor in cast_list:
    print(actor)