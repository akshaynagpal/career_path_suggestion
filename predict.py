import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv

#getting the data file
cd_list = []
with open("C:\/Users\/advance\/Documents\/GitHub\/career_path_prediction\/Career_data.csv",'rb') as csvfile:
	filereader = csv.reader(csvfile,delimiter=',')
	for row in filereader:
		cd_list.append(row)

#making an array from list of lists
data_array = np.array(cd_list)

def predictor():
        user_future = raw_input("Enter your future profession : ")
        for i in range(1,data_array.shape[0]):
                if fuzz.ratio(user_future,data_array[i][9])>50:
                        print "(Relevance = "+ str(fuzz.ratio(user_future,data_array[i][9])) + ") ",
                        if data_array[i][0] != '':
                                print "Bachelors : "+ data_array[i][0],
                        if data_array[i][3] != '':
                                print "-> Masters : "+ data_array[i][3],
                        if data_array[i][6] != '':
                                print "-> Doctoral : "+ data_array[i][6],
                        print "-> " + data_array[i][9],
                        print "\n"

choice = 'Y'                     
while choice == 'Y' or choice == 'y':
        predictor()
        choice = raw_input("Continue?(Y/y/N/n)")
        if choice == 'N' or choice == 'n':
                break
        elif choice != 'Y' and choice != 'y':
                break
