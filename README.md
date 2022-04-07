## Python Introduction:-
* Python is a powerful, general purpose programming language, interpreter and high level language,it was invented by Guido Van Rossum in 1991.
* He named python after the Show known as"The Monty Python flying circus"
* Python is use for developing websites, software, data analysis and data visualization.

### What can you do with learning Python:
* Data Analysis
* Machine learning
* Automation/ scripting
* Software testing and prototyping

### Keywords and Identifier:-
* Keywords are the reserved keyword in python, they are case sensitive
* There are 33 keywords in Python
* We cannot use keywords as a variable name or function

#### Identifiers:-
* An identifier is a name given to entities like class, functions, variables, etc. It helps to differentiate one entity from another.
* They are combination of both lowercase and uppercase
* Keywords cannot be use as an identifier.

### Statements & Comments:-
* Instructions that a Python interpreter can execute are called statements.
* In Python, the end of a statement is marked by a newline character. But we can make a statement extend over multiple lines with the line continuation character (\).
   ###### Identation:-
   * A code block (body of a function, loop, etc.) starts with indentation and ends with the first unindented line.
   * The enforcement of indentation in Python makes the code look neat and clean.
   ###### Comments:-
   * Comments are very important while writing a program. They describe what is going on inside a program, so that a person looking at the source code does not have a hard time figuring it out.
   * You might forget the key details of the program you just wrote in a month's time. So taking the time to explain these concepts in the form of comments is always fruitful.In Python, we use the hash (#) symbol to start writing a comment.
   * #This is a comment
#print out Hello
print('Hello')
  ###### Multi-line comments:-
  * We can have comments that extend up to multiple lines. One way is to use the hash(#) symbol at the beginning of each line. 
  * eg """This is also a
perfect example of
multi-line comments"""

### Variables:-
* A variable is a named location used to store data in the memory. It is helpful to think of variables as a container that holds data that can be changed later in the program.
* eg . num = 10

##### Constants:-
* A constant is a type of variable whose value cannot be changed. It is helpful to think of constants as containers that hold information which cannot be changed later.
* You can think of constants as a bag to store some books which cannot be replaced once placed inside the bag.

##### Literals:-
* Literal is a raw data given in a variable or constant.

## Data Types:-
1. Numbers
2. List
3. Boolean
4. Tuple
5. Strings
6. Set
7. Dictionary

##### Conversion:-
* The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion.
1. Implicit 
2. Explicit

###### Implicit type conversion:-
* In Implicit type conversion, Python automatically converts one data type to another data type
c = 10.5
type would be float conversion would be int(c)

##### Explicit type conversion:-
* In Explicit Type Conversion, users convert the data type of an object to required data type. We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.
     #### Key Points to Remember:-
     * Type Conversion is the conversion of object from one data type to another data type.
     * Implicit Type Conversion is automatically performed by the Python interpreter.
     * Python avoids the loss of data in Implicit Type Conversion.
     * Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.
     * In Type Casting, loss of data may occur as we enforce the object to a specific data type.

### Operator:-
* Operators are special symbol in python that carry out arithematic or logical computation
   * There are types of operator:-
   1. Arithematic operators
   2. Comparison operators
   3. Logical operators
   4. Membership operators
   5. Bitwise operators
   6. Assignment operators
   7. Identity operators

###### Arithematic operators:
  * a + b
  * a * b
  * a / b
  * a // b
  * a % b

###### Comparison operators:-
   * Comparison operators are used to compare values. It returns either True or False according to the condition.
   * x > y
   * x >= y
   * x < y
   * x <= y
   * x == y
   * x != y

###### Logical operator :
    * Logical operators are the and, or, not operators.
    * x = True
      y = False
      print('x and y is',x and y)
      print('x or y is',x or y)
      print('not x is',not x)
      
###### Bitwise operator:-
     * Bitwise operators act on operands as if they were strings of binary digits
     * for example 2 is 10 in binary and 7 is 111 in binary
     
     * 
