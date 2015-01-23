Python 2.7 (r27:82525, Jul  4 2010, 07:43:08) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import difflib
>>> from fuzzywuzzy import fuzz
>>> from fuzzywuzzy import process
>>> fuzz.ratio("this is a test","this is a test")
100
>>> fuzz.ratio("this is a test","this is a tes")
96
>>> fuzz.ratio("this is a test","this is a te")
92
>>> fuzz.ratio("this is a test","")
0
>>> fuzz.ratio("abc","abc")
100
>>> fuzz.ratio("abc","ab")
80
>>> fuzz.ratio("abc","abA")
67
>>> fuzz.ratio("a","A")
0
>>> fuzz.partial_ratio("a","A")
0
>>> choices = ["Data Analyst","Data Scientist","Software Scientist","Software Developer","Software Engineer"]
>>> fuzz.ratio("data scientist","Data Scientist")
86
>>> fuzz.ratio("data scientist","Data Analyst")
54
>>> for pos in choices:
	print pos+"->"+str(fuzz.ratio("data scientist",pos))

	
Data Analyst->54
Data Scientist->86
Software Scientist->63
Software Developer->19
Software Engineer->26

>>> positions = ["System Analyst","Data Scientist","Software Developer","CEO","Data Analyst","Software Engineer"]
>>> for pos in choices:
	print pos+"->"+str(fuzz.ratio("data scientist",pos))

	
Data Analyst->54
Data Scientist->86
Software Scientist->63
Software Developer->19
Software Engineer->26

>>> for pos in positions:
	print pos+"->"+str(fuzz.ratio("data scientist",pos))

	
System Analyst->14
Data Scientist->86
Software Developer->19
CEO->0
Data Analyst->54
Software Engineer->26

>>> for pos in positions:
	print pos+"->"+str(fuzz.ratio("software engineer",pos))

	
System Analyst->19
Data Scientist->39
Software Developer->69
CEO->0
Data Analyst->14
Software Engineer->88

>>> import difflib
>>> s = difflib.SequenceMatcher(None,"Software Engineer","software engineer")
>>> s.ratio()
0.8823529411764706
>>> s.quick_ratio()
0.8823529411764706
>>> s.real_quick_ratio()
1.0
>>> fuzz.ratio("Software Engineer","software engineer")
88
>>> s = difflib.SequenceMatcher(None,"Data Scientist","Data Analyst")
>>> s.ratio()
0.6153846153846154
>>> s.quick_ratio()
0.6153846153846154
>>> s.real_quick_ratio()
0.9230769230769231
>>> fuzz.ratio("Data Scientist","Data Analyst")
62
