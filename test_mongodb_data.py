
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://vg498660:-Nbv34WzwMGz9q9@cluster0.d0xvt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)