class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def listprint(self):
        printval=self.head
        while printval is not None:
            print(printval.data)
            printval=printval.next
    def _inset_at_Beginig(self,newdata):
        newnode=node(newdata)
        newnode.next=self.head
        self.head=newnode

l1=Linkedlist()
l1.head=node("toyota")
l2=node("BMW")
l3=node("Audi")
l4=node("Honda")
l1.head.next=l2
l2.next=l3
l3.next=l4
l1.listprint()
print("")
l1._inset_at_Beginig("benz")
l1.listprint()
l1._inset_at_Beginig("CHR")
print("")
l1.listprint()
