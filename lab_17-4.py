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
    def turn_on(self): # def actions for tv remote
        self.on = True
    def turn_off(self):
        self.on = False
    def volume_up(self, value):
        self.volume_level += value
    def volume_down(self, value):
        self.volume_level -= value
    def channel_up(self, value):
        self.channel += value
    def channel_down(self, value):
        self.channel -= value

# function calls and print statement
my_remote = tv_remote()
my_remote.on = True
my_remote.turn_on()
my_remote.turn_off()
my_remote.volume_up(7)
my_remote.volume_down(2)
my_remote.channel_up(8)
my_remote.channel_down(2)
my_remote.turn_on()
print(my_remote)