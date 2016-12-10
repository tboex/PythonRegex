import re

exampleStr = "Dr Lawrence helped the patient move out of bed at 21:45:02 and proceeded to give him his treatment"
exampleStr2 = "Dr Dyer tried to kill his patient at 0:05:21"

def getTime(str) :
	time = re.findall(r'\d{,2}:\d{2}:\d{2}', str)
	return time

print(getTime(exampleStr))
print(getTime(exampleStr2))
