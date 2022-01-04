# Question 65

> **_Please write assert statements to verify that every number in the list [2,4,6,8] is even._**



```python
l = [2,4,6,8, 10]
try:
    for i in l:
        assert not i%2
except:
    print('All elements in list are not even')
else:
    print('All elements in list are even')
```

    All elements in list are even
    

# Question 66

> **_Please write a program which accepts basic mathematic expression from console and print the evaluation result._**

> **_Example:
> If the following n is given as input to the program:_**

```
35 + 3
```

> **_Then, the output of the program should be:_**

```
38
```

---

### Hints

> **_Use eval() to evaluate an expression._**


```python
print(eval(input('Enter an expression: ')))
```

    Enter an expression: 99*101
    9999
    

# Question 67

> **_Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list._**


```python
li = [2, 3, 4, 10, 40, 60]


def binary_search(li, s):
    l = 0
    h = len(li)
    while True:
        m = (l+h)//2
        if s == li[m]:
            break
        elif s > li[m]:
            l = m
        elif s < li[m]:
           h = m 
        else:
            pass

    return m
s = int(input('Enter the No: '))
idx = binary_search(li, s)
print(f'The index of {s} in {li} is {idx} and position is {idx+1}')        
```

    Enter the No: 4
    The index of 4 in [2, 3, 4, 10, 40, 60] is 2 and position is 3
    

# Question 68

> **_Please generate a random float where the value is between 10 and 100 using Python module._**



```python
import random as r
while True:
    rf = r.randint(10,100)*r.random()
    if rf > 10 and rf <100:
        break
print(f'Random Float between 10, 100 is {rf}')
rand_num = r.uniform(10,100)
print(f'Another Random Float between 10, 100 is {rand_num}')
```

    Random Float between 10, 100 is 86.18082486724632
    Another Random Float between 10, 100 is 54.11861028289355
    


```python
help(r.uniform)
```

    Help on method uniform in module random:
    
    uniform(a, b) method of random.Random instance
        Get a random number in the range [a, b) or [a, b] depending on rounding.
    
    

# Question 69

> **_Please generate a random float where the value is between 5 and 95 using Python module._**


```python
import random as r
rand_num = r.uniform(5,95)
print(f'Random Float between 5, 95 is {rand_num}')
```

    Random Float between 5, 95 is 34.10537266158103
    

# Question 70

> **_Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension._**



```python
from random import choice
l = [x for x in range(0, 11, 2)]
print(choice(l))
```

    8
    

# Question 71

> **_Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension._**



```python
from random import choice
l = [x for x in range(0, 151) if not x%7 and not x%5]
print(choice(l))
```

    35
    

# Question 72

> **_Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive._**
---

### Hints

> **_Use random.sample() to generate a list of random values._**


```python
from random import sample
print(sample(range(100, 200), k=5))
```

    [163, 122, 176, 162, 128]
    

# Question 73

> **_Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive._**


```python
from random import sample
print(sample(range(100, 201, 2), k=5))
```

    [154, 170, 100, 130, 148]
    

# Question 74

> **_Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive._**


```python
from random import sample
print(sample([i for i in range(1, 1001) if i%7 == 0 and i%5 == 0], k=5))
```

    [665, 980, 350, 560, 140]
    

# Question 75

> **_Please write a program to randomly print a integer number between 7 and 15 inclusive._**



```python
from random import randint
print(randint(7, 15))
```

    15
    

# Question 76

> **_Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!"._**

---

### Hints

> **_Use zlib.compress() and zlib.decompress() to compress and decompress a string._**



```python
import zlib
c = zlib.compress("hello world!hello world!hello world!hello world!".encode('utf-8'))
print(c)
d = zlib.decompress(c)
print(d)
```

    b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82\r\x00\xbd[\x11\xf5'
    b'hello world!hello world!hello world!hello world!'
    

# Question 77
> **_Please write a program to print the running time of execution of "1+1" for 100 times._**


```python
def calctime_dec(func):
    def wrapper_calctime(*args, **kwargs):
        import time
        ts = time.time()
        for _ in range(100000):
            func(*args, **kwargs)
        te = time.time()
        
        print("Total time taken in : ", func.__name__, te - ts)
    return wrapper_calctime

@calctime_dec
def add_nos():
    d = 1+1

add_nos()
    
```

    Total time taken in :  add_nos 0.014000892639160156
    

# Question 78

> **_Please write a program to shuffle and print the list [3,6,7,8]._**


```python
import random as r
li = [3,6,7,8]
r.shuffle(li)
print(li)
```

    [7, 3, 6, 8]
    

# Question 79

> **_Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"]._**

---

### Hints

> **_Use list[index] notation to get a element from a list._**



```python
subject = ["I", "You"]
verb = ["Play", "Love"]
obj = ["Hockey","Football"]

for s in subject:
    for v in verb:
        for o in obj:
            print (f'{s} {v} {o}')
```

    I Play Hockey
    I Play Football
    I Love Hockey
    I Love Football
    You Play Hockey
    You Play Football
    You Love Hockey
    You Love Football
    

# Question 80

> **_Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24]._**


```python
odd = lambda x: x%2
li = [5,6,77,45,22,12,24]
print(list(filter(odd, li)))
```

    [5, 77, 45]
    

# Question 81

> **_By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]._**



```python
li = [12,24,35,70,88,120,155]
print([i for i in li if i%7 != 0 and i%5 != 0])
```

    [12, 24, 88]
    

# Question 82

> **_By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155]._**


```python
li = [12,24,35,70,88,120,155]
print([i for i in li if li.index(i)%2 != 0])
```

    [24, 70, 120]
    


```python
# solution 2
li = [12,24,35,70,88,120,155]
print([v for (i, v) in enumerate(li) if i%2 != 0 and i<=6])
```

    [24, 70, 120]
    

# Question 83

> **_By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155]._**


```python
li = [12,24,35,70,88,120,155]
print([v for (i, v) in enumerate(li) if i not in range(1, 4)])
```

    [12, 88, 120, 155]
    

# Question 84

> **_By using list comprehension, please write a program generate a 3\*5\*8 3D array whose each element is 0._**


```python
li = [[[0 for x in range(8)] for y in range(5)] for z in range(3)]
print(li)
```

    [[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]]
    
