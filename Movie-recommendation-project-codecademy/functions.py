import variables
def greeting():
    print('''
    Welcome to Eucalyptus polyanthemos!
    We are a movie recommendation service!

                /|\\
               / | \\
              /  |  \\
             /\/\|/\/\\
            /    |    \\
           /_____|_____\\
                |_|
    ''')
    
def inquire_genre():
    user_input = input('What genre of Movie are you looking for today? ')
    return user_input

def inquire_movie():
    user_input = input('Which of these movies interest you? ')
    return user_input

def logic_genre(user_input, hash_map):
    list_of_movies_in_genre = []
    if user_input.title() in variables.genre_list:
        print(f'You have selected: {user_input}.  Here are the list of movies to choose from:')
        for movie in variables.movie_list:                     
            if user_input.title() in hash_map.retrieve(movie.title).subgenre:
                list_of_movies_in_genre.append(hash_map.retrieve(movie.title))
                print(hash_map.retrieve(movie.title))       
    else:
        print('I am sorry, the inputted genre was not in our list of genres.  Please try again.')
        return logic_genre(inquire_genre(), hash_map)
    return list_of_movies_in_genre

def logic_movie(movie_list, user_input):
    for movie in movie_list:
        if user_input.title() == movie.title.title():
            print(f'You have chosen: {movie}A good choice!')
            print(f'You are now watching: {movie.title}')
            farewell()
            return
        elif pattern_search(movie.title.title(), user_input.title()) == True:
            new_input = input(f'did you mean {movie.title.title()}: ')
            if new_input == 'yes':
                print(f'You have chosen: {movie}A good choice!')
                print(f'You are now watching: {movie.title}')
                farewell()
                return
            else:
                print('Sorry we could not find the film you requested.  Please try again')
                return
    print('Sorry we could not find the film you requested.  Please try again')        
    return

def pattern_search(text, pattern):
    for index in range(len(text)):
        match_count = 0
        
        for char in range(len(pattern)):
            try:
                if pattern[char] == text[index + char]:                    
                    match_count += 1
                else:
                    continue
            except:
                IndexError
        if match_count >= len(text) // 2:
            
            return True
        else: 
            return False

def farewell():
    print('Thank you for watching with Eucalyptus polyanthemos!')
    print('Enjoy your movie!')
   

#logic_movie(logic_genre(inquire_genre(), variables.movie_hash_map), inquire_movie())





