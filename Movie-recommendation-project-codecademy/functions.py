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

def logic(user_input, hash_map):
    if user_input.title() in variables.genre_list:
        print(f'You have selected: {user_input}.  Here are the list of movies to choose from:')
        for movie in variables.movie_list:
            if user_input.title() in movie.subgenre:
                print(hash_map.retrieve(movie.title))
        inquire_movie()
        if user_input2.title() is (hash_map.retrieve(user_input2.title())).title:
            print(f'You have chosen: {(hash_map.retrieve(user_input2)).title}')
        else:
            print('That was not one of the options, Try again.')
    else:
        print('I am sorry, the inputted genre was not in our list of genres.  Please try again.')
        return logic(inquire_genre(), hash_map)


logic(inquire_genre(), variables.movie_hash_map)