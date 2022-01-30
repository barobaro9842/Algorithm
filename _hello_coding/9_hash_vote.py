voted = {}

def check_voter(name):
    if voted.get(name):
       print("Out!")
    else:
        voted[name] = True
        print("Vote")

check_voter("tom")
check_voter("mike")
check_voter("mike")
