# Author: SCT (AMDG) 4/12/22

class TV_remote:
       """ represents a tv remote """
       def remote(self):
             """ Create a new remote """
             return 
       def __str__(self):
        """ To string method """
        return "The radius of the circle is {0}".format(self)

my_remote = TV_remote()
print(my_remote.__str__())