# Author: SCT (AMDG) 4/12/22

class tv_remote:  # def class
    def __init__(self, channel=0, volume_level=0, on=False):  # sets all base value parameters for tv
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
    def __str__(self): # if statement for tv on
        if self.on == True:
            return "The TV is on channel {0} at volume level {1}.".format(self.channel, self.volume_level) # str format for print
        else:   # else statment for tv being off
            return "The TV is off."


# function calls and print statement
my_remote = tv_remote()
my_remote.on = True
print(my_remote)