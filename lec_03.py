# How it appears, how it functions


from dataclasses import dataclass

@dataclass
class MediaItem:
    id : int
    title : str
    genre : str
    platform : str
    status : str = "Plan to Watch"
    rating : float = None
    progress : int = 0

    def markCompleted(self):
        self.status = "Completed"

@dataclass
class Movie(MediaItem):
    duration : int = 0

    def calculateWatchTime(self):
        if self.status == "Completed":
            return self.duration
        return 0

@dataclass
class Series(MediaItem):
    total_episodes : int
    episodes_runtime : int = 45

    def calculateWatchTime(self):
            if self.status == "Completed":
                return self.duration        
            return 0




m1 = Movie(1, 'Dhurandhar', 'Action', 'Netflix')
m2 = Movie(7, 'Sholay', 'Drama', 'Prime')

m1.duration = 150
m1.markCompleted()
print(m1.calculateWatchTime())

m2.rating = 4
print(m2.calculateWatchTime())



#HOMEWORK : TO CALCULATE TOTAL Duration of Series' Episodes
# Homework : Create method to find the Progress Percentage based on episodes watched