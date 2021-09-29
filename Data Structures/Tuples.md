Tuples

Examples

    AngkorWat = (13.4125, 103.866667)

    print(type(AngkorWat))
    # <class 'tuple'="">

    print("AngkorWat is at latitude: {}".format(AngkorWat[0]))
    # AngkorWat is at latitude: 13.4125

    print("AngkorWat is at longitude: {}".format(AngkorWat[1]))
    # AngkorWat is at longitude: 103.866667

- A tuple is another useful container. It's a data type for immutable ordered sequences of elements. They are often used to store related pieces of information. Consider this example involving latitude and longitude:

location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

Tuples are similar to lists in that they store an ordered collection of objects which can be accessed by their indices. Unlike lists, however, tuples are immutable - you can't add and remove items from tuples, or sort them in place.

Tuples can also be used to assign multiple variables in a compact way.

dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

The parentheses are optional when defining tuples, and programmers frequently omit them if parentheses don't clarify the code.

In the second line, three variables are assigned from the content of the tuple dimensions. This is called tuple unpacking. You can use tuple unpacking to assign the information from a tuple into multiple variables without having to access them one by one and make multiple assignment statements.

If we won't need to use dimensions directly, we could shorten those two lines of code into a single line that assigns three variables in one go!

length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))

 - Tuples are ordered and immutable