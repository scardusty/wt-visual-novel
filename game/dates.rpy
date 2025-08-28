init python:
    class day_time(object):
        def __init__(self):
            self.day = 1 # set this to whatever starting day is
            self.weekdays = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"] # arrange these so first weekday goes first
            self.time_of_day = ["day", "afternoon", "night"] # add or remove to increase time of day slots
            self.end_of_day = "night" # automatically picks last slot as end of day

        @property
        def weekday(self):
            return self.weekdays[(self.day-1)%7]

        @property
        def time(self):
            return self.time_of_day[0]

        def advance(self, increment = 1, days = 0):
            if not (increment + days): # no input
                increment = 1

            if days: # add to increment by length of time_of_day
                increment += days * len(self.time_of_day)

            while increment > 0: # loop through increments to shift timeslot and days forward
                if self.time_of_day[0] == self.end_of_day:
                    self.day += 1
                self.time_of_day.append(self.time_of_day.pop(0))
                increment -= 1 # reduce increment to escape loop after enough runs

default clock = day_time()

"""label potatoes:
    "{b}clock.day{/b} returns Day: {b}[clock.day]{/b}"
    "{b}clock.weekday{/b} returns Weekday: {b}[clock.weekday]{/b}"
    "{b}clock.time{/b} returns Time of Day: {b}[clock.time]{/b}"
    "{b}$ clock.advance(){/b} advances time"
    $ clock.advance() # advances time by one slot
    "Advanced 1 slot:\n\nDay [clock.day] ([clock.weekday]) [clock.time]"

    $ clock.advance(2) # advances time by two slots
    "Advanced 2 slots:\n\nDay [clock.day] ([clock.weekday]) [clock.time]"

    $ clock.advance(days=1) # advances one day
    "Advanced 1 day:\n\nDay [clock.day] ([clock.weekday]) [clock.time]"

    $ clock.advance(1,8) # advance 8 days and one slot
    "Advanced 1 slot and 8 days (note night to morning still advances addition day):\n\nDay [clock.day] ([clock.weekday]) [clock.time]"
    return
"""