print("-----Welcome to your personal diary!-----")
name = input("//enter your name : ")

ps = input("//enter password : ")
username = name 
password = ps
if username == name :
    with open("stored_password.csv", "r") as f:
        read = f.readlines()
        for line in read:
            stored_username, stored_password = line.strip().split(",")
            if username == stored_username :
                if stored_password == ps :

                 print("login sucessefully!")
                
                import details as dstl
                import sorting as srt
            

                 
        else :
               print("user not found!")
               

    print("-----enter your details to create a account-----")
    print(f"entered name :{name} ")
pass1 = input("// set your diary password: ")
pass2 = input("// re-entre your diary password: ")
if pass1 == pass2 :
    with open("stored_password.csv", "a") as f:
        f.writelines(str(f"{username},{pass1}"+"\n"))
    print("your diary is set up successfully!")
    import details as dlts
    import sorting as srt
  
else:
    print("password cant match!")
    exit()



