import random
import string
import os


print(r"""
   _____________________________________________________
  /- /- /- /- /- /- /- /- /- \- \- \- \- \- \- \- \- \-\_\
 / / / /                                          \  \  \_\
/ / / /  NNNN  N   IIIII  TTTTT  RRRRR     O  O    \  \  \_\
\ \ \ \  N  NN N    II      T    RRRRR    O    O   /  /  /_/
 \ \ \ \ N     N   IIIII    T    R   RR    O  O   /  /  /_/
  \- \- \             Generator                  /- /- /_/
""")


chars = string.ascii_letters + string.digits + ''
codes = []


ran = ''.join(random.choice(chars) for i in range(8))


file_ = input("Enter file where codes should be saved: ")
top = str(input("What message should be written at top of file?: "))
amount = int(input("Amount of codes: "))

os.system("cls")

for i in range(amount):
   nitro = ''.join(random.choice(chars) for i in range(16))
   codes.append(f"https://discord.gift/{nitro}")
   print(f"https://discord.gift/{nitro}")


codes = '\n'.join(codes)


with open(file_ ,"w") as file_:
    file_.write(f"{str(top)}\n{codes}")
