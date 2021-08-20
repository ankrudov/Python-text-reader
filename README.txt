Starting off i assumed the files would need to be dynamically read and transformed with whatever input is put in.
I will be explaining the function comma_separator; however all functions work the same with the main differences being the replace method inside the first for loop. replacing the comma and pipe respectively.
and the sorting method inside the sorted variables. the comma function uses a lambda function to sort by date and lastname, while the other two use itemgetter to sort by index. 


In a txt file named comma.txt is where the data that will be parsed is contained. 
The code takes the python statement "with open" to open the comma text file.
I created two empty variablle lists : comma_list, and name_list lists to house the data that i would be iterating over.
in the next line we have the variable "comma" that houses the comma.text data using pythons readlines method to parse the data.

The first step in the parse method that i tackled was replacing the commas in the data and adding the left overs to a new list.
FOR I IN COMMA: 
iterates through the txt data, removes the comma and adds the data to the commalist variable.
I ran into an issues that caused all the data to become one string inside their list, making it hard to be able to sort by date. 
To bypass this issues i created a for loop that would iterate through the comma list data and SPLIT() the strings by their spaces, and move them into their own list "name_list". this made each word their own string and made it posible for me to sort by the date.

To ensure the user uses the correct format, i added a for loop that checks the length of the elements inside the lists, and checks if its longer than the allowed elements.. 5 or 6, 
an error will pop up and end the program. 

after that issue was fixed i was able to create another variable named sorted_list that would house the new sorted data using the "sorted method"
This methods goes through the lists and uses a lambda function to name every list "t" then using the imported datetime method, sorts the data in index [4] "assuming that all data will match and be 5 indeces long", then uses predefined code to read the format as m/d/y and sort accordingly.

After sorting the data i still had a list of list that didnt match the wanted output of one string, so for the final variable, out_value i used a list comprehension to JOIN the list of strings with ' ' spaces.
Finally i iterated through the out_value data and displayed the output in the console. 
The code is dynamic and will iterate through any data written inside the comma.txt file as long as it follows the same format as the previous entries.


in order to test the app the user must call the defined functions 
space_separator()
comma_separator()
pipe_separator()

users can add extra elements by updating the txt files and following the correct format using the examples.