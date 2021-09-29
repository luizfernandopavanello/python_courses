Example

    house_number = 13
    street_name = "The Crescent"
    town_home = "Belmont"
    print(type(house_name)) # <class 'int'="">

    address = str(house_number + " " + street_name + ", " + town_name
    print(address) # 13 The Crescent, Belmont

Type and Type Conversion

You have seen four data types so far:

    int
    float
    bool
    string

You got a quick look at type() from an earlier video, and it can be used to check the data type of any variable you are working with.

>>> print(type(633))
int
>>> print(type(633.0))
float
>>> print(type('633'))
str
>>> print(type(True))
bool

You saw that you can change variable types to perform different operations. For example,

"0" + "5"

provides completely different output than

0 + 5

What do you think the below would provide?

"0" + 5

How about the code here:

0 + "5"

Checking your variable types is really important to assure that you are retrieving the results you want when programming.
