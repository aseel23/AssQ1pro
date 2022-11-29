Name =input("please enter your name:")
Age =input("please enter your age:")
Address =input("please enter your located address:")
Sen="Hello Mr/Mrs"
# Name,Age.Address is str

if not  Name.isdigit() and not Name.isspace():
  if Age.isdigit() and not Age.isspace():
    if not Address.isspace():
      print(Sen+" "+ Name+" "+"age"+"{"+Age+"}"+" "+"located in"+"{"+ " " +Address+"}"+"\n"+"thanks for beening one of our community.")
    else:
        print("wrong message")
  else:
      print("wrong message")


else:
     print("wrong message")