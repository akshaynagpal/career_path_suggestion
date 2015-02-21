from Tkinter import *
import tkMessageBox
from numpy import array
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv

cd_list = []

# opening csv file

with open("C:\/Users\/advance\/Documents\/GitHub\/career_path_prediction\/Career_data.csv",'rb') as csvfile:
    filereader = csv.reader(csvfile,delimiter=',')
    for row in filereader:
        cd_list.append(row)

data_array = array(cd_list)  # making an array from list of lists

def predictor(str1,inp):
    print str1
    user_input = inp
    user_future = user_input.title()
    user_output = []
    count_result = -1
    
    if str1 == 'HS':
        flag = 0
        for i in range(1,data_array.shape[0]):   
            if fuzz.ratio(user_future,data_array[i][9])>60:
                flag = 1
                count_result += 1
                user_output.append([str(count_result)])
                user_output[count_result].append(str(fuzz.ratio(user_future,data_array[i][9])))
                if data_array[i][0] != '':
                    user_output[count_result].append("Bachelors :" + data_array[i][0])
                if data_array[i][3] != '':
                    user_output[count_result].append("Masters :" + data_array[i][3])
                if data_array[i][6] != '':
                    user_output[count_result].append("Doctoral :" + data_array[i][6]) 
                user_output[count_result].append(data_array[i][9])
                
        if flag == 0: #No simple ratio match, try partial match
            print "No simple ratio match...trying for partial match..."
            for i in range(1,data_array.shape[0]):      
                if fuzz.partial_ratio(user_future,data_array[i][9])>80:
                    flag = 1
                    count_result += 1
                    user_output.append([str(count_result)])
                    user_output[count_result].append(str(fuzz.partial_ratio(user_future,data_array[i][9])))
                    if data_array[i][0] != '':
                        user_output[count_result].append("Bachelors :" + data_array[i][0])
                    if data_array[i][3] != '':
                        user_output[count_result].append("Masters :" + data_array[i][3])
                    if data_array[i][6] != '':
                        user_output[count_result].append("Doctoral :" + data_array[i][6])
                    user_output[count_result].append(data_array[i][9])
                    
        return user_output
    
    elif str1 == 'B': #Bachelors selected
        flag = 0
        for i in range(1,data_array.shape[0]):   
            if fuzz.ratio(user_future,data_array[i][9])>60: #relevance > 60
                print "inside 1st loop "
                flag = 1
                count_result += 1
                user_output.append([str(count_result)])
                user_output[count_result].append("Relevance:" + str(fuzz.ratio(user_future,data_array[i][9])))
                if data_array[i][3] != '':
                    user_output[count_result].append("Masters :" + data_array[i][3])
                if data_array[i][6] != '':
                    user_output[count_result].append("Doctoral :" + data_array[i][6]) 
                user_output[count_result].append(data_array[i][9])
                
        if flag == 0:
            print "no simple ratio match...trying for partial match..."
            for i in range(1,data_array.shape[0]):      
                if fuzz.partial_ratio(user_future,data_array[i][9])>80: #partial relevance > 80
                    flag = 1
                    count_result += 1
                    user_output.append([str(count_result)])
                    user_output[count_result].append("Relevance:"+str(fuzz.partial_ratio(user_future,data_array[i][9])))
                    if data_array[i][3] != '':
                        user_output[count_result].append("Masters :" + data_array[i][3])
                    if data_array[i][6] != '':
                        user_output[count_result].append("Doctoral :" + data_array[i][6])
                    user_output[count_result].append(data_array[i][9])
                    
        return user_output
        

def help_callback():
    tkMessageBox.showinfo(
        "Help INFORMATION",
        "help help help"
        )
    return

def callback():
    if str(listbox1.curselection()) == str(('0',)):
        print "Zero Selected"
        text_box_input = str(e.get())
        x = predictor('HS',text_box_input)
        tkMessageBox.showinfo(
        "RESULT",
        '\n'.join(map('->'.join, x))
        )
    elif str(listbox1.curselection()) == str(('1',)):
        print "ONE SELECTED"
        text_box_input = str(e.get())
        x = predictor('B',text_box_input)
        tkMessageBox.showinfo(
        "RESULT",
        '\n'.join(map('->'.join, x))
        )
    return


root = Tk()
root.wm_title("Career Suggestion")
root.geometry("250x250")  #width x height
#creating menu
menu = Menu(root)

root.config(menu=menu)
helpmenu=Menu(menu)
menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="Help",command=help_callback)

frame = Frame(root, width=100, height=100)
w = Label(root,text = "Enter your target profession:")
w.pack(fill=X)
e = Entry(root)
e.pack(fill=X)

w0 = Label(root,text = "Select your current education:")
w0.pack(fill=X)
listbox1 = Listbox(root)
listbox1.pack(fill=X)
listbox1.insert(END,"High School")
listbox1.insert(END,"Bachelors")

b = Button(root,text="get",width=10,command=callback)
b.pack(fill=X)

root.mainloop()
