class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_end(self, data):
        new_node = node(data)
        if (self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while (temp.next != None):
                tenp = temp.next
            temp.next = new_node


    def display(self):
        if(self.head==None):
            print("no data")
        else:
            temp=self.head
            while(temp!=None):
                print(temp.data,end="---->")
                temp=temp.next
    def delete_at_begin(self):
        if(self.head==None):
            print("no data")
        else:
            self.head=self.head.next
    def delete_at_end(self):
        if(self.head==None):
            print("no data")
        else:
            temp=self.head
            prev=None
            while(temp.next!=None ):
                temp=temp.next
            temp.prev=None
n1=sll()
n1.insert_at_beginning('22')
n1.insert_at_beginning('20')
n1.insert_at_beginning('06')

#n1.insert_at_end('07')
n1.delete_at_begin()
n1.delete_at_end()
n1.display()