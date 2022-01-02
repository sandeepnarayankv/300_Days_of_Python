# Question 16

> **_Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers._** 
>**_Suppose the following input is supplied to the program:_**

```
1,2,3,4,5,6,7,8,9
```

> **_Then, the output should be:_**

```
1,9,25,49,81
```


```python
s = input ('Enter a list of comma seperated numbers: ').split(',')
sq = [str(int(i)**2) for i in s if int(i)%2 != 0]
print(','.join(sq))
```

    Enter a list of comma seperated numbers: 1,2,3,4,5,6,7,8,9
    1,9,25,49,81
    

# Question 17

> **_Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:_**

```
D 100
W 200
```

- D means deposit while W means withdrawal.

> **_Suppose the following input is supplied to the program:_**

```
D 300
D 300
W 200
D 100
```

> **_Then, the output should be:_**

```
500
```


```python
total = 0
while True:
    s = input('Enter Transaction (Press Enter to End): ')
    if s == '':
        break
    else:
        l = s.split()
        if l[0].upper() == 'D':
            total += int(l[1])
        elif l[0].upper() == 'W':
            total -= int(l[1])
        else:
            pass
print(total)
```

    Enter Transaction (Press Enter to End): D 300
    Enter Transaction (Press Enter to End): D 300
    Enter Transaction (Press Enter to End): W 200
    Enter Transaction (Press Enter to End): D 100
    Enter Transaction (Press Enter to End): 
    500
    

# Question 18

> **_A website requires the users to input username and password to register. Write a program to check the validity of password input by users._**

> **_Following are the criteria for checking the password:_**

- **_At least 1 letter between [a-z]_**
- **_At least 1 number between [0-9]_**
- **_At least 1 letter between [A-Z]_**
- **_At least 1 character from [$#@]_**
- **_Minimum length of transaction password: 6_**
- **_Maximum length of transaction password: 12_**

> **_Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma._**

> **_Example_**

> **_If the following passwords are given as input to the program:_**

```
ABd1234@1,a F1#,2w3E*,2We3345
```

> **_Then, the output of the program should be:_**

```
ABd1234@1
```


```python
alpha_lower = lambda x: x.isalpha() and x.islower()
alpha_upper = lambda x: x.isalpha() and x.isupper()
digit = lambda x: x.isdigit()
spl = lambda x: x in '$#@'
    
s = input ('Enter a list of comma seperated password candidates: ').split(',')
accepted = list()
for p in s:
    if len(p) >= 6 and len(p)<= 12 and True in map(alpha_lower, p) and True in map(alpha_upper, p) and True in map(digit, p) and True in map(spl, p):
        accepted.append(p)

print (','.join(accepted))
```

    Enter a list of comma seperated password candidates: ABd1234@1,aF1#,2w3E*,2We3345
    ABd1234@1
    

# Question 19

> **_You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:_**

- **_1: Sort based on name_**
- **_2: Then sort based on age_**
- **_3: Then sort by score_**

> **_The priority is that name > age > score._**

> **_If the following tuples are given as input to the program:_**

```
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
```

> **_Then, the output of the program should be:_**

```
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
```



```python
lst = list()
while True:
    s = input ('Enter a list of comma seperated tuple values: ')
    if s:
        lst.append(tuple(s.split(',')))
    else:
        break

lst.sort(key = lambda x: (x[0], int(x[1]), int(x[2])))
lst
```

    Enter a list of comma seperated tuple values: Json,21,85
    Enter a list of comma seperated tuple values: Tom,19,80
    Enter a list of comma seperated tuple values: John,20,90
    Enter a list of comma seperated tuple values: Jony,17,91
    Enter a list of comma seperated tuple values: Jony,17,93
    Enter a list of comma seperated tuple values: 
    




    [('John', '20', '90'),
     ('Jony', '17', '91'),
     ('Jony', '17', '93'),
     ('Json', '21', '85'),
     ('Tom', '19', '80')]



# Question 20

> **_Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n._**

> **_Suppose the following input is supplied to the program:_**

```
7
```

> **_Then, the output should be:_**

```
0
7
14
```


```python
class Divisible():
    def __init__(self, n):
        self.n = n
    
    def by_seven(self):
        for i in range(0, self.n//7+2):
            yield i*7
            
n = int(input('Please insert a number. --> '))
seven = Divisible(n)
for value in seven.by_seven():
    print(value)
```

    Please insert a number. --> 7
    0
    7
    14
    

# Question 21

> **_A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:_**

```
UP 5
DOWN 3
LEFT 3
RIGHT 2
```

> **_The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer._**
> **_Example:_**
> **_If the following tuples are given as input to the program:_**

```
UP 5
DOWN 3
LEFT 3
RIGHT 2
```

> **_Then, the output of the program should be:_**

```
2
```


```python
origin = (0,0)

left = lambda current_pos, move: (current_pos[0] - move, current_pos[1])
right = lambda current_pos, move: (current_pos[0] + move, current_pos[1])
up = lambda current_pos, move: (current_pos[0], current_pos[1] + move)
down = lambda current_pos, move: (current_pos[0], current_pos[1] - move)

current_pos = (0,0)
while True:
    s = input ('Enter space seperated direction and value: ')
    if s:
        l = s.split()
        if l[0].upper() == 'LEFT':
            current_pos = left(current_pos, int(l[1]))
        elif l[0].upper() == 'RIGHT':
            current_pos = right(current_pos, int(l[1]))
        elif l[0].upper() == 'UP':
            current_pos = up(current_pos, int(l[1]))
        elif l[0].upper() == 'DOWN':
            current_pos = down(current_pos, int(l[1]))
        else:
            pass
    else:
        break
d = int(((current_pos[0]-origin[0])**2 + (current_pos[1]-origin[1])**2)**0.5)
print (d)
```

    Enter space seperated direction and value: up 5
    Enter space seperated direction and value: down 3
    Enter space seperated direction and value: left 3
    Enter space seperated direction and value: right 2
    Enter space seperated direction and value: 
    2
    

# Question 22

> **_Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically._**

> **_Suppose the following input is supplied to the program:_**

```
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
```

> **_Then, the output should be:_**

```
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
```


```python
s = input ('Enter a list of words: ').split()
wc = dict()
wc = {w:s.count(w) for w in s if w not in wc}
for k in sorted(wc.keys()):
    print(f'{k}:{wc[k]}')
```

    Enter a list of words: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
    2:2
    3.:1
    3?:1
    New:1
    Python:5
    Read:1
    and:1
    between:1
    choosing:1
    or:2
    to:1
    

# Question 23

> **_Write a method which can calculate square value of number_**



```python
def square(n):
    return n**2

square(5)
```




    25



# Question 24

> **_Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions._**

> **_Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()_**

> **_And add document for your own function_**


```python
print(abs.__doc__)
print(int.__doc__)

def square(n):
    '''
    Return the square of a Number
    '''
    return n**2

print(square.__doc__)
```

    Return the absolute value of the argument.
    int([x]) -> integer
    int(x, base=10) -> integer
    
    Convert a number or string to an integer, or return 0 if no arguments
    are given.  If x is a number, return x.__int__().  For floating point
    numbers, this truncates towards zero.
    
    If x is not a number or if base is given, then x must be a string,
    bytes, or bytearray instance representing an integer literal in the
    given base.  The literal can be preceded by '+' or '-' and be surrounded
    by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
    Base 0 means to interpret the base from the string as an integer literal.
    >>> int('0b100', base=0)
    4
    
        Return the square of a Number
        
    

# Question 25

> **_Define a class, which have a class parameter and have a same instance parameter._**



```python
class Animal():
    name = "Animal"
    def __init__(self, name):
        self.name = name
        
giraffe = Animal('Giraffe')
print(giraffe.name)
print(Animal.name)
    
```

    Giraffe
    Animal
    
