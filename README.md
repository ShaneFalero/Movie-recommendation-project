# Movie-recommendation-project
movie recommendation project for codecademy

This project was assigned to me through Codecademy
The goal of this project is to learn how to store data into a data structure that was taught throughout the course

Learned data structures:
    Doubly-linked lists
    Graphs
    Hash-maps
    Heaps
    Queues
    Singly linked lists
    Stacks
    Trees

Use an algorithm taught throughout the course to sort or search data within a data structure to create a recommendation software that would sort through a primary category then output 
    a subcategory


Algorithms learned:
    Brute force algorithms
    Divide and Conquer
    Greedy algorithms
    Dynamic programming
    Pathfinding
    Pattern Search
    Sorting
    Tree traversal algorithms


My thoughts for this project were initially to create a tree to iterate through genres of movies, inquire what genre would like to be watched, then iterate thorugh a list of movies within the genre and output the appropriate movies - unfortunately the file got corrupted so I decided to change my approach.

My new approach is going to be to again, class movies with subgenres, cost, ratings, and a title.
Then I am going to create a hash map
For the main program, I am going to have the bot inquire what genre of movies interest the user, iterate through the subgenre class attribute and then output every move with the subgenre equal to the user input.
The user will then have the opportunity to decide whether any of the outputted movies are of interest and 'execute' it