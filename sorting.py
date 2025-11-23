print("-----do you want to sort your diary entries? (yes/no)-----") 
srt = input("// ")
try :
   
 if srt == "yes":

   with open ("dairy.csv" , "r") as f:
    lines = f.readlines()
    lines.sort()
    
   with open ("dairy.csv" , "w") as f:
    f.writelines(lines)
    print("your diary is sorted successfully!")
 elif  srt == "no":
   print("okey! ")
 else :
    print("invalid input! ")
except :
 pass
print("Thank you for using your personal diary!")
exit()