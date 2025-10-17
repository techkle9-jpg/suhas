
try:
  age=int(input("enter your age :"))
  if age >=18:
    print("you are eligible to vote")
  else:
    print("you are not eligible to vote")
except valueerror:
  print("please enter s valid integer")
