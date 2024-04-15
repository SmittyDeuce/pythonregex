import re
# 1. Python Regular Expressions Mastery
# Task 1: Code Correction

# Problem Statement:
# You are given a piece of code that is intended to extract email addresses from a given text. However, the code contains errors and does not function as expected. Your task is to identify and correct these errors.

# Code Example:


text = "Contact emails are: john.doe@example.com and jane.doe@example.com."


# testing = re.findall(r"[a-zA-Z0-9._%+-]{2,}", text) 
# # print(testing)
# '''this prints every word in the text string excluding special
# characters if they 
# aren't in middle '''

# testing2 = re.findall(r"@[a-zA-Z0-9.%+-]{2,}", text)
# # print(testing2)
# ''' this prints out anything from @ to .com if i remove the . 
# it wont print out .com'''



emails = re.findall(r"[a-z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-z|[A-Z]{2,}", text)
# print(emails)

redacted = re.sub(r"[a-z0-9._%+-]+@[a-zA-Z0-9._%+-]+.",r"[ANONYMIZED USER]", text)
# print(redacted)


# Expected Outcome:
# Correctly reformat the date in each log entry.
# Replace all instances of '@username' with '[ANONYMIZED USER]'.
# Use re.sub() effectively to achieve the desired text manipulations.





# 2. Python Regular Expressions Deep Dive
# Objective:
# The aim of this assignment is to deepen your practical skills in Python's regular expressions, enhancing your ability to process and manipulate text data. You will tackle a variety of real-world scenarios, applying regex to extract, validate, and transform text effectively.

# Task 1: Email Extraction Enhancement

# Problem Statement:
# You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains (e.g., 'exclude.com'). Modify the script to extract all email addresses except those from the specified domain.

# Code Example:



# text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
# emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
# print(emails)
# Expected Outcome:

# Adapt the regex pattern to exclude email addresses from 'exclude.com'.
# Ensure the script still extracts all other valid email addresses.
# 3. Advanced Text Processing with Python Regex
# Objective:
# The goal of this assignment is to harness the full potential of Python's Regular Expressions for advanced text processing. You'll tackle complex tasks involving data extraction, validation, and transformation, sharpening your skills in applying regex in various challenging scenarios.

# Task 1: Advanced Data Extraction

# Problem Statement:
# Develop a script to extract specific information from a formatted text. The text contains data entries delimited by semicolons and formatted as 'Key: Value'. Extract the value corresponding to a specific key.

# Code Example:



# text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
# # Extract the Occupation from the text
# # Your code here
# Expected Outcome:

# Correctly identify and categorize valid and invalid URLs from the list.
# Use regex to validate the format of each URL.
# 4. Python Regex Challenge: Enhancing E-Commerce Operations
# Objective:

# This assignment aims to refine your skills in using Python Regular Expressions to address common challenges in e-commerce operations. You will focus on tasks such as product categorization, customer review analysis, and data formatting, crucial for efficient e-commerce management.

# Task 1: Product Description Keyword Tagging

# Problem Statement:
# You have a list of product descriptions. Your task is to tag each product based on keywords in the description. For instance, tag products as 'Electronics', 'Apparel', or 'Home & Kitchen' based on relevant keywords found in their descriptions.

# Code Example:

# descriptions = [
#     "Smartphone with 6-inch screen and 128GB memory",
#     "Cotton t-shirt in medium size",
#     "Stainless steel kitchen knife set"
# ]
# # Tag each product based on keywords in the description
# # Your code here
# Expected Outcome:

# Convert all price formats in the string to a standardized 'USD XX.XX' format.
# Use re.sub() to perform the necessary replacements and format transformations.