"""Check that the Pokemon dataset in MongoDB Atlas has
the correct amount of rows in it, and that the rows
look fine. It was imported using
mongoimport --host Cluster0-shard-0/cluster0-shard-00-00-q42xu.mongodb.net:27017,cluster0-shard-00-01-q42xu.mongodb.net:27017,
cluster0-shard-00-02-q42xu.mongodb.net:27017 --ssl --username <USERNAME> --password <PASSWORD>
--authenticationDatabase admin --db pokemon --collection all_data --type csv --file Pokemon_cleaned.csv --headerline
"""

#!/usr/bin/env python
import os
import pymongo

if __name__ == "__main__":
    mongo_atlas_username = os.environ['MONGO_ATLAS_USERNAME']
    mongo_atlas_password = os.environ['MONGO_ATLAS_PASSWORD']

    connection_string = "mongodb://<USERNAME>:<PASSWORD>@cluster0-shard-00-00-q42xu.mongodb.net:27017,cluster0-shard-00-01-q42xu.mongodb.net:27017,cluster0-shard-00-02-q42xu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"
    connection_string = connection_string.replace("<USERNAME>",
                                                  mongo_atlas_username)
    connection_string = connection_string.replace("<PASSWORD>",
                                                  mongo_atlas_password)
    print(connection_string)

    client = pymongo.MongoClient(connection_string)

    db = client.pokemon
    coll = db.all_data

    i = 0
    for p in coll.find():
        i += 1
        print(p)
    print("Total number of rows:", i)
