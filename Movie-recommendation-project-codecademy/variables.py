#This file is utilized for creating data structure, assigning objects and creating variables to be searched through for the primary program.

class Movie():
    def __init__(self, title, famous_actors, ratings, cost = 0, subgenre = [] ):
        self.title = title
        self.actors = famous_actors
        self.ratings = ratings
        self.cost = cost
        self.subgenre = subgenre

    def __repr__(self):
        print(f'''
        Movie title: {self.title},
        Genre: {self.subgenre},
        Ratings: {self.ratings},
        Cost: {self.cost} 
        ''')


