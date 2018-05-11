import pymongo
import pandas as pd
from pymongo import MongoClient
import numpy as np
from random import randint

client = MongoClient()

# Get the sampleDB database
db = client.sampleDB

fivestar = db.reviews.find({'rating': { '$lt': 6 } } )
print(fivestar)

print(fivestar[0])
print(fivestar[1])
print(fivestar[2])

fivestar0 = pd.DataFrame([fivestar[0]], columns=fivestar[0].keys())
fivestar1 = pd.DataFrame([fivestar[1]], columns=fivestar[1].keys())
fivestar2 = pd.DataFrame([fivestar[2]], columns=fivestar[2].keys())

fivestar0 = pd.concat([fivestar0, fivestar1], axis=0)
fivestar0 = pd.concat([fivestar0, fivestar2], axis=0)

print(fivestar0)

fivestar0 = np.asarray(fivestar0)

print(fivestar0.shape)
print(fivestar0)