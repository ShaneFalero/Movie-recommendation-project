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
        return

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
    def retrieve(self,key):
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
