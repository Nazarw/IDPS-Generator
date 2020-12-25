from xeger import Xeger
import threading
x = Xeger(limit=10)  # default limit = 10

def Generate():
    idps_regex = x.xeger("0{7}10{2}8[456789ACE]000[6789ABCD][01F][04][0123][0123456789ABCDEF]{13}")
    print(idps_regex)
    with open("idps.txt","a") as generated:
        generated.write(idps_regex + "\n")

while True:
    while threading.active_count() < int(100):
        threading.Thread(target=Generate()).start()
input()