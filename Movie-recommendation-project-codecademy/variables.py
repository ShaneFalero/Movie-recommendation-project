#This file is utilized for creating data structure, assigning objects and creating variables to be searched through for the primary program.

class Movie():
    def __init__(self, title, ratings, released, cost = 0, subgenre = [] ):
        self.title = title
        self.ratings = ratings
        self.released = released
        self.cost = cost
        self.subgenre = subgenre

    def __repr__(self):
        return f'''
        Movie title: {self.title}
        Release Date: {self.released}
        Ratings: {self.ratings}
        Genre: {", ".join(self.subgenre)}
        Cost: {self.cost}

        ---------------------
        '''
        

#Hashmap that accounts for collisions using open addressing
#Note for later:  key will be movie.title; value will be class of movie

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for items in range(self.array_size)]
    
    #Hashing function
    def hash(self, key, count_collision = 0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collision  #returns index into the underlying array

    #Compression function
    def compressor(self, hash_code):
        return hash_code % self.array_size #calculates array index for a hash map when given a hash code

    #Setter function
    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value == None:
            self.array[array_index] = [key, value]
            return
        
        elif current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return
        
        #Handling collisions at self.array[array_index]:
        num_collisions = 1

        while current_array_value[0] != key:
            new_hash_code = self.hash(key, num_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value == None:
                self.array[new_array_index] = [key,value]
                return
            
            elif current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            num_collisions +=1
        return

    #getter function
    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]
        
        if possible_return_value is None:
            return None

        elif possible_return_value[0] is key:
            return possible_return_value[1]

        #Handling collisions:
        retrieval_collisions = 1

        while possible_return_value != key:
            retrieving_array_index = self.compressor(self.hash(key, retrieval_collisions))
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value == None:
                return None
            
            elif possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions +=1

        return

#Creating variables:
#Action Movies
The_Kings_Man = Movie("The King's Man", '6.3/10', 2021, 19.99, ['Action', 'Adventure'])
LOTR_RotK = Movie('Lord of the Rings: Return Of The King', '9.0/10', 2003, 9.99, ['Action', 'Fantasy', 'Adventure'])
Avengers_Endgame = Movie('Avengers Endgame', '8.4/10', 2019, 19.99, ['Action', 'Science Fiction'] )
Rogue_One_SW = Movie('Rogue One: A Star Wars Story', '7.8/10', 2016, 19.99,  ['Action', 'Science Fiction'])
The_Bourne_Identity = Movie('The Bourne Identity', '7.9/10', 2002, 14.99, ['Action', 'Thriller'])


#Horror Movies
Scream = Movie('Scream', '6.3/10', 2022, 31.99, ['Horror', 'Thriller'])
The_Shining = Movie('The Shining', '8.4/10', 1980, 14.99, ['Horror', 'Mystery'])
The_Conjuring = Movie('The Conjuring', '7.5/10', 2013, 14.99, ['Horror', 'Thriller'] )
Orphan_First_Kill = Movie('Orphan: First Kill', '6/10', 2022, 24.99, ['Horror', 'Thriller'])
Us = Movie('Us', '6.8/10', 2019, 14.99, ['Horror', 'Thriller'])

#Science fiction
Morbius = Movie('Morbius', '5.2/10', 2022, 19.99, ['Action', 'Fantasy', 'Science Fiction'] )
Avatar = Movie('Avatar', '7.8/10', 2009, 9.99, ['Action, Science Fiction'])
Interstellar = Movie('Intersteller', '8.6/10', 2014, 9.99, ['Science Fiction', 'Adventure'])
Ready_Player_One = Movie('Ready Player One', '7.4/10', 2018, 9.99, ['Science Fiction', 'Action'] )
Inception = Movie('Inception', '8.8/10', 2010, 9.99, ['Action', 'Science Fiction'])

#Comedy
The_Waterboy = Movie('The Waterboy', '6.1/10', 1998, 7.99, ['Comedy'])
Dumb_and_dumber = Movie('Dumb And Dumber', '7.3/10', 1992, 9.99, ['Comedy'])
Shanghai_Knights = Movie('Shanghai Knights', '6.2/10', 2003, 9.99, ['Action', 'Comedy'])
Free_Guy = Movie('Free Guy', '7.1/10', 2021, 19.99, ['Action', 'Comedy', 'Science Fiction'] )
Step_Brothers = Movie('Step Brothers', '6.9/10', 2008, 7.99, ['Comedy'])

#Drama
Gladiator = Movie('Gladiator', '8.5/10', 2000, 12.99, ['Action', 'Adventure', 'Drama'])
Titanic = Movie('Titanic', '7.9/10', 1997, 12.99, ['Romance', 'Drama'])
Forrest_Gump = Movie('Forrest Gump', '8.8/10', 1994, 14.99, ['Drama', 'Romance'])
Django = Movie('Django', '8.4/10', 2012, 12.49, ['Western', 'Drama'])
The_Queen = Movie('The Queen', '7.3/10' , 2006, 12.99, ['Drama', 'Historical Drama'])

movie_list = [The_Kings_Man, LOTR_RotK, Avengers_Endgame, Rogue_One_SW, The_Bourne_Identity, Scream, The_Shining, The_Conjuring, Orphan_First_Kill, Us, Morbius, Avatar, Interstellar,
Ready_Player_One, Inception, The_Waterboy, Dumb_and_dumber, Shanghai_Knights, Free_Guy, Step_Brothers, Gladiator, Titanic, Forrest_Gump, Django, The_Queen]
genre_list = ['Comedy', 'Action', 'Adventure', 'Drama', 'Western', 'Science Fiction', 'Horror', 'Thriller', 'Fantasy', 'Mystery', 'Romance']

movie_hash_map = HashMap(25)
for movie in movie_list:
    movie_hash_map.assign(movie.title, movie)

#print((movie_hash_map.retrieve('Avengers Endgame')).ratings)
#print(vars(movie_hash_map))

