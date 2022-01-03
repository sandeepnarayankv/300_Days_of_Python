# Question 26

> **_Define a function which can compute the sum of two numbers._**


```python
def sum_of_2(n1, n2):
    '''
    Sum of Two Numbers
    '''
    return n1+n2

sum_of_2(1, 2)
```




    3



# Question 27

> **_Define a function that can convert a integer into a string and print it in console._**


```python
def convert_str(num):
    print(str(num))

convert_str(5)
```

    5
    

# Question 28

> **_Define a function that can receive two integer numbers in string form and compute their sum and then print it in console._**


```python
def sum_str(s1, s2):
    t = int(s1) + int(s2)
    print(t)
    
sum_str('5', '7')
```

    12
    

# Question 29

> **_Define a function that can accept two strings as input and concatenate them and then print it in console._**


```python
def concat_str(s1, s2):
    print(s1+' '+s2)

concat_str('3', 'love')
```

    3 love
    

# Question 30

> **_Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line._**


```python
def print_long(s1, s2):
    if len(s1) > len(s2):
        print(s1)
    elif len(s2) > len(s1):
        print(s2)
    else:
        print(s1+'\n'+s2)
        
print_long('sandeep', 'sandeep')
```

    sandeep
    sandeep
    

# Question 31

> **_Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys._**



```python
def print_sq(n):
    d = {i:i**2 for i in range(1, n+1)}
    print(d)

print_sq(20)
```

    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400}
    

# Question 32

> **_Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only._**



```python
def print_keys(n):
    d = {i:i**2 for i in range(1, n+1)}
    print(d.keys())

print_keys(20)
```

    dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    

# Question 33

> **_Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included)._**



```python
def list_sq(n):
    l = [i**2 for i in range(1, n+1)]
    print(l)

list_sq(20)
```

    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
    

# Question 34

> **_Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list._**



```python
def list_pr_sq(n):
    l = [i**2 for i in range(1, n+1)]
    print(l[:5])

list_pr_sq(20)
```

    [1, 4, 9, 16, 25]
    

# Question 35

> **_Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list._**



```python
def last5_pr_sq(n):
    l = [i**2 for i in range(1, n+1)]
    print(l[-5:])

last5_pr_sq(20)
```

    [256, 289, 324, 361, 400]
    

# Question 36

> **_Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list._**


```python
def last15_pr_sq(n):
    l = [i**2 for i in range(1, n+1)]
    print(l[5:])

last15_pr_sq(20)
```

    [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
    

# Question 37

> **_Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included)._**


```python
def tuple_sq(n):
    t = tuple([i**2 for i in range(1, n+1)])
    print(t)

tuple_sq(20)
```

    (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400)
    

# Question 38

> **_With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line._**



```python
def print_div(t):
    half = len(t)//2
    print(t[:half])
    print(t[half:])

print_div((1,2,3,4,5,6,7,8,9,10,11, 12))
```

    (1, 2, 3, 4, 5, 6)
    (7, 8, 9, 10, 11, 12)
    

# Question 39

> **_Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)._**



```python
check_even = lambda x:not x % 2

print(tuple(filter(check_even, (1,2,3,4,5,6,7,8,9,10))))
```

    (2, 4, 6, 8, 10)
    

# Question 40

> **_Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No"._**


```python
def print_yes(s):
    if s.upper() == 'YES':
        print('Yes')
    else:
        print('No')

print_yes('Sandeep')
```

    No
    

# Question 41

> **_Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]._**



```python
sq = lambda x:x**2

print(list(map(sq, [1,2,3,4,5,6,7,8,9,10])))
```

    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    

# Question 42

> **_Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]._**



```python
sq = lambda x:x**2
even = lambda x:not x % 2

print(list(map(sq, filter(even, [1,2,3,4,5,6,7,8,9,10]))))
```

    [4, 16, 36, 64, 100]
    

# Question 43

> **_Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included)._**



```python
even = lambda x:not x % 2
even_nos =  filter(even, range(1, 21))
print(list(even_nos))
```

    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    

# Question 44

> **_Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included)._**



```python
sq = lambda x:x**2

print(list(map(sq, range(1, 21))))
```

    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
    

# Question 45

> **_Define a class named American which has a static method called printNationality._**


```python
class American():
    nationality = 'American'
    def __init__(self, state):
        self.nationality = 'American'
        self.state = state
    def printNationalityState(self):
        print(f'I am {self.nationality} from {self.state}')
        
    @classmethod
    def printNationalityCls(cls):
        print(f'I am {cls.nationality}')
        
    @staticmethod
    def printNationality():
        print('I am American')
        
eddie = American('NY')
American.printNationality()
American.printNationalityCls()
eddie.printNationality()
eddie.printNationalityCls()
eddie.printNationalityState()

```

    I am American
    I am American
    I am American
    I am American
    I am American from NY
    

# Question 46

> **_Define a class named American and its subclass NewYorker._**



```python
class American():
    nationality = 'American'
    def __init__(self):
        self.nationality = 'American'
        
    def printNation(self):
        print(f'I am {self.nationality}')
        
    @classmethod
    def printNationalityCls(cls):
        print(f'I am {cls.nationality}')
        
    @staticmethod
    def printNationality():
        print('I am American')
        
class NewYorker(American):
    def __init__(self):
        super().__init__()
        self.state = 'New York'
        
    def printState(self):
        super().printNation()
        print(f'My state is {self.state}')
        
eddie = NewYorker()
eddie.printState()
print(NewYorker.mro())
```

    I am American
    My state is New York
    [<class '__main__.NewYorker'>, <class '__main__.American'>, <class 'object'>]
    
