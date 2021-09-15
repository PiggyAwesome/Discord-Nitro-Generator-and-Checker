import requests
import os
import time
import json
import random

print(r"""
   _____________________________________________________
  /- /- /- /- /- /- /- /- /- \- \- \- \- \- \- \- \- \-\_\
 / / / /                                          \  \  \_\
/ / / /  NNNN  N   IIIII  TTTTT  RRRRR     O  O    \  \  \_\
\ \ \ \  N  NN N    II      T    RRRRR    O    O   /  /  /_/
 \ \ \ \ N     N   IIIII    T    R   RR    O  O   /  /  /_/
  \- \- \             Checker                    /- /- /_/
""")
dire = input("Enter codes directory: ")

with open(dire, "r") as codes:
    codes = codes.read().splitlines()

works = input("Enter directory to save woking codes: ")

os.system("cls")
print(f"Checking {codes.__len__()} codes")

with open("proxies.txt", "r") as proxy_file:
  proxy = proxy_file.read().splitlines()

def proxies():
  proxies = {
    "http:": random.choice(proxy),
    "https": random.choice(proxy)
  }
  return proxies

for code in codes:
  try:
    cleanCode = code.split("https://discord.gift/")

    response = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{cleanCode}?with_application=false&with_subscription_plan=true", proxies=proxies())
  
    while response.status_code == 429:
        response = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{cleanCode}?with_application=false&with_subscription_plan=true", proxies=proxies())
    msg = json.dumps(response.text)["message"]
    print(f"{code} | {msg}")
    if response.status_code != 404:
        works.write(code)

  except KeyboardInterrupt:
    exit()

  except:
      pass
    