# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 21:51:13 2018

@author: HP
"""
#use of the file
import media
import opener
#here init()is called constructor
toy_story=media.Movie("Toy Story",
                      "A story of a boy and his toys",
                      "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=SgoiKLFBA3Q") #instances of class
avatar=media.Movie("Avatar",
                   "A marine on a alian planet",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_QL50_.jpg",
                   "https://www.youtube.com/watch?v=d1_JBMrrYw8") 
#print(toy_story.storyline)
#print(avatar.storyline)
#toy_story.show_trailor()
#from pil import pillow
movies=[toy_story, avatar]
opener.open_movies_page(movies)
