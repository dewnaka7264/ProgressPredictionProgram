# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#UOW ID:- 19540456
#Date:- 12/2/2022

pass_credit=0 #defining the variables
defer_credit=0
fail_credit=0

progress_count=0 #defining the variables 
trailer_count=0
exclude_count=0
retriever_count=0
total_count=0

def Range(x): # Define a function to check the range of any input(x)
    if x not in (0,20,40,60,80,100,120):
        print("Out of valid range!")


        
def histogram(Level_name,y): # Define a function to print the histogram output
    print(Level_name,y,": ",y*"*" )

while True: # To loop the below block of code 
    try: # To handle an expected error
        pass_credit=int(input("Enter your Pass credit: "))# user can input
        Range(pass_credit)# User defined function
        defer_credit=int(input("Enter your Defer credit: "))
        Range(defer_credit)
        fail_credit=int(input("Enter your Fail credit: "))
        Range(fail_credit)  
        if pass_credit+defer_credit+fail_credit==120: # To step to the nested if, this if condition must be true.
            if pass_credit==120 and defer_credit==0 and fail_credit==0:
                print("Progress")
                progress_count+=1 # To count the histogram, program collects data
            elif pass_credit==100 and defer_credit in (20,0) and fail_credit in (0,20):
                print("Progress(module trailer)")
                trailer_count+=1
            elif pass_credit in (80,60,40,20,0) and defer_credit in (0,20,40,60,80,100,120) and fail_credit in (0,20,40,60):
                print("Do not Prgress-module retriever")
                retriever_count+=1
            elif pass_credit in (40,20,0) and defer_credit in (0,20,40) and fail_credit in (80,100,120):
                print("Exclude")
                exclude_count+=1
        else:
            print("Total incorrect") # If the first if condition is false, then this will be executed. 
        total_count+=1 # Counts the total count of sets of data.
    except ValueError: # this will handle the expected value error.
         print("Integer required") 

    print("  ")    
    Enter_more_data=str(input("Would you like to check another set of data?\nEnter 'y' for yes or 'q' to exit and view results: "))# Users choice to continue the program or stop and check the results.
    
    if Enter_more_data=="y":
        continue # This will continue the loop and again will ask to input credits
    elif Enter_more_data=="q": # will exit the loop and display the histogram
        print("-"*60)
        print("  ")
        print("Histogram")
        histogram("Progress",progress_count)
        histogram("Progress(module trailer)",trailer_count)
        histogram("Do not Prgress-module retriever",retriever_count)
        histogram("Exclude",exclude_count)
        print("  ")
        print(total_count, "outcomes in total")
        print("-"*60)
        break # Will stop the while true loop
    else:
        break # If something entered other than "y" or "q" program stops 



        
        
            
            
            
            
        
 
    


    

    

        
