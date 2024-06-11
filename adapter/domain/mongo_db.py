from pymongo import MongoClient
from config import (MONGO_HOST)

class MongoDB:
    def __init__(self):
        self.mongo_url = MONGO_HOST
        self.client = MongoClient(self.mongo_url)
        self.database = self.client["images"]
        self.collection = self.database["items"]
        
    def save_json(self,params):
        
        result = self.collection.find_one_and_update({"url": params.url},
                               {"$set": params.dict()},
                               upsert=True)
        return result
    
    def load_json(self,param):
        result = self.collection.find({'url': {'$regex': param}})
        
        return result
    
    def save_geojson(self,params):
        result = self.collection.find_one_and_update({"prefix": params["prefix"]},
                               {"$set": params},
                               upsert=True)
        return result
    
    def load_geojson(self,param):
        result = self.collection.find({'prefix': {'$regex': param}})
        
        return result
    


        
    