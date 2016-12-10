import re

exampleStr = "qwertweb7448 Rockwell St.okwaeokdwa"
exampleStr2 = "waedceacae6317 Kemore Ave.okaeodawd"

address = re.findall(r'\d{1,4}\s\w+\s\w+',exampleStr)
address2 = re.findall(r'\d{1,4}\s[NSEW]?\s\w+\s\w+', exampleStr2)

print(address)
print(address2)
