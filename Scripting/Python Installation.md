Before We Install Python:
1. Prepare to Use Command Line

To install Python and follow this lesson, you will need to use the command line. We will walk you through all the details, so don't worry if you have never used it before! If you would like to learn or refresh on command lines, we strongly recommend going through this free Shell Workshop lesson, where you can set up and learn how to use Unix Shell commands.
** Note to Windows Users: Install Git Bash

As noted in the free Shell Workshop linked above, we recommend you install Git Bash here and use this as your terminal for this lesson. Please note that during installation you should select the checkbox Use Git and Optional Unix tools from the Windows Command Prompt. This will allow you to use Unix commands while in Windows. If you'd rather use PowerShell, those commands are also provided in this lesson. For more information on the different command shells, check out the Shell Workshop lesson linked above.
2. Is Python Already Installed On Your Computer?

In this course, we're using the most recent major version of Python - Python 3. Although Python 2 is still being used in many places, it is no longer being updated. In order to keep up compatibility with future improvements to Python, we recommend using Python 3.

Mac OS X and Linux usually come with Python 2 already installed. We DO NOT recommend that you make any changes to this Python, since parts of the operating system are using Python. However, it shouldn't do any harm to your system to install Python 3 separately, too.

Windows doesn't usually come with Python included, but you can still check whether you have it installed before going ahead. So, first, check that you’ve not already got Python 3 installed.

Open up your Terminal or Command Line (this would be Git Bash on Windows).

In a new terminal or command prompt, type

$ python --version

and press Enter.

You might get a response that the Python version installed is something like Python 2.7.9. In that case, it would tell you that you have Python 2 installed, and you'll want to follow the steps in the next couple of sections to update it to Python 3.

If instead the version number starts with a 3, then you already have Python 3 installed! Don't install Python again!

Alternatively, you might see an error message - don't worry about that for now, just try the steps in the next couple of sections.

https://docs.python.org/3/library/