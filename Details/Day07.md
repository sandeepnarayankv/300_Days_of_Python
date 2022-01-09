# Question 1
> **_Write a program which will check if the string given matches the criteria for the password
> Has minimum 8 characters, containts alphabets, numbers or the following special chars @#%&_**


```python
import re
regex = r"(^[a-zA-Z0-9%$&#@]{8,})$"
pattern = re.compile(regex)
password = (input('Enter the password: '))
mtch = pattern.match(password)
if mtch == None:
    print('Password does not Match')
else:
    print('Password Matches')
```

    Enter the password: sfgkhs
    Password does not Match
    

# Question 2
> **_Write a program which will check if the string given matches the criteria for the password
> Has minimum 8 characters, containts alphabets, numbers or the following special chars @#%& and ends with a Number_**


```python
import re
regex = r"(^[a-zA-Z0-9%$&#@]{7,}\d)$"
pattern = re.compile(regex)
password = (input('Enter the password: '))
mtch = pattern.match(password)
if mtch == None:
    print('Password does not Match')
else:
    print('Password Matches')
```

    Enter the password: 65876548756
    Password Matches
    

# Question 3
> **_Write a program which will check if the string given matches the criteria for the password
> Has minimum 8 characters, starts with an alphabet, contains atleast 1 lowercase, 1 uppercase 1 Number and , atleast 1 special Character_**


```python
import re
regex =  r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)(^([a-zA-Z][\w\W]{7,}))"
pattern = re.compile(regex)
password = (input('Enter the password: '))
mtch = pattern.match(password)
if mtch == None:
    print('Password does not Match')
else:
    print('Password Matches')
```

    Enter the password: hgdfjhgsd12$A
    Password Matches
    

# Question 4
> **_Using Regex Write a program which split an email into username & domain_**


```python
import re

regex = r"(^([\w_.+]*)@([\w\W]*))"
pattern = re.compile(regex)
email = (input('Enter the email: '))
matches = pattern.search(email).groups()
print(f'User Name: {matches[1]}')
print(f'Domain: {matches[2]}')
```

    Enter the email: dgffds.sfsf.fdfd@gfdfd.xxx
    User Name: dgffds.sfsf.fdfd
    Domain: gfdfd.xxx
    
