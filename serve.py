import bjoern 
from app import app

host = '0.0.0.0'
port = 5005

print("bjoern is up and running")

bjoern.run(app, host, port)