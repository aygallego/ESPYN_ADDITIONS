# -*- coding: utf-8 -*-
"""
Created on Wed May  7 09:37:22 2014

@author: AndreaGallego
working with ESPYN to add functionalities
This is a class for fantasy football news 
"""

import urllib
#import pandas 


class Sport():
    API_KEY=''
    ESPN_URL='http://api.espn.com/v1'
    BASE_URL=ESPN_URL +'/fantasy'
    FOOTBALL='football'
    
    
    SUPPORTED_SPORTS=frozenset([FOOTBALL])
    
    def __init__(self,sport=None):
        if sport not in Sport.SUPPORTED_SPORTS:
            raise KeyError ("%s is not a valid supported sport" %sport)
        self.BASE_URL=Sport.BASE_URL + '/' + sport 
        
    def get_Fantasy_news(self):
    
        fetch_url = self.BASE_URL+ '/news'+ '?apikey='+ Sport.API_KEY
        print fetch_url
        return urllib.urlopen(fetch_url)
        
        
class League(Sport):
    LEAGUE_TO_SPORT={
            'nfl': Sport.FOOTBALL}
    def __init__(self, league=None):
        if league not in League.LEAGUE_TO_SPORT.keys():
            raise KeyError ("%s is not a valid supported league" % league)
            self.base_url=Sport(sport=League.LEAGUE_TO_SPORT[league])
            print self.base_url
                    
if __name__=="__main__":
    football=League('nfl')
    print football.get_Fantasy_news().readlines() 
    
    
    #next implemnentation is to create class for pandas and load data into dataframe 
            
            
        
        
        
        
        