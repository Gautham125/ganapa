class node:
    def __init__(self,data):
        self.data=data
        self.rlink=None
        self.llink=None
class dlist:
    def __init__(self):
        self.start=None

    def insert(self,data):
        nn=node(data)
        if self.start==None:
            self.start=nn
            return
        else:
            nn.rlink=self.start
            self.start.llink=nn
            self.start=nn

    def delete(self):
        if self.start==None:
            print("Empty list")
        else:
            temp=self.start
            print("Deleted item is",temp.data)
            self.start=self.start.rlink
            self.start.llink=None
            
    def display(self):
        temp=self.start
        print("The status of list is:")
        if self.start==None:
            print("Empty list")
        else:
            while(temp!=None):
                print(temp.data)
                temp=temp.rlink
               
    def exit():
        sys.exit()

import sys
l=dlist()
while True:
    print("Select your choice:\n1: Insert\n2:Delete\n3:Display\n4:Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        item=int(input("Enter an item to insert: "))
        l.insert(item)
        l.display()
    elif choice==2:
        l.delete()
        l.display()
    elif choice==3:
        l.display()
    elif choice==4:
        exit()
    else:
        print("Wrong choice")