#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#UOW ID:- 19540456
#Date:- 12/2/2022

pass_credit=0
defer_credit=0
fail_credit=0

progress_count=0
trailer_count=0
exclude_count=0
retriever_count=0
total_count=0


list1=[]
list2=[]
list3=[]
list4=[]
credit_level=0

file=None # defining the file
file=open("textfile.txt","w") # open the file to read the file


def Range(x):
    if x not in (0,20,40,60,80,100,120):
        print("Out of valid range!")


def histogram(Level_name,w):
    print(Level_name,w,": ",w*"*" )

def Listing(credit_level,pass_credit,defer_credit,fail_credit):
    if credit_level=="Progress":
        list1.append(pass_credit)
        list1.append(defer_credit)
        list1.append(fail_credit)
    elif credit_level=="Progress(module trailer)":
        list2.append(pass_credit)
        list2.append(defer_credit)
        list2.append(fail_credit)
    elif credit_level=="Do not Progress-module retriever":
        list3.append(pass_credit)
        list3.append(defer_credit)
        list3.append(fail_credit)
    elif credit_level=="Exclude":
        list4.append(pass_credit)
        list4.append(defer_credit)
        list4.append(fail_credit)


  
while True:
     
    try:
        pass_credit=int(input("Enter your Pass credit: "))
        Range(pass_credit)
        defer_credit=int(input("Enter your Defer credit: "))
        Range(defer_credit)
        fail_credit=int(input("Enter your Fail credit: "))
        Range(fail_credit)
        
        if pass_credit+defer_credit+fail_credit==120:
            if pass_credit==120 and defer_credit==0 and fail_credit==0:
                print("Progress")
                progress_count+=1
                credit_level=="Progress"
                line="Progress-"+str(pass_credit)+","+str(defer_credit)+","+str(fail_credit)# structure for the final print
                file.write(line)
                Listing("Progress",pass_credit,defer_credit,fail_credit)

            elif pass_credit==100 and defer_credit in (20,0) and fail_credit in (0,20):
                print("Progress(module trailer)")
                trailer_count+=1
                credit_level=="Progress(module trailer)"
                line="Progress(module trailer)-"+str(pass_credit)+","+str(defer_credit)+","+str(fail_credit)# structure for the final print
                file.write(line)
                Listing("Progress(module trailer)",pass_credit,defer_credit,fail_credit)

            elif pass_credit in (80,60,40,20,0) and defer_credit in (0,20,40,60,80,100,120) and fail_credit in (0,20,40,60):
                print("Do not Progress-module retriever")
                retriever_count+=1
                credit_level=="Do not Progress-module retriever"
                line="Do not Progress-module retriever-"+str(pass_credit)+","+str(defer_credit)+","+str(fail_credit)# structure for the final print
                file.write(line)
                Listing("Do not Progress-module retriever",pass_credit,defer_credit,fail_credit)
            
            elif pass_credit in (40,20,0) and defer_credit in (0,20,40) and fail_credit in (80,100,120):
                print("Exclude")
                exclude_count+=1
                credit_level=="Exclude"
                line="Exclude-"+str(pass_credit)+","+str(defer_credit)+","+str(fail_credit)# structure for the final print
                file.write(line)
                Listing("Exclude",pass_credit,defer_credit,fail_credit)
                
                 
        else:
            print("Total incorrect")
        total_count+=1
    except ValueError:
        print("Integer required")
        
    print("  ")    
    Enter_more_data=str(input("Would you like to check another set of data?\nEnter 'y' for yes or 'q' to exit and view results: "))
    if Enter_more_data=="y":
        continue
    elif Enter_more_data=="q":
        print("-"*60)
        print("Histogram")
        histogram("Progress",progress_count)
        histogram("Progress(module trailer)",trailer_count)
        histogram("Do not Progress-module retriever",retriever_count)
        histogram("Exclude",exclude_count)
        print("  ")
        print(total_count, "outcome(s) in total")
        print("-"*60)
        break
    else:
        break




    
file.flush()#content stored into file
file.close()# close the file


    

    
