from dataclasses import dataclass
from enum import Enum
from abc import ABC, abstractmethod

class WatchStatus(Enum):
    PLAN_TO_WATCH = "Plan to Watch"
    COMPLETED = "Completed"
    DROPPED = "Dropped"
    WATCHING = "Watching"
    ON_HOLD = "On Hold"

# ______________________MEDIAItem______________________________________

@dataclass
class MediaItem(ABC):     #Abstract Base Class  
    id : int
    title : str
    genre : str
    platform : str
    status : WatchStatus = WatchStatus.PLAN_TO_WATCH
    rating : float = None

    def markCompleted(self):
        self.status = WatchStatus.COMPLETED

    @abstractmethod
    def calculateWatchTime(self):
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        return {
            "type":self.__class__.__name__,
            "id" : self.id,
            "title" : self.title,
            "genre" : self.genre,
            "platform" : self.platform,
            "status" : self.status.value,
            "rating" : self.rating
        }

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> "MediaItem":
        '''Deserialisation of Dictionary into MediaItem object'''
        pass



# ______________________MOVIE______________________________________

@dataclass
class Movie(MediaItem):
    runtime_minutes : int = 0

    def calculateWatchTime(self):
        if self.status == WatchStatus.COMPLETED:
            return self.runtime_minutes
        return 0

    def to_dict(self):
        data = super().to_dict()
        data["runtime_minutes"] = self.runtime_minutes
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Movie":
        return cls(
            id = data["id"],
            title = data["title"],
            genre = data["genre"],
            platform = data["platform"],
            status = WatchStatus(data["status"]),
            rating = data.get("rating"),
            runtime_minutes = data.get("runtime_minutes")
        )


# _______________________SERIES_____________________________________

@dataclass
class Series(MediaItem):
    total_episodes : int = 12
    episodes_watched : int = 0
    episodes_runtime : int = 45

    def calculateWatchTime(self):
        return self.episodes_watched * self.episodes_runtime if self.episodes_watched > 0 else 0

    @property
    def progress_percentage(self) -> float:
        return round((self.episodes_watched/self.total_episodes)*100, 1) if self.episodes_watched > 0 else 0.0

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "total_episodes" : self.total_episodes,
            "episodes_watched" : self.episodes_watched,
            "episodes_runtime" : self.episodes_runtime   
        })
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Series":
        return cls(
            id = data["id"],
            title = data["title"],
            genre = data["genre"],
            platform = data["platform"],
            status = WatchStatus(data["status"]),
            rating = data.get("rating"),
            total_episodes = data.get("total_episodes"),
            episodes_watched = data.get("episodes_watched"),
            episodes_runtime = data.get("episodes_runtime")
        )



s1 = Series(2,"Panchayat", "Comedy","Prime", episodes_watched=3)
s2 = Series(5,"Rookie", "Drama, Action","Netflix", episodes_watched=5, total_episodes=125)

m1 = Movie(1, 'Dhurandhar', 'Action', 'Netflix', runtime_minutes=120, status=WatchStatus.WATCHING)

# print(f"Series 2 : {s2}\n\n")
# print(f"Series 1 : {s1.to_dict()}")


seriesDict = {'type': 'Series', 'id': 2, 'title': 'Panchayat', 'genre': 'Comedy', 'platform': 'Prime', 'status': 'Plan to Watch', 'rating': None, 'total_episodes': 12, 'episodes_watched': 3, 'episodes_runtime': 45}

print(Movie.from_dict(seriesDict))