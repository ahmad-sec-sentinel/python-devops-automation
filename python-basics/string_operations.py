#This python file lists simple operations done on string data type using in built functions
# 1. String strip to remove white spaces
text = "   There are  spaces left  intentionally  blank     "
stripped_text = text.strip()
print("Stripped text:", stripped_text)

# 2. Counting the number of characters after stripping the text of blank spaces
length = len(stripped_text)
print("Length of the string after removing white spaces:", length)

# 3. Concept of string concatenation
str1 = "DevOps"
str2 = "Automation"
result = str1 + " " + str2
print(result)

# 4. Converting string to upper or lower case using inbuilt function
uppercase = result.upper()
lowercase = result.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

# 5. Replacing all instances of a word with another word
str3 = "Automation make tasks easy to perform"
new_text = str3.replace("tasks", "operations")
print("Modified text:", new_text)

# 6. split() without arguments splits the string on any whitespace (spaces, tabs, newlines).It treats consecutive whitespace as a single separator.
#It removes leading and trailing whitespace automatically.
str4 = " Terraform automates infrastrucure creation"
words = str4.split()
print("Words:", words) #split() returns a list containing substrings of the original string.


