# Question 47

> **_Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area._**



```python
class Circle():
    def __init__ (self, radius):
        self.radius = radius
        self.PI = 22/7
        
    def area(self):
        '''
        Calculates the area of the Circle
        '''
        return self.PI*self.radius**2
    
    def perimeter(self):
        '''
        Calculates the perimeter of the circle
        '''
        return 2*self.PI*self.radius
    
r14 = Circle(14)
print(f'Area = {r14.area()}')
print(f'Perimeter = {r14.perimeter()}')
```

    Area = 616.0
    Perimeter = 88.0
    

# Question 48

> **_Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area._**


```python
class Rectangle():
    def __init__ (self, l, w):
        self.l = l
        self.w = w
        
    def area(self):
        '''
        Calculates the area of the Rectangle
        '''
        return self.l*self.w
    
    def perimeter(self):
        '''
        Calculates the perimeter of the Rectangle
        '''
        return 2*(self.l+self.w)
    
l4w2 = Rectangle(4,2)
print(f'Area = {l4w2.area()}')
print(f'Perimeter = {l4w2.perimeter()}')
```

    Area = 8
    Perimeter = 12
    

# Question 49

> **_Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default._**


```python
class Shape():
        
    def area(self):
        '''
        Calculates the area of the Shape
        '''
        return 0
    
    def perimeter(self):
        '''
        Calculates the perimeter of the Shape
        '''
        return 0
    
class Square(Shape):
    def __init__(self, l):
        self.l = l
    
    def area(self):
        '''
        Calculates the area of the square
        '''
        return self.l**2
    
    def perimeter(self):
        '''
        Calculates the perimeter of the Shape
        '''
        return 4*self.l
        
sq5 = Square(5)
print(f'Area = {sq5.area()}')
print(f'Perimeter = {sq5.perimeter()}')
```

    Area = 25
    Perimeter = 20
    

# Question 50

> **_Please raise a RuntimeError exception._**



```python
def zero(x):
    if x == 0:
        print('Zero')
    else:
        raise RuntimeError('Argumet has to be Zero')
        
try:
    zero(10)
except RuntimeError as exc:
    print (exc)
```

    Argumet has to be Zero
    

# Question 51

> ***Write a function to compute 5/0 and use try/except to catch the exceptions.***


```python
try:
    5/0
except Exception as exc:
    print(exc)
```

    division by zero
    

# Question 52

> ***Define a custom exception class which takes a string message as attribute.***


```python
class MyError(Exception):
    '''
    My own exception class

    Attributes:
        msg  -- explanation of the error
    '''
    def __init__(self, msg):
        self.msg =msg
        
err = MyError('My Error')
err.msg
```




    'My Error'



# Question 53

> ***Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.***


```python
email = 'sandeep@cts.com'
pos = email.index('@')
username = email[:pos]
company = email[pos+1:email.index('.')]
print (f'User Name: {username} and Company: {company}')
```

    User Name: sandeep and Company: cts
    

# Question 54

> **_Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only._**

> **_Example:
> If the following email address is given as input to the program:_**

```
john@google.com
```

> **_Then, the output of the program should be:_**

```
google
```


```python
email = 'sandeep@cts.com'
pos = email.index('@')
username = email[:pos]
company = email[pos+1:email.index('.')]
print (f'User Name: {username} and Company: {company}')
```

    User Name: sandeep and Company: cts
    

# Question 55

> **_Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only._**

> **_Example:
> If the following words is given as input to the program:_**

```
2 cats and 3 dogs.
```

> **_Then, the output of the program should be:_**

```
['2', '3']
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**



```python
check_digit = lambda x: x.isdigit()
print(list(filter(check_digit, input('Enter words: ').split())))
```

    Enter words: 2 cats and 3 dogs.
    ['2', '3']
    

# Question 56

> **_Print a unicode string "hello world"._**

---

### Hints

> **_Use u'strings' format to define unicode string._**


```python
unicode_string = u"Hello World!"
print(unicode_string)
```

    Hello World!
    

# Question 57

> **_Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8._**

---

### Hints

> **_Use unicode()/encode() function to convert._**



```python
s = input('Enter String: ')
u = s.encode('utf-8')
print(u)
```

    Enter String: Life is Good
    b'Life is Good'
    

# Question 58

> **_Write a special comment to indicate a Python source code file is in unicode._**


```python
# used in Python 2 but useless in Python 3
# Python 3 default encoding is utf-8
#Solution below for Python 2
# -*- coding: utf-8 -*-
```

# Question 59
> **_Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0)._**

> **_Example:
> If the following n is given as input to the program:_**

```
5
```

> **_Then, the output of the program should be:_**

```
3.55
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**



```python
def func(n):
    if n == 0:
        return 0
    else:
        return round(n/(n+1) + func(n-1), 2)

print(func(5))
```

    3.55
    

# Question 60

> **_Write a program to compute:_**

```
f(n)=f(n-1)+100 when n>0
and f(0)=0
```

> **_with a given n input by console (n>0)._**

> **_Example:
> If the following n is given as input to the program:_**

```
5
```

> **_Then, the output of the program should be:_**

```
500
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**



```python
def func(n):
    if n == 0:
        return 0
    else:
        return 100 + func(n-1)

print(func(5))
```

    500
    

# Question 61

> **_The Fibonacci Sequence is computed based on the following formula:_**

```
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
```

> **_Please write a program to compute the value of f(n) with a given n input by console._**

> **_Example:
> If the following n is given as input to the program:_**

```
7
```

> **_Then, the output of the program should be:_**

```
13
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---


```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input('Enter n: '))
print(func(n))
```

    Enter n: 7
    13
    

# Question 62

> **_The Fibonacci Sequence is computed based on the following formula:_**

```
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
```

> **_Please write a program to compute the value of f(n) with a given n input by console._**

> **_Example:
> If the following n is given as input to the program:_**

```
7
```

> **_Then, the output of the program should be:_**

```
0,1,1,2,3,5,8,13
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**



```python
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
n = int(input('Enter n: '))
fibs = [str(fib(i)) for i in range(n+1)]
print(','.join(fibs))
```

    Enter n: 8
    0,1,1,2,3,5,8,13,21
    

# Question 63

> **_Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console._**

> **_Example:
> If the following n is given as input to the program:_**

```
10
```

> **_Then, the output of the program should be:_**

```
0,2,4,6,8,10
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**



```python
def even_gen(n):
    for i in range(0, n+1, 2):
        yield i
even = [str(x) for x in even_gen(int(input('Enter n: ')))]
print(','.join(even))
```

    Enter n: 10
    0,2,4,6,8,10
    

# Question 64

> **_Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console._**

> **_Example:
> If the following n is given as input to the program:_**

```
100
```

> **_Then, the output of the program should be:_**

```
0,35,70
```

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**



```python
def div_5_7(n):
    for i in range(n+1):
        if not i%7 and not i%5:
            yield i

l = [str(i) for i in div_5_7(int(input('Enter n: ')))]
print(','.join(l))
```

    Enter n: 100
    0,35,70
    
