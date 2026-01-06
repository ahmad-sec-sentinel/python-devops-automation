# 1. Finding a pattern in a string 
import re  #Loads Python’s regular expression module to  use functions like re.search
text = "Cloud services provide high availability and scalability"
pattern = r"service"  # Defines a raw string pattern containing the regular expression to search for. The r prefix makes backslashes literal, useful for regex

match = re.search(pattern, text) #re.search scans the whole string and stops at the first match; it does not require the pattern to match the entire string
if match:
    print("Pattern found:", match.group(0))  # group(0) is the whole match
else:
    print("Pattern not found")
#When a match is found, match is an instance of the re.Match class (a Match object). If no match is found, match is None

print(type(match))            # <class 're.Match'> or <class 'NoneType'>
if match:
    print(match.group(0))     # prints 'service' for this example
    print(match.span())       # prints (6, 13) the start and end indices
    print(match.string)       # prints the original text
