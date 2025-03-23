def pedirName():
  name= input("What's your name? ")
  age= int(input("{} How old are you?:  ".format(name)))
  print("Wellcome at the project {}, being {} is great ".format(name.upper(), age))
  print("See you soon")
  
if __name__ == '__main__':  
  pedirName()
