#importing mysql and declaring variables
import mysql.connector
myconnection=""
cursor=""
username=""
password=""

#module to check mysql connectivity
def mysqlconnectioncheck():
    global myconnection
    global username
    global password
    username=input("\n ENTER MYSQL SERVER'S USERNAME:")
    password=input("\n ENTER MYSQL SERVER'S PASSWORD:")
    myconnection=mysql.connector.connect(host="localhost",user=username,passwd="2004" )
    if myconnection:
        print("\n CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEENESTABLISHED !")
        cursor=myconnection.cursor()
        cursor.execute("create database if not exists school")
        cursor.execute("use school")
        cursor.close()
        return myconnection
    else:
        print("ERROR ESTABLISHING MYSQL CONNECTION")

#module to establish mysql connection

def mysqlconnection():
    global username
    global password
    global myconnection
    myconnection=mysql.connector.connect(host="localhost",user=username,passwd=password , database="school")
    if myconnection:
        return myconnection
    else:
        print("\n ERROR ESTABLISHING MYSQL CONNECTION !")
    myconnection.close()

#module for homescreen
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n ★★★★★★★★★★★★★★★ SCHOOL DATA MANAGER ★★★★★★★★★★★★★★★")
print("\n --------------------WELCOME------------------------")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#module for new admission
def admission():
    if myconnection:
        cursor=myconnection.cursor()
        cursor.execute("create table if not exists student(studentname varchar(30), phone varchar(12), address varchar(100), sclass varchar(5), section varchar(5), roll_no varchar(5), admission_no varchar(10))")
        name=input("\n ENTER STUDENT'S NAME : ")
        phone=input("ENTER PHONE NUMBER :")
        address=input("ENTER ADDRESS :")
        sclass=input("ENTER CLASS :")
        section=input("ENTER SECTION :")
        roll_no=input("ENTER ROLL NUMBER:")
        admission_no=input("ENTER ADMISSION NUMBER :")
        sql="insert into student values(%s,%s,%s,%s,%s,%s,%s)"
        values=(name,phone,address,sclass,section,roll_no,admission_no)
        cursor.execute(sql,values)
        cursor.execute("COMMIT")
        cursor.close()
        print("\n New Student Enrolled Successfully :) ")
    else:
        print("\n ERROR ESTABLISHING CONNECTION")

#module to display students data
def displaystudentdata():
    cursor=myconnection.cursor()
    if myconnection:
        cursor.execute("select * from student")
        data=cursor.fetchall()
        print(data)
        cursor.close()
    else:
        print("\n something went wrong, please try again ...")

#module to update students data
def updatestudentdata():
    cursor=myconnection.cursor()
    if myconnection:
        admission_no=input("ENTER ADMISSION NO:")
        sql="select * from student where admission_no=%s"
        cursor.execute(sql,(admission_no,))
        data=cursor.fetchall()
        if data:
            print("PRESS 1 FOR NAME")
            print("PRESS 2 FOR CLASS")
            print("PRESS 3 FOR ROLL NO")
            choice=int(input("Enter your choice"))
            if choice==1:
                name=input("ENTER NAME OF THE STUDENT :")
                sql="update student set name=%s where admission_no=%s"
                cursor.execute(sql,(name,admission_no))
                cursor.execute("commit")
                print("NAME UPDATED ")
            elif choice==2:
                std=input("ENTER CLASS OF THE STUDENT= :")
                sql="update student set sclass=%s where admission_no=%s"
                cursor.execute(sql,(std,admission_no))
                cursor.execute("commit")
                print("CLASS UPDATED")
            elif choice==3:
                roll_no=int(input("ENTER ROLL NO OF THE STUDENT :"))
                sql="update student set roll_no=%s where admission_no=%s"
                cursor.execute(sql,(roll_no,admission_no))
                cursor.execute("commit")
                print("ROLL NO UPDATED")
            else:
                print("NO RECORD FOUND")
                cursor.close()
    else:
        print("\n TRY AGAIN")
    #updatestudentdata

#MODULE TO ENTER MARKS OF STUDENT
def studentmarks():
    if myconnection:
        cursor=myconnection.cursor()
        createtable="create table if not exists marks1(admission_no varchar(20),physics int(5),chemistry int(5),maths int(5),computer int(5),english int(5),totalint(10))"
        cursor.execute(createtable)
        admission_no=input("\n ENTER ADMISSION NUMBER OF THE STUDENT:")
        physics=int(input("\n ENTER MARKS OF PHYSICS :"))
        chemistry=int(input("\n ENTER MARKS OF CHEMISTRY :"))
        maths=int(input("\n ENTER MARKS OF MATHS : "))
        computer=int(input("\n ENTER MARKS OF COMPUTER :"))
        english=int(input("\n ENTER MARKS OF ENGLISH :"))
        total=physics+chemistry+maths+computer+english
        sql="insert into marks1 values(%s,%s,%s,%s,%s,%s,%s)"
        values=(admission_no,physics,chemistry,maths,computer,english,total)
        cursor.execute(sql,values)
        cursor.execute("commit")
        print("\n MARKS OF STUDENT ENTERED SUCCESSFULLY !")
    else:
        print("\n ERROR ESTABLISHING MYSQL CONNECTION !")

#MODULE TO GENERATE REPORT CARD OF ALL STUDENTS
def allstudents_reportcard():
    cursor=myconnection.cursor()
    if myconnection:
        cursor.execute("select * from marks1")
        data=cursor.fetchall()
        print(data)
        cursor.close()
    else:
        print("\n TRY AGAIN")

#MODULE TO GENERATE REPORT CARD OF ONE STUDENT
def reportcardonestudent():
    cursor=myconnection.cursor()

    if myconnection:
        admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
        cursor=myconnection.cursor()
        sql=("select * from marks1 where admission_no=%s")
        cursor.execute(sql,(admission_no,))
        data=cursor.fetchall()
        if data:
            print(data)
        else:
            print("RECORD NOT FOUND ,TRY AGAIN")
    else:
        print("\n TRY AGAIN")

#MODULE TO ENTER FEES OF STUDENTS
def studentfee() :
    if myconnection:
        cursor=myconnection.cursor()
        createtable ="create table if not exists fees (admission_no varchar(10),month int (10) ,tution_fees int (10) ,lab_fee int(5),total int( 15))"
        cursor.execute(createtable)
        admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
        month=int(input("\n ENTER MONTH (1-12) : "))
        tution_fee=int(input("\n ENTER TUTION FEES : "))
        lab_fee=int(input("\n ENTER LAB FEES : "))
        total = tution_fee+lab_fee
        sql="insert into fees values(%s,%s,%s,%s,%s)"
        values=(admission_no,month,tution_fee,lab_fee,total)
        cursor.execute(sql,values)
        cursor.execute("commit")
        cursor.close()
        print("\n Fees paid successfully !")
    else:
        print("\n ERROR ESTABLISHING MYSQL CONNECTION")

#MODULE TO GENERATE FEES RECEIPT OF ALL STUDENTS
def feerecieptallstudent():
    ursor=myconnection.cursor()
    if myconnection:
        cursor.execute("select * from fees")
        data=cursor.fetchall()
        print(data)
        cursor.close()
    else:
        print("\n TRY AGAIN ")

#MODULE TO GENERATE FEES RECEIPT OF ONE STUDENT
def feereceipt_onestudent():
    cursor=myconnection.cursor()
    if myconnection:
        admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
        cursor=myconnection.cursor()
        sql="select * from fees where admission_no=%s"
        cursor.execute(sql,(admission_no,))
        data=cursor.fetchall()
        if data:
            print(data)
    else:
        print("\n TRY AGAIN")

#MODULE TO ISSUE TC
def studenttc():
    cursor=myconnection.cursor()
    if myconnection:
        admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
        cursor=myconnection.cursor()
        sql="select * from student where admission_no=%s"
        cursor.execute(sql,(admission_no,))
        data=cursor.fetchall()
        if data:
            sql=("delete from student where admission_no=%s")
            cursor.execute(sql,(admission_no,))
            cursor.execute("commit")
            print("STUDENT'S TRANSFER CERTIFICATE GENERATED ")
    else:
        print("\n TRY AGAIN")

#module for menu

myconnection=mysqlconnectioncheck()

if myconnection:
    mysqlconnection()
def menu():
    while(True):
        print("\n\n")
        print("=========================================================")
        print("\t ENTER 1 - NEW ADMISSION")
        print("\t ENTER 2 - DISPLAY STUDENTS DATA")
        print("\t ENTER 3 - UPDATE STUDENT'S DATA")
        print("\t ENTER 4 - PAY STUDENT'S FEE")
        print("\t ENTER 5 - ISSUE TRANSFER CERTIFICATE")
        print("\t ENTER 6 - ADD STUDENT'S MARK DETAILS")
        print("\t ENTER 7 - GENERATE ALL STUDENTS REPORT CARD")
        print("\t ENTER 8 - GENERATE STUDENT WISE REPORT CARD")
        print("\t ENTER 9 - GENERATE ALL STUDENTS FEE RECIEPT")
        print("\t ENTER 10 -GENERATE STUDENT WISE FEE RECIEPT ")
        print("\t ENTER 11 -EXIT ")
        print("=========================================================")
        choice=int(input("PLEASE ENTER YOUR CHOICE :"))
        if choice==1:
            admission()
        elif choice==2:
            displaystudentdata()
        elif choice==3:
            updatestudentdata()
        elif choice==4:
            studentfee()
        elif choice==5:
            studenttc()
        elif choice==6:
            studentmarks()
        elif choice==7:
            allstudents_reportcard()
        elif choice==8:
            reportcardonestudent()
        elif choice==9:
            feerecieptallstudent()
        elif choice==10:
            feereceipt_onestudent()
        elif choice==0:
            j=0
            return j
        else:
            print("Wrong input try again")

menu()

#END OF THE CODE