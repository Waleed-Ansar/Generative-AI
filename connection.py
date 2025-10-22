import ssl
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://Waleed-Ansar:fastAPI%40waleed570@fastapi-cluster.0yfuiu4.mongodb.net/"

ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = True
ssl_ctx.verify_mode = ssl.CERT_REQUIRED

client = AsyncIOMotorClient(
    MONGO_URI,
    tls=True,
    tlsAllowInvalidCertificates=False,
    tlsCAFile=None
)

db = client["Book_Shelf"]
collection_name = db["Books"]
api_keys = db["api_key"]
