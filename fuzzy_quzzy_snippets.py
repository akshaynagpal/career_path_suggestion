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



--------------------------------------------------------------
Python 2.7 (r27:82525, Jul  4 2010, 07:43:08) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import csv
>>> with open("C:\Users\advance\Documents\GitHub\career_path_prediction\Career_data.csv",'rb') as csvfile:
	filereader = csv.reader(csvfile,delimiter=',')

	

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    with open("C:\Users\advance\Documents\GitHub\career_path_prediction\Career_data.csv",'rb') as csvfile:
IOError: [Errno 22] invalid mode ('rb') or filename: 'C:\\Users\x07dvance\\Documents\\GitHub\\career_path_prediction\\Career_data.csv'
>>> with open("C:\/Users\/advance\/Documents\/GitHub\/career_path_prediction\/Career_data.csv",'rb') as csvfile:
	filereader = csv.reader(csvfile,delimiter=',')

	
>>> cd_list = []
>>> cd_list
[]
>>> for row in filereader:
	cd_list.append([row])

	

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    for row in filereader:
ValueError: I/O operation on closed file
>>> with open("C:\/Users\/advance\/Documents\/GitHub\/career_path_prediction\/Career_data.csv",'rb') as csvfile:
	filereader = csv.reader(csvfile,delimiter=',')
	for row in filereader:
		cd_list.append([row])

		
>>> cd_list
[[['Bachelors Stream', 'Bachelors Univ', 'Bachelors Duration', 'Masters Stream', 'Masters Univ', 'Masters Duration', 'Doctoral Stream', 'Doctoral Univ', 'Doctoral Duration', 'Work Position', 'Work Organisation']], [['CS', 'Stanford University', '2000-2004', 'CS', 'Princeton University', '2004-2006', 'Data Science', 'MIT', '2006-2009', 'Data Scientist', 'Google']], [['EE', 'Manipal University', '1984-1988', 'CS', 'University of Wisconsin', '1988-1990', '', '', '', 'Software Engineer', 'Microsoft']], [['ME', 'Delhi College of Engineering', '2004-2008', '', '', '', '', '', '', 'Mechanical Design Engineer', 'Ford']], [['IT', 'IIT Delhi', '2001-2005', 'Networking and System Engineering', 'University of California', '2005-2007', '', '', '', 'System Administrator', 'Google']], [['CS', 'IIIT Hyderabad', '1999-2003', 'Software Engineering', 'New York University', '2003-2005', '', '', '', 'Software Developer', 'Yahoo']], [['Mathematics and Computing', 'IIT Delhi', '2001-2005', 'Data Mining', 'NTU Singapore', '2005-2007', 'Statistics', 'Harvard', '2005-2008', 'Data Analyst', 'Quora']], [['CS', 'IIT Delhi', '2001-2005', 'Software Engineering', 'University of Wisconsin', '2005-2007', 'Distributed Systems', 'MIT', '2007-2010', 'Research and Development', 'Microsoft']], [['Mechanical Engineering', 'IIT Kharagpur', '2000-2004', 'Automobile Engineering', 'University of France ', '2004-2006', 'MBA Product Development', 'Harvard', '2009-2011', 'Product Development', 'Mercedes']], [['IT', 'ITM University', '2001-2005', '', 'IIM Ahemdabad', '2005-2007', '', '', '', 'Marketing Manager', 'Airtel']], [['CS', 'Stanford University', '2000-2004', '', '', '', '', '', '', 'CEO', 'Google']], [['Civil Engineering', 'NIT Kurukshetra', '1998-2002', 'Structure Engineering', 'IIT Delhi', '2002-2004', '', '', '', 'Chief Architect', 'LNT']]]
>>> import fuzzywuzzy
>>> 