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
       1. '&' meaning 'and' operator in this both value should be True or 
       False(0000 1010)and(0000 0100) is(0000 0000)
       2. '|' meaning 'or' operator in this atleast one value should be 
       true (0000 1010)or(0000 0100) is(0000 1110)
       3. '-' meaning 'not' operator in this true value shows as 
       false(0000 1010)not is(1111 0101)
       4. '^' meaning 'XOR' operator in this if one value is 0 and 1 
       then the output would be 1 i.e. (0000 1110)
       5. '>>' meaning 'Bitwise right shift' in this 
       x>>2=2(0000 0010)
       6. '<<' meaning 'Bitwise left shift' in this 
       X<<2 = 40(0010 1000)

###### Assignment operator:-
     * It is use to assign values to variables.
     * like a = 5 can be written as a += 5
       1. '+' is 'a += 5'
       2. '*' is 'a *= 5'
       3. '/' is 'a/=5'
       4. '%' is 'a%=5'
       5. '//=' is 'a//=5'
       6. '**=' is 'a**=5'
 
###### Identity Operator:-
     *  This operator is used to check if two values (or variables) are located on 
     the same part of the memory. Two variables that are equal does not imply that they are identical.
     * The operators are declared as 'is' and 'is not'
       1. 'is' means if operators are identical then it returns as true value
       2. 'is not' means if operators are not identical then it returns as false value
         
###### Membership operators:-
     * Membership operator are used to test whether a value or variable is found in a sequence
     (string, list, tuple, set and dictionary) or not
     * The operators are declared as 'in' and 'not in'
        1. 'in' means that the value is available in the list
        2. 'not in' means the value is not available in the list
        
## Python Flow Control:-

   ##### if... else statement:-
       * Decision making is required when we want to execute a code only 
       if a certain condition is satisfied.
       * syntax: if test expression:
                     statement(s)
       * In Python, the body of the if statement is indicated by the indentation. 
       The body starts with an indentation and the
       first unindented line marks the end.
       * syntax:
          if test expression:
          Body of if
          else:
          Body of else
 #### if...elif...else Statement:-
         * The elif is short for else if. It allows us to check for multiple expressions.
         * The if block can have only one else block. But it can have multiple elif blocks.
 #### Python Nested if statements:-
         * We can have a if...elif...else statement inside another if...elif...else statement. This is called nesting
           in computer programming.
           
 ## For loop:-
      * The for loop in Python is used to iterate over a sequence (list, tuple, string) or
         other iterable objects. Iterating over a sequence is called traversal.
      * syntax:
            for val in sequence:
            loop body
   #### range function:
         * We can generate a sequence of numbers using range() function
         * We can also define the start, stop and step size as range(start, stop,step_size). 
            step_size defaults to 1 if not provided
         *   print(list(range(2, 8)))
               print(list(range(2, 20, 3))
   #### While loop:-
         * The while loop in Python is used to iterate over a block of code as long as the test expression (condition)
            is true.
         * We generally use this loop when we don't know the number of times to iterate beforehand.
         * syntax: while test_expression:
                     Body of while
  #### break and continue:-
         * In Python, break and continue statements can alter the flow of a normal loop.
         * Loops iterate over a block of code until the test expression is false, but
            sometimes we wish to terminate the current iteration or even the whole loop without checking test expression.
         * The break and continue statements are used in these cases.
         * continue statement is used to skip the rest of the code inside a loop for the current iteration only.
            Loop does not terminate but continues on with the next iteration.
  #### pass:-
         * In Python programming, the pass statement is a null statement.
         * The difference between a comment and a pass statement in Python is 
            that while the interpreter ignores a comment entirely, pass is not ignored.
         * However, nothing happens when the pass is executed. It results in no operation.
         
  ## Functions:-
         1. In Python, a function is a group of related statements that performs a specific task.
         2. Functions help break our program into smaller and modular chunks.
            As our program grows larger and larger, functions make it more organized and manageable.
         3. Furthermore, it avoids repetition and makes the code reusable.
         4. def function_name(parameters):
	                  """docstring"""
                     statement(s)
         5. Keyword def that marks the start of the function header.
         6. Parameters (arguments) through which we pass values to a function. They are optional.
         7. A colon (:) to mark the end of the function header.
         8. Optional documentation string (docstring) to describe what the function does.
         9. One or more valid python statements that make up the function body. Statements must have
            the same indentation level
         10. An optional return statement to return a value from the function.
         
   #### Types of Functions:-
      * Basically, we can divide functions into the following two types:
            . Built-in functions - Functions that are built into Python.
            . User-defined functions - Functions defined by the users themselves.
            
  
     
          
