>>> cd_list = []	
>>> cd_list
[]
>>> with open("C:\/Users\/advance\/Documents\/GitHub\/career_path_prediction\/Career_data.csv",'rb') as csvfile:
	filereader = csv.reader(csvfile,delimiter=',')
	for row in filereader:
		cd_list.append(row)

#-----------------------------------------------------------

>>> for i in range(1,data_array.shape[0]):
	if fuzz.ratio(user_future,data_array[i][9])>60:
		print "(Relevance = "+ str(fuzz.ratio(user_future,data_array[i][9])) + ") ",
		if data_array[i][0] != '':
			print "Bachelors : "+ data_array[i][0],
		if data_array[i][3] != '':
			print "-> Masters : "+ data_array[i][3],
		if data_array[i][6] != '':
			print "-> Doctoral : "+ data_array[i][6],
		print "-> " + data_array[i][9],
		print "\n"

		
(Relevance = 63)  Bachelors : EE -> Masters : CS -> Software Engineer 


(Relevance = 89)  Bachelors : CS -> Masters : Software Engineering -> Software Developer 