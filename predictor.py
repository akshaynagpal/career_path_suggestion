def predictor():
        flag = 0
        user_input = raw_input("Enter your future profession : ")
        user_future = user_input.title()
        for i in range(1,data_array.shape[0]):
                if fuzz.ratio(user_future,data_array[i][9])>60:
                        flag = 1
                        print "(Relevance = "+ str(fuzz.ratio(user_future,data_array[i][9])) + ") ",
                        if data_array[i][0] != '':
                                print "Bachelors : "+ data_array[i][0],
                        if data_array[i][3] != '':
                                print "-> Masters : "+ data_array[i][3],
                        if data_array[i][6] != '':
                                print "-> Doctoral : "+ data_array[i][6],
                        print "-> " + data_array[i][9],
                        print "\n"
        if flag == 0:
                print "no simple ratio match...trying for partial match..."
                for i in range(1,data_array.shape[0]):
                        if fuzz.partial_ratio(user_future,data_array[i][9])>80:
                                flag = 1
                                print "(Relevance = "+ str(fuzz.ratio(user_future,data_array[i][9])) + ") ",
                                if data_array[i][0] != '':
                                        print "Bachelors : "+ data_array[i][0],
                                if data_array[i][3] != '':
                                        print "-> Masters : "+ data_array[i][3],
                                if data_array[i][6] != '':
                                        print "-> Doctoral : "+ data_array[i][6],
                                print "-> " + data_array[i][9],
                                print "\n"
