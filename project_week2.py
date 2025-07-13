print("DATABASE\n")
while(True):
    print("1.Create\n2.Update\n3.Delete\n4.Search\n5.Display\n6.Exit")
    
    inp=int(input("enter choice:"))
    if(inp==1):
        n=int(input("enter no. of student:"))
        student=[]
        for u in range(0,n):
            id=int(input("enter a Roll number: "))
            q=input("enter name:")
            r=int(input("enter marks:"))
            student.append({"ID":id,"Name":q,"marks":r})
        continue 
            
    elif(inp==2):
        num1=int(input("enter Roll no. :"))
        for ptr in range(len(student)):
            for up in student:
                if(num1==student[ptr]["ID"]):
                    upmark=(input("enter new marks: "))
                    student[ptr]["marks"]=upmark
                break
        continue
    elif(inp==3):
        print("this action will delete the data from the database")
        dl=int(input("enter roll no."))
        for dle in range(len(student)):
            for ind in student:
                if(dl==student[dle]["ID"]):
                    print("found")
                    student.pop(dle)
            break

        continue
    elif(inp==4):
        src=int(input("enter roll no."))
        for u in range(len(student)):
            if(src==student[u]["ID"]):
                print("found")
                print(student[u])
        

        continue
    elif(inp==5):
        for show in range(len(student)):
            print(f"Rollno:{student[show]["ID"]}  |  Name:{student[show]["Name"]}  |  Marks:{student[show]["marks"]}")
            
        
    elif(inp==6):
        break