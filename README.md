

This is a CLI App that acts a ticket viewer for my account. The username and password to contacting the API is already hard-coded in the script as the instructions mentioned that it will be contacting my account, and not any user's account. If you wish to view tickets in a different account you must
a - Change the values of 'username' and 'password' in 'main.py.' to your own.
b - Log into your account, go to Channels>API> Enable Password Access

Pre- requisits:

1 - Make sure to install the requests library as it is needed to contact the API. You can do so by running the command 'pip install requests.'
2 - There is a 'Post_tickets' script in this repository, however it was only included because it was relevant to the project as a whole, it is not needed to run the program, 
as the dummy ticket information was posted to the account when I ran it.
3 - Make sure that the 'ApiErrors.py' file is in the same directory when you run main. This file contains a dictionary that maps to API errorss. This givs details to the user when
we run into API/HTTP Errors.

How to Run: Using CMD, navigate to the directory that contains all files downloaded from this repository. Once you are in the directory, type 'pip3 install requests'. - Make sure you have python downloaded. Finally just type 'python main.py'. Make sure you are in the directory this entire time, and that it contains all folders.

Alternatively, you can run in any IDE that supports Pycharm.


Note: As for the Unit testing aspect. It is not a concept I worked with very much, and I had ran out of time to work on this project; however, I did commit a new main method after learning about unit testing and the importance of writing code that is testable to begin with. I changed some of the code to make it more testable, and then I utilized a unit testing class/framework to test that aspect of the code. Unfortunately,I would have enjoyed transforming my  entire code, but this week has been quite tough, on top of my currnt Internship.
