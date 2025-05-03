import pandas as pd
import numpy as np
#import sqlalchemys
import matplotlib.pyplot as plt  
df = pd.DataFrame() 
csv_file = "C:\\Users\\pathol.csv"
# name of function: read_csv_file 
# purpose: To read CSV file and create DataFrame df
def read_csv_file():
    df=pd.read_csv(csv_file)
    print(df)

# name of function: clear 
# purpose : clear output screen 
def clear():
    for x in range(10):      #X=0....9
        print() 
 
# name of function : data_analysis_menu 
# purpose : To generate a Data Analysis menu
def data_analysis_menu():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\nData Analysis MENU ')
        print('_'*100)
        print('1.  Reveal Details of all Patients\n')
        print('2.  Browse All Categories of Report\n')
        print('3.  Preview Top Records of Patients\n')
        print('4.  Preview Bottom Records of Patients\n')
        print('5.  Show Specific Category of Report\n')
        print('6.  Incorporate New patient Record\n')
        print('7.  Create New Category in Report\n')
        print('8.  Remove Existing Category of Report\n')
        print('9.  Erase Specific Record of a Patient\n')
        print('10. Specific Patient\'s COVID-19 Status Report\n')
        print('11. Data Overview\n')
        print('12. Exit (Back to Main Menu)\n')
        ch = int(input('Enter your choice:'))
        if ch == 1:
            print(df)
            wait = input()
        elif ch == 2:
            print(df.columns)
            wait = input()
        elif ch == 3:
             n = int(input('Enter Total rows you want to   show :'))
             print(df.head(n))
             wait = input()
        elif ch == 4:
            n = int(input('Enter Total rows you want to show :'))
            print(df.tail(n))
            wait = input()
        elif ch == 5:
             print(df.columns)
             col_name = input('Enter Column Name that You want to print : ')
             print(df[col_name])
             wait = input()
        elif ch==6:
            a = input('Enter Patient Name :')
            b = input('Enter Age :')
            c = input(' Enter Gender :')
            d = input(' Enter Blood Group :')
            e =input(' Enter Covid Test Report:')
            f=int( input(' Enter Sugar Level :'))
            g=int(input(' Enter Blood Pressure:'))
            h=float(input('Enter Hemoglobin:'))
            df.loc[len(df)]=[a,b,c,d,e,f,g,h]
            print(df)
            df.to_csv("C:\\Users\\pathol.csv",index=False)
            wait=input()
        elif ch==7:
            col_name = input('Enter new column name :')
            col_value =input('Enter default column value :')
            df[col_name]=col_value
            print(df)
            df.to_csv("C:\\Users\\pathol.csv",index=False)
            print('\n\n Press any key to continue....')
            wait=input()
        elif ch==8:
            print(df.columns)
            col_name =input('Enter column Name to delete :')
            del df[col_name]
            print(df)
            df.to_csv("C:\\Users\\pathol.csv",index=False)
            wait=input()
        elif ch==9:
            print("Choose row index  from df")
            index_no =int(input('Enter the Index Number that You want to delete from 1 - 34 :'))
            df = df.drop(index_no)
            df.to_csv("C:\\Users\\pathol.csv",index=False)
        #df.drop(index_no,inplace=True)
            print(df)
            print('\n\n Press any key to continue....')
            wait = input()
        elif ch==10:
            print("Row index from 1-34")
            v=int(input('enter row label'))
            print(df.loc[v+1 ,['Patient name','Covid Test']])
        elif ch==11:
            print(df.describe())
            print("\n\n Press any key to continue....")
            wait=input
        elif ch==12:
            break
        else:
            print("Invalid Choice")
            print('\n\n Press any key to continue....')
            wait = input

        
# name of function : graph 
# purpose : To generate a Graph menu
def graph():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\nGRAPH MENU ')
        print('_'*100)
        print('1. Line Graph: Age Distribution of Patients\n')
        print('2. Bar Graph: Sugar Levels Across Patients\n')
        print('3. Bar Graph: Blood Pressure Levels of Patients\n')
        print('4. Histogram: Number of Patients Across Different Age Group\n')
        print('5. Horizontal Bar Chart: Hemoglobin Levels of Patients\n')
        print('6. Exit (Back to MAIN MENU)\n')
        ch = int(input('Enter your choice:' ))
        if ch==1:
            x = df['Patient name']
            y= df['Age']
            plt.xticks(rotation='vertical')
            plt.xlabel('PATIENT NAME-->')
            plt.ylabel('AGE -->')
            plt.title('PLOT SHOWING AGE OF PATIENTS')
            plt.grid(True)
            plt.plot(x,y,'r*',linewidth=3,linestyle='solid',markeredgecolor='k')
            plt.show()
        elif ch==2:
            x=df.loc[:,'Patient name']
            y = df.loc[:,'Sugar Level(mg/dl)']
            plt.bar(x,y,color='pink')
            plt.xticks(rotation='vertical')
            plt.grid(True)
            plt.title("BAR GRAPH REPRESENTING SUGAR LEVEL OF PATIENTS")
            plt.xlabel('PATIENT NAME')
            plt.ylabel('SUGAR LEVEL')
            plt.show()
            wait= input()          
        elif ch==3:
            x=df['Patient name']
            y=df['Blood Pressure(mmhg)']
            plt.xticks(rotation='vertical')
            plt.grid(True)
            plt.title('BLOOD PRESSURE OF PATIENTS')
            plt.xlabel('PTAIENTS NAME-->')
            plt.ylabel('BLOOD PRESSURE-->')
            plt.bar(x,y,color='yellow',edgecolor='b')
            plt.show()
        elif ch==4:
            x=df['Age']
            plt.title('HISTOGRAM DISPLAYING NO. OF PATIENTS OF DIFF. AGE GROUP')
            plt.xlabel('AGE OF PATIENTS-->')
            plt.ylabel('NO. OF PATIENTS-->')
            plt.hist(x,color='silver',edgecolor='k',bins=range(0,61,5))
            plt.xticks(range(0,61,5))
            plt.show()
        elif ch==5:
            y=df['Patient name']
            x=df['Hemoglobin(g/dl)']
            plt.title('BARCHART DISPLAYING HEMOGLOBIN OF PATIENTS')
            plt.ylabel('NAME OF PATIENTS-->')
            plt.xlabel('HEMOGLOBIN(g/dl) OF PATIENTS -->')
            plt.barh(y,x,color='cyan',edgecolor='black')
            plt.show()
        elif ch==6:
            break 
 


# function name          : export_menu 
# purpose                : function to generate export menu
def export_menu():    
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\nEXPORT MENU ')
        print('_'*100)
        print()
        print('1.  CSV File\n')
        print('2.  Exit (Back to MAIN MENU)')
        ch = int(input('Enter your Choice : '))
        if ch==1:
            df.to_csv('C:\\Users\\export.csv') 
            print('\nCheck your patients record  on C: Drive(export.csv).....') 
            wait = input()
        elif ch == 2:
            break 
    
 



def main_menu():
    while True:
        clear()
        print('MAIN MENU ')
        print('_'*100)
        print('1.  Read CSV File')
        print()
        print('2.  Data Analysis Menu\n')
        print('3.  Graph Menu\n')
        print('4.  Export Data\n')
        print('5.  Exit\n')
        choice = int(input('Enter your choice :'))
        if choice==1:
            read_csv_file()
            wait=input()
        elif choice==2:
            data_analysis_menu()
            wait=input()
        elif choice==3:
            graph()
            wait=input()
        elif choice==4:
            export_menu()
            wait=input()
        elif choice==5:
            break
           
 # call your main menu
main_menu()


