print("Contact book")
while(True):
    print("Enter 1 for adding contact\nEnter 2 for searching contact\nEnter 3 for displaying contact\nEnter 4 to delete contact\nEnter 5 to update contact\nEnter 6 to exit")
    n=int(input("enter choice:"))

    if n==1:
        with open("contact.text","a") as f: 
            name=input("enter name:")
            cont=input("enter number:")
            add=input("enter address:")
            f.write(f'name={name} || contact={cont} || address={add}\n')
        print("Contact Saved")
        continue
    elif n==2:
        num=input("enter number:")
        with open("contact.text","r") as con:
            for line in con:
                if num in line:
                    print(line)            
        print("successfully Retrieved")
        continue
    elif n==3:
        with open("contact.text","r") as fl:
            disp=list(fl.readlines())
            for itm in disp:
                print(itm)
        continue
    elif n==4:
        num=input('enter number or name to delete contact :')
        file = open("contact.text", "r")
        lines = file.readlines()
        new_lines = []
        for line in lines:
            if num not in line.strip():
                new_lines.append(line)
        file.close()
        file = open("contact.text", "w")
        file.writelines(new_lines)
        file.close()
        print('Contact Deleted')
    elif(n==5):
        search_text = input("enter old number : ")
        replace_text =input("enter new number:")


        with open('contact.text', 'r') as file:
            data = file.read()
            data = data.replace(search_text, replace_text)

        with open('contact.text', 'w') as file:
            file.write(data)

        print("Successfully Updated")

    elif n==6:
        break



   
    



