import random

f_num = random.randint(1,100)
iteration = 0

while True:
  guess = int(input("Guess The between 1 to 100 : "))
  iteration += 1
  if guess == f_num:
      print(f"Congratulation you guess the Write Number In {iteration} Try..\n")
      break
  elif guess < f_num:
      print("Please Guess the Bigger Number..\n")
  elif guess > f_num:
      print("Please Guess the Lower Number..\n")
  else:
      print("Please Enter The Valid Input..\n")
