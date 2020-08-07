#imports

import tkinter as tk
import tkinter as Tk
import tkinter
from tkinter import *
from tkinter.ttk import *
import webbrowser
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from PIL import Image,ImageTk

from matplotlib import rcParams
from matplotlib.cm import rainbow

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

#definitions

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))


def takeInput():
    inputValues = []

    
    age1 = ((int(age.get()) - 29)  / (77-29 ))
    print(age1)
    trestbps1 = ((int(rbp.get()) - 94)/(200-94))
    chol1 = ((int (serumChol.get()) - 126)/(564-126))
    thalach1 = ((int(thalach.get()) - 71)/(202-71))
    oldpeak1 = (float(oldpeak.get())/ (6.2))
    
    inputValues.append(age1)
    inputValues.append(sex.get())
    inputValues.append(chestPain.get())
    inputValues.append(trestbps1)
    inputValues.append(chol1)
    inputValues.append(FBS.get())
    inputValues.append(ECG.get())
    inputValues.append(thalach1)
    inputValues.append(trestbps1)
    inputValues.append(oldpeak1)
    inputValues.append(slope.get())
    inputValues.append(ca.get())
    inputValues.append(thal.get()) 
    
    print(inputValues)


    print("\n") 
    final_Result = knn_classifier.predict([inputValues])
    print(final_Result)
    

    substituteWindow = tkinter.Tk()
    substituteWindow.geometry('640x480-8-200')
    substituteWindow.title("RESULT PREDICTION")
    substituteWindow.iconbitmap('logo.ico')
    
    substituteWindow.columnconfigure(0, weight=2)
    substituteWindow.columnconfigure(1, weight=1)
    substituteWindow.columnconfigure(2, weight=2)
    substituteWindow.columnconfigure(3, weight=2)
    substituteWindow.rowconfigure(0, weight=1)
    substituteWindow.rowconfigure(1, weight=10)
    substituteWindow.rowconfigure(2, weight=10)
    substituteWindow.rowconfigure(3, weight=1)
    substituteWindow.rowconfigure(4, weight=1)
    substituteWindow.rowconfigure(5, weight=1)
    
    if final_Result[0] == 1:
        label1 = tkinter.Label(substituteWindow, text="HIGH CHANCES OF CARDIAC FAILURE", font=('Impact', -35), fg='Red')
        label1.grid(row=0, column=1, columnspan=6)
        
        label12 = tkinter.Label(substituteWindow, text="---------------------------------------------------------------", font=('Impact', -35), fg='#0080ff')
        label12.grid(row=1, column=1, columnspan=6)

        Button = tkinter.Button(substituteWindow, text="Result-Graphs", font=('Impact', -15), bg = '#ff704d', command=plot)
        Button.grid(row=1, column=1, columnspan=6)

        label13 = tkinter.Label(substituteWindow, text="Nearest Coronary Care Unit(CCU):-", font=('Impact', -20), fg='#0080ff')
        label13.grid(row=2, column=1)

        label04= tkinter.Label(substituteWindow, text="Name:- ", font=('Impact', -17), fg='Black')
        label04.grid(row=3, column=1)
        label14= tkinter.Label(substituteWindow, text=" Mauli Dialysis Center", font=('Impact', -17), fg='gray')
        label14.grid(row=3, column=2)

        label05 = tkinter.Label(substituteWindow, text="Contact number:- ", font=('Impact', -17), fg='Black')
        label05.grid(row=4, column=1)
        label15= tkinter.Label(substituteWindow, text="(+91) 8698477331", font=('Impact', -17), fg='gray')
        label15.grid(row=4, column=2)

        label06 = tkinter.Label(substituteWindow, text="Email ID:-", font=('Impact', -17), fg='Black')
        label06.grid(row=5, column=1)
        label16 = tkinter.Label(substituteWindow, text=" lphgpct@gmail.com ", font=('Impact', -17), fg='gray')
        label16.grid(row=5, column=2)

        label07 = tkinter.Label(substituteWindow, text="Address:- ", font=('Impact', -17), fg='Black')
        label07.grid(row=6, column=1)
        label17 = tkinter.Label(substituteWindow, text=" Mauli Tower, Shegaon 444203", font=('Impact', -17), fg='gray')
        label17.grid(row=6, column=2)

        label18 = tkinter.Label(substituteWindow, text="Click he link for more details", font=('Impact', -17), fg='Black')
        label18.grid(row=7, column=1)

        lbl = tk.Label(substituteWindow, text=r"http://maulidialysis.mauligroup.org/index.html", fg="black", cursor="hand2")
         
        lbl.bind("<Button-1>", callback)
        lbl.grid(row=7, column=2)

        label12 = tkinter.Label(substituteWindow, text="---------------------------------------------------------------", font=('Impact', -35), fg='#0080ff')
        label12.grid(row=9, column=1, columnspan=6)
        
        
      
    else: 
        label1 = tkinter.Label(substituteWindow, text="NO DETECTIOIN OF CARDIAC FAILURE", font=('Impact', -35) )
        label1.grid(row=2, column=1, columnspan=6)
        
        Button = tkinter.Button(substituteWindow, text="Result-Graphs", font=('Impact', -15), bg = '#ff704d', command=plot)
        Button.grid(row=3, column=1, columnspan=6)

        label2 = tkinter.Label(substituteWindow, text="Do not forget to exercise daily. ", font=('Impact', -20), fg='green')
        label2.grid(row=4, column=1, columnspan=6)      
        
    substituteWindow.mainloop()
        


heart = pd.read_csv("heart.csv")

min_max = MinMaxScaler()
columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
heart[columns_to_scale ] = min_max.fit_transform(heart[columns_to_scale])
y = heart['target']
X = heart.drop(['target'], axis = 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)




def about():
    image=Image.open('Aboutus.png')
    image.show()
 
    
def about_system():
    image=Image.open('AboutSys.png')
    image.show()
    
    
def details():
    
    master = Tk() 
    label00 = tkinter.Label(master, text="Close me", font=('Algerian', -35) ,bg ='#ffad99')
    label00.grid(row=0, column=0, columnspan=3)
    text1 = tk.Text(mainWindow)
    photo = tk.PhotoImage(file='D:\Project\Files\detail1.png')
    text1.insert(tk.END, '\n')
    text1.image_create(tk.END, image=photo)
    text1.grid( row=1, rowspan=7, column=3)
    master.mainloop() 
    
#Graph-Ploting

def plot ():
      
        a=knn_classifier.score(X_test,y_test)*100
        b=svclassifier.score(X_test,y_test)*100
        c=classifier.score(X_test,y_test)*100
        d=model.score(X_test,y_test)*100
                
        result = []
        result.append(a)
        result.append(b)
        result.append(c)
        result.append(d)
        print(result)
    
        algorithms = ['KNN', 'SVM', 'DT', 'RF']
        colors = rainbow(np.linspace(0, 1, len(algorithms)))
        plt.bar(algorithms, result, color = colors)
        for i in range(len(algorithms)):
            plt.text(i, result[i], result[i])
        plt.xlabel('Algorithms')
        plt.ylabel('Scores')
        plt.title('Graphical Representation')
        canvas = FigureCanvasTkAgg(plt, master=mainWindow)
        canvas.get_tk_widget().pack()
        canvas.draw()
      
        
#Algorithms implemention
        
print(len(X_train))
len(X_test)
knn_score = []
knn_classifier = KNeighborsClassifier(n_neighbors = 4)
knn_classifier.fit(X_train, y_train)
knn_score.append(knn_classifier.score(X_test, y_test))


sv_score = []
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)
sv_score.append(svclassifier.score(X_test, y_test))


DT_score = []
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
DT_score.append(classifier.score(X_test, y_test ))


RF_score = []
model = RandomForestClassifier()
model.fit(X_train, y_train)
RF_score.append(model.score(X_test, y_test ))





#Tkinter user Interface

mainWindow = tkinter.Tk()
mainWindow.geometry('2000x600')
mainWindow['padx']=20
mainWindow.configure(bg='#ffad99')
mainWindow.title("CARDIAC FAILURE PREDICTION SYSTEM")
mainWindow.iconbitmap('logo.ico')


mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=2)
mainWindow.rowconfigure(0, weight=0)
mainWindow.rowconfigure(1, weight=0)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)
mainWindow.rowconfigure(6, weight=1)
mainWindow.rowconfigure(7, weight=1)
mainWindow.rowconfigure(8, weight=10)


menubar = Menu(mainWindow)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="About us", command = about)
filemenu.add_command(label = "About System", command = about_system)



menubar.add_cascade(label = "Details", command = details)
menubar.add_cascade(label = "About", menu = filemenu)
menubar.add_cascade(label = "Exit", command = mainWindow.quit())
editmenu = Menu(menubar, tearoff=0)

mainWindow.config(menu = menubar)

label1 = tkinter.Label(mainWindow, text="Cardiac Failure Prediction System", font=('Algerian', -35) ,bg ='#ffad99')
label1.grid(row=0, column=0, columnspan=3)


ageFrame = tkinter.LabelFrame(mainWindow, text="Age(yrs)")
ageFrame.grid(row=2, column=0)
ageFrame.config(font=("Courier", -15),bg ='#ffad99')
age= tkinter.Entry(ageFrame)
age.grid(row=2, column=2, sticky='nw')

sexFrame = tkinter.LabelFrame(mainWindow, text="Gender")
sexFrame.grid(row=2, column=1)
sexFrame.config(font=("Courier", -15),bg ='#ffad99')
sex= tkinter.Entry(sexFrame)
sex.grid(row=2, column=2, sticky='nw')


chestPainFrame = tkinter.LabelFrame(mainWindow, text="CP (0-4)")
chestPainFrame.grid(row=2, column=2)
chestPainFrame.config(font=("Courier", -15),bg ='#ffad99')
chestPain= tkinter.Entry(chestPainFrame)
chestPain.grid(row=2, column=2, sticky='nw')

rbpFrame = tkinter.LabelFrame(mainWindow, text="RBP (94-200)")
rbpFrame.grid(row=3, column=0)
rbpFrame.config(font=("Courier", -15),bg ='#ffad99')
rbp= tkinter.Entry(rbpFrame)
rbp.grid(row=2, column=2, sticky='nw')

serumCholFrame = tkinter.LabelFrame(mainWindow, text="Serum Chol")
serumCholFrame.grid(row=3, column=1)
serumCholFrame.config(font=("Courier", -15),bg ='#ffad99')
serumChol = tkinter.Entry(serumCholFrame)
serumChol.grid(row=2, column=2, sticky='n')

FBSFrame = tkinter.LabelFrame(mainWindow, text="Fasting BS(0/1)")
FBSFrame.grid(row=3, column=2)
FBSFrame.config(font=("Courier", -15),bg ='#ffad99')
FBS= tkinter.Entry(FBSFrame)
FBS.grid(row=2, column=2, sticky='nw')

ECGFrame = tkinter.LabelFrame(mainWindow, text="ECG (0/1)")
ECGFrame.grid(row=4, column=0)
ECGFrame.config(font=("Courier", -15),bg ='#ffad99')
ECG = tkinter.Entry(ECGFrame)
ECG.grid(row=2, column=2, sticky='nw')


thalachFrame = tkinter.LabelFrame(mainWindow, text="thalach(71-202)")
thalachFrame.grid(row=4, column=1)
thalachFrame.config(font=("Courier", -15),bg ='#ffad99')
thalach = tkinter.Entry(thalachFrame)
thalach.grid(row=2, column=2, sticky='nw')

exangFrame = tkinter.LabelFrame(mainWindow, text="exAngina(0/1)")
exangFrame.grid(row=4, column=2)
exangFrame.config(font=("Courier", -15),bg ='#ffad99')
exang = tkinter.Entry(exangFrame)
exang.grid(row=2, column=2, sticky='nw')


oldpeakFrame = tkinter.LabelFrame(mainWindow, text="Old Peak(0-6.2)")
oldpeakFrame.grid(row=5, column=0)
oldpeakFrame.config(font=("Courier", -15),bg ='#ffad99')
oldpeak = tkinter.Entry(oldpeakFrame)
oldpeak.grid(row=2, column=2, sticky='nw')
  
slopeFrame = tkinter.LabelFrame(mainWindow, text="Slope(0,1,2)")
slopeFrame.grid(row=5, column=1)
slopeFrame.config(font=("Courier", -15),bg ='#ffad99')
slope = tkinter.Entry(slopeFrame)
slope.grid(row=2, column=2, sticky='nw')

caFrame = tkinter.LabelFrame(mainWindow, text=" C.A (0-3)")
caFrame.grid(row=5, column=2)
caFrame.config(font=("Courier", -15),bg ='#ffad99')
ca = tkinter.Entry(caFrame)
ca.grid(row=2, column=2, sticky='nw')


thalFrame = tkinter.LabelFrame(mainWindow, text=" THAL(0,1,2,3)")
thalFrame.grid(row=6, column=1)
thalFrame.config(font=("Courier", -15),bg ='#ffad99')
thal = tkinter.Entry(thalFrame)
thal.grid(row=2, column=2, sticky='nw')




text1 = tk.Text(mainWindow)
photo = tk.PhotoImage(file='D:\Project\Files\heart0.png')
text1.insert(tk.END, '\n')
text1.image_create(tk.END, image=photo)
text1.grid( row=1, rowspan=7, column=3)

label2 = tkinter.Label(mainWindow, text="To know how  to avoid a Cardiac attack or a stroke click the link below", font=('Impact') , fg='black')
label2.grid(row=7, column=3)

lbl = tk.Label(mainWindow, text=r"https://www.who.int/features/qa/27/en/", fg="black", cursor="hand2" ,bg ='#ffad99')

lbl.bind("<Button-1>", callback)
lbl.grid(row=8, column=3)




analyseButton = tkinter.Button(mainWindow, text="<<<<<ENTER>>>>>", font=('Impact', -15), bg = '#ff704d', command=takeInput)
analyseButton.grid(row=8, column=0, columnspan=3)



mainWindow.mainloop()


