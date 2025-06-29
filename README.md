# Social Network OOP

## Overview
This project simulates a small social network and analyzes connections between its members to recommend potential new friends.
It is implemented in Python using Object-Oriented Programming (OOP) principles.

## Object-Oriented Design
The project follows OOP practices:

- Class Hierarchy and Inheritance:
    User: base class that defines shared user attributes
    Member: inherits from User and adds functionality for managing friendships.
    SocialNetwork: Manages the network of members, file loading, and recommendation logic.
- Encapsulation and Abstraction:
    Each class encapsulates its own data and exposes behaviour through clearly defined methods.
- No code duplication:
    The program is structured to avoid redundant logic and adheres to the DRY(Don't Repeat Yourself) principles.

## Features
- Load social network data from a text file (e.g., `nw_data1.txt`)  
- Represent members and their friendships using custom classes  
- Display the social network in a clear, readable format in the console
- **Social network analysis and statistics:**
- Query the number of firends a given member has, with input validation
- Display members with the least number of firends and those with no friends
- Show all direct friends (relationships) of a given memeber, with input validation
- Find and display indirect friends (friends of friends, excluding the memeber) for every member.
- **Input validation and consistency checks:**  
- Verify that the number of members matches the header in the input file  
- Validate that all friendships are reciprocal (if A is friend of B, then B must be friend of A)  
- Raise exceptions with descriptive error messages if inconsistencies are detected  
- Included test data files for consistent and inconsistent social networks to facilitate testing



```bash
git clone https://github.com/SebastianRodriguezds/Social-Network_OOP.git
cd Social-Network_OOP
