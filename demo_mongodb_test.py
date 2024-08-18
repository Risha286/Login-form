import pymongo

# Replace the following with your MongoDB connection string
connection_string = "mongodb://localhost:27017/"

# Connect to MongoDB
client = pymongo.MongoClient(connection_string)

# Test the connection by listing databases
try:
    databases = client.list_database_names()
    print("Connected to MongoDB. Databases available:")
    for db in databases:
        print("-", db)
except Exception as e:
    print("An error occurred:", e)
