import re

exampleStr = "On 12/07/16 Dr. Boex amazed Mr. Dyer by using Regex to remove the date code"
exampleStr2 = "On 1.05.15 Dr. Dyer started to be amazed at the Regex code that Dr. Boex used on 12/07/16"
exampleStr3 = "There was a situation in the courtroom on 10-5-16. This happened at 4:05:12"

def regexDate(str) :
	return re.findall(r'\d{1,2}[/\-.]\d{1,2}[/\-.]\d{1,2}', str)

print(regexDate(exampleStr))
print(regexDate(exampleStr2))
print(regexDate(exampleStr3))
