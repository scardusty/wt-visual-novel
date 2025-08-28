init python:    
    

    class Player:

        #Starting player stats, 3 statblocks to choose from


        def __init__(self, stats, money = 2000, points = 4000, name = "pc", position = ""):
            self.name = name
            self.money = money
            self.points = points
            self.position = position
            self.points_highest = 4000 #starting value
            self.primary_trigger = maintrigger[0] #always
            self.trigger_highest = maintrigger[0] #starting value

            #Go through all the triggers and see which has the most points
            all_trigger_points = []
            for trigger in all_triggers:
                all_trigger_points.append(trigger.points)
                if trigger.points == max(all_trigger_points):
                    self.trigger_highest = trigger.name
            self.points_highest = max(all_trigger_points)

            self.base_stats = stats
            self.stats = self.base_stats.copy()
            self._stats_halved = self.stats

            self.setStats()


        # Stats with their values halved. 
        # honestly, the only reason i made this is so that 
        # the radar chart looks nicer (too many lines when the range is 10) 

        def stats_halved(self):
            self.OGstats = self.stats
            self._stats_halved = self.OGstats.copy()
            for i in self._stats_halved: 
                x = self.OGstats[i]
                y = x / 2
                self._stats_halved[i] = y
            return self._stats_halved


        def setStats(self):
            self.attack = self.stats["attack"]
            self.mobility = self.stats["mobility"]
            self.skill = self.stats["skill"]
            self.defense = self.stats["defense"]
            self.command = self.stats["command"]
            self.ranger = self.stats["ranger"]
            self.trion = self.stats["trion"]
            self.stats_halved()
            #self.stats_halved() = self._stats_halved
        
        #def __repr__(self):
        #   return self.stats

        def statsArray(self, half = False):
            if half == True:
                self.given_stats = self.stats_halved()
                print(f'halved stats are {self.stats_halved()}')
            else:
                self.given_stats = self.stats
                self.given_stats = self.given_stats.copy()
            self.stats_array = []
            for i in self.given_stats:
                stat_v = self.given_stats[i]
                self.stats_array.append(stat_v)
            return self.stats_array
            

            #{ "stats": {"attack": 4.0, "mobility": 4.00, "defense": 4.00, "command": 4.00, "skill": 4.00, "ranger":4.00, "trion":OGtrion},"money":[2000],"main_points":[4000], "stats_halved": 0 }
    
            

        """@property
        def stats_halved(self):
            return self._stats_halved

        @stats_halved.setter
        def stats_halved(self, OGstats):
            self.OGstats = OGstats
            self.OGstats = self.OGstats.copy()
            self._stats_halved = self.OGstats
            for i in self._stats_halved: 
                x = self.OGstats[i]
                y = x / 2
                self._stats_halved[i] = y
            #return self._stats_halved"""