# String_operations_webservice
Python web service in jinja2 framework to perform various string operations on the inputs supplied

====================
Used the Google AppEngine to host this  Word Processing Application.

Three Web Services for this project

Web Services
============
Google DataStore : 
which is a schemaless NoSQL datastore providing robust, scalable storage for the web application.
Memcache:
If the input given by the user is data which has previously been given by the user, then in such case output is retrieved from the memcache within lesser time. 
Google User Management:
Logging into the application using this service. This application has user login, which is authenticated using Google Account.

Functionality: 
==============
The web application has three Radio buttons 

First Tab (radio button)- Word Processor  :performs the following operations 

1) Palindrome - When a text is entered, the processed message returns all the palindromes in the String.

2) Word Count - For the given input string, the processed message returns the count of the letters excluding the spaces in the String

3) Sort - When the input string is given, the processed message returns the string that sorted with respect to the length of the words

4) Browse - For the entered text, the processed message returns the related urls and information by browsing over the internet

5) Digit - For the String entered, the processed message returns only the number of digits in the string

6) Reverse - For the String entered, the processed message returns the reverse of the string

Second Tab (radio button) - Advanced Operations contains the Compare function

Compare - When two paragraphs are entered, the processed message returns the differences between the two paragraphs

Merge - This function merges two paragraphs and displays the output

Third tab (radio button) contains History.

This feature uses Google Datastore to retrieve the data entered in the Text Box.

Usage:
=============
Login to the application using gmail credentials

select first tab, word processor

Enter the text and select one of the operations from the drop down box

click process, and the ouput is displayed below it

In the advanced processor tab, enter two paragraphs and click one of the function from drop down

Navigate to History tab to view the history of entered paragraphs.

Future Work - 
Plans to implement Image processor with functionality to edit the images and to store data on the images.
