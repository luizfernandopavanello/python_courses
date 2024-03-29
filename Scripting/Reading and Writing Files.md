Reading and Writing Files

To follow along with the example above, create a new file in Atom, copy the following text into it, and save it as some_file.txt!

Hello!!

You've read the contents of this file!

Here's how we read and write files in Python.
Reading a File

f = open('my_path/my_file.txt', 'r')
file_data = f.read()
f.close()

    First open the file using the built-in function, open. This requires a string that shows the path to the file. The open function returns a file object, which is a Python object through which Python interacts with the file itself. Here, we assign this object to the variable f.
    There are optional parameters you can specify in the open function. One is the mode in which we open the file. Here, we use r or read only. This is actually the default value for the mode argument.
    Use the read method to access the contents from the file object. This read method takes the text contained in a file and puts it into a string. Here, we assign the string returned from this method into the variable file_data.
    When finished with the file, use the close method to free up any system resources taken up by the file.

Writing to a File

f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()

    Open the file in writing ('w') mode. If the file does not exist, Python will create it for you. If you open an existing file in writing mode, any content that it had contained previously will be deleted. If you're interested in adding to an existing file, without deleting its content, you should use the append ('a') mode instead of write.
    Use the write method to add text to the file.
    Close the file when finished.

Too Many Open Files

Run the following script in Python to see what happens when you open too many files without closing them!

files = []
for i in range(10000):
    files.append(open('some_file.txt', 'r'))
    print(i)

With

Python provides a special syntax that auto-closes a file for you once you're finished using it.

with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()

This with keyword allows you to open a file, do operations on it, and automatically close it after the indented code is executed, in this case, reading from the file. Now, we don’t have to call f.close()! You can only access the file object, f, within this indented block.
