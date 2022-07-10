```diff
-hashcracker was created for educational purposes only. 
-Do not crack anyone else's passwords without their consent (It's a crime!) 
-How you use the hashcracker is entirely up to you.
```
## Installation
You can install HC by cloning this GitHub repository or by manually downloading main.py
```
git clone https://github.com/j-jaros/hashcracker
```
## How HashCracker can be used?
Let's imagine a situation like this:
You are a blackhat hacker. One day, someone asks you to redirect a government gold shipment to Sweden.

You learn that yesterday a database containing all the data that allows you to log in to the government platform through which the gold supply is managed has been leaked.

You buy leak data for cryptocurrencies and get to work.

You know that passwords are hashed and not salted. Unfortunately, you do not know the algorithm in which they were hashed.

This is where HashCracker comes in.

![HashCracker_demo1](https://i.ibb.co/wrfXfbp/HC1.png)\
You run the script, then paste the hash from the leak and wait about 10 seconds (more about this in the technical information)
and voilà! 
You know the password that allows you to log in to the administrator account and redirect the delivery.

## How HashCracker works?
#### 1. Checking if the dictionary exists
At startup, the first thing to check is that the password dictionary exists.\
If it exists, you will be prompted for a hash.
Otherwise, an error message will be displayed.

#### 2. Recognition of the algorithm
The algorithm is recognized by measuring the length of the hash.\
For example, if the hash is 32 characters long, we know it is MD5.\
If the hash is 96 characters long, we know it is SHA-384 etc.
#### 3. Creating a password list
Creating a list of passwords is done by reading the dictionary with passwords and placing each of the passwords in the list.
#### 4. Cracking the password
Cracking the password is done by reading each item from the list, hashing it and comparing it with the base hash (the hash entered by the user)
If the hashes are identical, the currently selected item from the list will be displayed as a cracked password

## Technical information
#### Password dictionary requirements
```
File must be named passwords
File must have .txt extension
The file must be located in the same directory as main.py
Each password should be in separate line
```
#### Supported algorithms
```
MD5
SHA-1 
SHA-224
SHA-256
SHA-384
SHA-512
```
#### Cracking speed
The speed of password cracking depends on the number of passwords and the place where the password is located.
If we have 999,999 entries in the dictionary (the same as in the dictionary attached to the HashCracker) and the password is at the very end of the dictionary, then the cracking time will be longer
#### Cracking speed tests result
Speed ​​test results vary depending on the environment in which main.py is running
##### MacOS Monterey 12.4 (Terminal) i5 1.6GHz/8GB RAM
```
Number of tests performed: 50
Longer cracking time: 9.610 seconds
Shortest cracking time: 9.001 seconds
Average cracking time: 9.11 seconds
```
##### MacOS Monterey 12.4 (PyCharm 2022.1.3 Professional) i5 1.6Ghz/8GB RAM
```
Number of tests performed: 50
Longer cracking time: 6.035 seconds
Shortest cracking time: 5.270 seconds
Average cracking time: 5.471 seconds
```
More tests will be performed in future.

### License
If you plan to use HashCracker in your project, or if you use it for professional purposes, please let me know. I am curious how it will be used :)\
HashCracker is licensed [MIT](https://github.com/j-jaros/hashcracker/blob/main/LICENSE)
