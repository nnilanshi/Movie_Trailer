# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 21:41:17 2018

@author: HP
"""
import webbrowser
#class defination
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): # init initialise the space for name storyine etc
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube
        #self is not keyword
        #through instance constructor is called
        #here constructor uses keyword self but this can also be named as anything        
    #instance method
    def show_trailor(self):
        webbrowser.open(self.trailer_youtube_url)