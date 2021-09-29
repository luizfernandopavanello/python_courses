String Methods

Methods are like some of the functions you have already seen:

    len("this")
    type(12)
    print("Hello world")

These three above are functions - notice they use parentheses, and accept one or more arguments. Functions will be studied in much more detail in a later lesson!

A method in Python behaves similarly to a function. Methods actually are functions that are called using dot notation. For example, lower() is a string method that can be used like this, on a string called "sample string": sample_string.lower().

Methods are specific to the data type for a particular variable. So there are some built-in methods that are available for all strings, different methods that are available for all integers, etc.

Below is an image that shows some methods that are possible with any string.

Each of these methods accepts the string itself as the first argument of the method. However, they also could receive additional arguments, that are passed inside the parentheses. Let's look at the output for a few examples.

>>> my_string.islower()
True
>>> my_string.count('a')
2
>>> my_string.find('a')
3

You can see that the count and find methods both take another argument. However, the .islower() method does not accept another argument.

No professional has all the methods memorized, which is why understanding how to use documentation and find answers is so important. Gaining a strong grasp of the foundations of programming will allow you to use those foundations to use documentation to build so much more than someone who tries to memorize all the built-in methods in Python.
One important string method: format()

We will be using the format() string method a good bit in our future work in Python, and you will find it very valuable in your coding, especially with your print statements.

We can best illustrate how to use format() by looking at some examples:

Example 1

print("Mohammed has {} balloons".format(27))

Example 1 Output

Mohammed has 27 balloons

Example 2

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))

Example 2 Output

Does your dog bite?

Example 3

maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))

Example 3 Output

Maria loves math and statistics

Notice how in each example, the number of pairs of curly braces {} you use inside the string is the same as the number of replacements you want to make using the values inside format().

More advanced students can learn more about the formal syntax for using the format() string method here.

 - Another String Method - Split

Another important string method: split()

A helpful string method when working with strings is the .split method. This function or method returns a data container called a list that contains the words from the input string. We will be introducing you to the concept of lists in the next video.

The split method has two additional arguments (sep and maxsplit). The sep argument stands for "separator". It can be used to identify how the string should be split up (e.g., whitespace characters like space, tab, return, newline; specific punctuation (e.g., comma, dashes)). If the sep argument is not provided, the default separator is whitespace.

True to its name, the maxsplit argument provides the maximum number of splits. The argument gives maxsplit + 1 number of elements in the new list, with the remaining string being returned as the last element in the list. You can read more about these methods in the Python documentation too.

Here are some examples for the .split() method.

    A basic split method:

    new_str = "The cow jumped over the moon."
    new_str.split()

    Output is:

    ['The', 'cow', 'jumped', 'over', 'the', 'moon.']

    Here the separator is space, and the maxsplit argument is set to 3.

    new_str.split(' ', 3)

    Output is:

    ['The', 'cow', 'jumped', 'over the moon.']

    Using '.' or period as a separator.

    new_str.split('.')

    Output is:

    ['The cow jumped over the moon', '']

    Using no separators but having a maxsplit argument of 3.

    new_str.split(None, 3)

    Output is:

    ['The', 'cow', 'jumped', 'over the moon.']

