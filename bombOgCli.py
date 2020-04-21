import bombOg as b
import getpass
un=getpass.getuser()
pn=input("Enter number : ")
n=int(input("Enter limit : "))
cc=str(91)
if b.ifExists(un):
    if b.checkQuota(b.getUserDetails(un)):
        if b.blackList(pn):
            b.startBombing(pn,cc,n,un)
        else:
            print("This number has been blacklisted")
            exit()
