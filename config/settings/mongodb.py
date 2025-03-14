import pymongo

from config.env import env

MONGO_HOST = env("MONGO_HOST", default="127.0.0.1")
MONGO_PORT = env.int("MONGO_PORT", default=27017)
MONGO_DATABASE = env("MONGO_DATABASE", default="hoopoe_mongo")
MONGO_USERNAME = env("MONGO_USERNAME", default="hoopoe_mongo")
MONGO_PASSWORD = env("MONGO_PASSWORD", default="hoopoe_mongo")


mongo_client = pymongo.MongoClient(
    host=MONGO_HOST, port=MONGO_PORT, username=MONGO_USERNAME, password=MONGO_PASSWORD
)

mongo_db = mongo_client[MONGO_DATABASE]
