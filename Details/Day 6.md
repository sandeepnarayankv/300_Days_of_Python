# Question 85

> **_By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]._**

---

### Hints

> **_Use list comprehension to delete a bunch of element from a list.Use enumerate() to get (index, value) tuple._**



```python
l = [12,24,35,70,88,120,155]
f = [v for i, v in enumerate(l) if i not in (0, 4, 5)]
print(f)
```

    [24, 35, 70, 155]
    

# Question 86

> **_By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]._**

---

### Hints

> **_Use list's remove method to delete a value._**


```python
l = [12,24,35,24,88,120,155]
nl = [x for x in l if x!=24]
print(nl)
```

    [12, 35, 88, 120, 155]
    

# Question 87

> **_With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists._**

---

### Hints

> **_Use set() and "&=" to do set intersection operation._**



```python
l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]
nl = list(set(l1).intersection(set(l2)))
print(nl)
```

    [35]
    

# Question 88

> **_With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved._**

---

### Hints

> **_Use set() to store a number of values without duplicate._**



```python
li = [12,24,35,24,88,120,155,88,120,155]
lir = sorted(list(set(li[::-1])), reverse = True)
print(lir)
```

    [155, 120, 88, 35, 24, 12]
    

# Question 89

> **_Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class._**

---

### Hints

> **_Use Subclass(Parentclass) to define a child class._**



```python
class Person():
    def __init__(self):
        self.gender = 'Unknown'
    def getGender(self):
        print(self.gender)
        
class Male(Person):
    def __init__(self):
        self.gender = 'Male'
        
class Female(Person):
    def __init__(self):
        self.gender = 'Female'
        
san = Male()
pre = Female()

san.getGender()
pre.getGender()
```

    Male
    Female
    

# Question 90

> **_Please write a program which count and print the numbers of each character in a string input by console._**

> **_Example:
> If the following string is given as input to the program:_**

```
abcdefgabc
```

> **_Then, the output of the program should be:_**

```
a,2
c,2
b,2
e,1
d,1
g,1
f,1
```

### Hints

> **_Use dict to store key/value pairs.
> Use dict.get() method to lookup a key with default value._**



```python
s = input('Enter a String: ')
d = dict()
for c in s:
    n = s.count(c)
    if c not in d.keys():
        d[c] = n
for k, v in d.items():
    print(f'{k},{v}')
```

    Enter a String: abcdefgabc
    a,2
    b,2
    c,2
    d,1
    e,1
    f,1
    g,1
    

# Question 91

> **_Please write a program which accepts a string from console and print it in reverse order._**

> **Example:
> If the following string is given as input to the program:\***

```
rise to vote sir
```

> **_Then, the output of the program should be:_**

```
ris etov ot esir
```

### Hints

> **_Use list[::-1] to iterate a list in a reverse order._**



```python
s = input('Enter a String: ')
print(s[::-1])
```

    Enter a String: rise to vote sir
    ris etov ot esir
    

# Question 92

> **_Please write a program which accepts a string from console and print the characters that have even indexes._**

> **_Example:
> If the following string is given as input to the program:_**

```
H1e2l3l4o5w6o7r8l9d
```

> **_Then, the output of the program should be:_**

```
Helloworld
```

### Hints

> **_Use list[::2] to iterate a list by step 2._**


```python
s = input('Enter a String: ')
l = [v for i,v in enumerate(s) if i%2 == 0]
print(''.join(l))
```

    Enter a String: H1e2l3l4o5w6o7r8l9d
    Helloworld
    

# Question 93

> **_Please write a program which prints all permutations of [1,2,3]_**

---

### Hints

> **_Use itertools.permutations() to get permutations of list._**



```python
import itertools as i
l = [1,2,3]
nl = list()
for x in range(1, len(l)+1):
    for t in list(i.permutations(l, x)):
        nl.append(t)
print(nl)
```

    [(1,), (2,), (3,), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    

# Question 94

> **_Write a program to solve a classic ancient Chinese puzzle:
> We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?_**

---

### Hints

> **_Use for loop to iterate all possible solutions._**



```python
h = int(input('Heads: '))
l = int(input('Legs: '))
total = h
combos = list()
legs_of_animals = {'Rabbit': 4, 'Chicken': 2}
for i in range(1, total+1):
    rabbit_legs = legs_of_animals['Rabbit']*i
    chicken_legs = legs_of_animals['Chicken']*(total - i)
    total_legs = rabbit_legs+chicken_legs
    if total_legs == l:
        combos.append((i, total-i))
        
for r, c in combos:
    print(f'Rabbits: {r}, Chicken: {c}')
```

    Heads: 35
    Legs: 94
    Rabbits: 12, Chicken: 23
    

# Question 95

> **_Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up._**

> **_If the following string is given as input to the program:_**
>
> ```
> 5
> 2 3 6 6 5
> ```
>
> **_Then, the output of the program should be:_**
>
> ```
> 5
> ```

### Hints

> **_Make the scores unique and then find 2nd best number_**



```python
n = int(input('N: '))
l = [int(i) for i in input('Enter the values: ').split()]
rs = sorted(list(set(l)))[-2]
print(rs)
```

    N: 5
    Enter the values: 2 3 6 6 5
    5
    

# Question 96

> **_You are given a string S and width W.
> Your task is to wrap the string into a paragraph of width._**

> **_If the following string is given as input to the program:_**
>
> ```
> ABCDEFGHIJKLIMNOQRSTUVWXYZ
> 4
> ```
>
> **_Then, the output of the program should be:_**
>
> ```
> ABCD
> EFGH
> IJKL
> IMNO
> QRST
> UVWX
> YZ
> ```

### Hints

> **_Use wrap function of textwrap module_**



```python
import textwrap as t
s = input('S: ')
w = int(input('W: '))
paras= t.wrap(s, w)
for p in paras:
    print(p)
```

    S: ABCDEFGHIJKLIMNOQRSTUVWXYZ
    W: 4
    ABCD
    EFGH
    IJKL
    IMNO
    QRST
    UVWX
    YZ
    

# Question 97

> **_You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)_**

> **_Different sizes of alphabet rangoli are shown below:_**
>
> ```
> #size 3
>
> ----c----
> --c-b-c--
> c-b-a-b-c
> --c-b-c--
> ----c----
>
> #size 5
>
> --------e--------
> ------e-d-e------
> ----e-d-c-d-e----
> --e-d-c-b-c-d-e--
> e-d-c-b-a-b-c-d-e
> --e-d-c-b-c-d-e--
> ----e-d-c-d-e----
> ------e-d-e------
> --------e--------
> ```

### Hints

> **_First print the half of the Rangoli in the given way and save each line in a list. Then print the list in reverse order to get the rest._**



```python
import string
n = int(input('Size of Pyramid: '))
line_nos = (n*2) - 1
line_size = (line_nos)*2 - 1
chars = string.ascii_lowercase
ans = []
for i in range(n):
    left = '-'.join(chars[n - i - 1:n])
    mid = left[-1:0:-1] + left
    final = mid.center(line_size, '-')
    ans.append(final)

if len(ans) > 1:
    for i in ans[n - 2::-1]:
        ans.append(i)
ans = '\n'.join(ans)
print(ans)
```

    Size of Pyramid: 2
    --b--
    b-a-b
    --b--
    

# Question 98

> **_You are given a date. Your task is to find what the day is on that date._**

**Input**

> **_A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format._**
>
> ```
> 08 05 2015
> ```

**Output**

> **_Output the correct day in capital letters._**
>
> ```
> WEDNESDAY
> ```

---

### Hints

> **_Use weekday function of calendar module_**



```python
import calendar as c
week_days = {0: 'MONDAY',
            1: 'TUESDAY',
             2: 'WEDNESDAY',
            3: 'THURSDAY',
            4: 'FRIDAY',
            5: 'SATURDAY',
            6: 'SUNDAY'}
dt = input().split()
print(dt)
wk = c.weekday(int(dt[2]), int(dt[0]), int(dt[1]))
print(week_days[wk])
```

    08 05 2015
    ['08', '05', '2015']
    WEDNESDAY
    

# Question 99

> **_Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both._**

**Input**

> **_The first line of input contains an integer, M.The second line contains M space-separated integers.The third line contains an integer, N.The fourth line contains N space-separated integers._**
>
> ```
> 4
> 2 4 5 9
> 4
> 2 4 11 12
> ```

**Output**

> **_Output the symmetric difference integers in ascending order, one per line._**
>
> ```
> 5
> 9
> 11
> 12
> ```

---

### Hints

> **_Use \'^\' to make symmetric difference operation._**



```python
len1 = int(input('Enter S11 len: '))
s1 = set([int(s) for s in input('Enter S1: ').split()])
len2 = int(input('Enter S2 len: '))
s2 = set([int(s) for s in input('Enter S2: ').split()])

s = set.symmetric_difference(s1, s2)
for c in s:
    print(c)
```

    Enter S11 len: 4
    Enter S1: 2 4 5 9
    Enter S2 len: 4
    Enter S2: 2 4 11 12
    5
    9
    11
    12
    

# Question 100

> **_You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification._**

> **_If the following string is given as input to the program:_**
>
> ```
> 4
> bcdef
> abcdefg
> bcde
> bcdef
> ```
>
> **_Then, the output of the program should be:_**
>
> ```
> 3
> 2 1 1
> ```

### Hints

> **_Make a list to get the input order and a dictionary to count the word frequency_**



```python
n = int(input())

wl = list()
wd = dict()

for i in range(n):
    w = input()
    if w not in wd:
        wl.append(w)
    wd[w] = wd.get(w, 0) + 1

print(len(wl))
for w in wl:
    print(wd[w], end=' ')
```

    4
    bcde
    dhgfdhs
    bcde
    bcde
    2
    3 1 

# Question 101

> **_You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency._**

> **_If the following string is given as input to the program:_**
>
> ```
> aabbbccde
> ```
>
> **_Then, the output of the program should be:_**
>
> ```
> b 3
> a 2
> c 2
> d 1
> e 1
> ```

### Hints

> **_Count frequency with dictionary and sort by Value from dictionary Items_**



```python
s = input('S: ')
d = dict()
d = {c: s.count(c) for c in s if c not in d.keys()}
dl = list(d.items())
sorted_dl = sorted(dl, key = lambda x: x[1], reverse=True)    
for t in sorted_dl:
    print(t[0], t[1])
```

    S: aabbbccde
    b 3
    a 2
    c 2
    d 1
    e 1
    

# Question 102

> **_Write a Python program that accepts a string and calculate the number of digits and letters._**

**Input**

> ```
> Hello321Bye360
> ```

**Output**

> ```
> Digit - 6
> Letter - 8
> ```

---

### Hints

> **_Use isdigit() and isalpha() function_**



```python
s = input('S: ')
l = 0
d = 0
for c in s:
    if c.isalpha():
        l+=1
    elif c.isdigit():
        d+=1
    else:
        pass
print(f'Digit - {d}')
print(f'Letter - {l}')

```

    S: Hello321Bye360
    Digit - 6
    Letter - 8
    

# Question 103

> **_Given a number N.Find Sum of 1 to N Using Recursion_**

**Input**

> ```
> 5
> ```

**Output**

> ```
> 15
> ```

---

### Hints

> **_Make a recursive function to get the sum_**



```python
def recursive_sum (n):
    if n <=1:
        return n
    else:
        return n + recursive_sum(n-1)

n = int(input('N: '))
print(recursive_sum(n))
        
```

    N: 5
    15
    
