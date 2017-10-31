# SERVER
DOMAIN = "localhost"
SERVER = "http://" + DOMAIN
SENDER = "no-reply@" + DOMAIN
SECURITY_EMAIL_SENDER = SENDER
# REPEC
REPEC_API_CODE = "xxxxxxxx"

# Since we use docker's links, don't touch the following lines
# if you don't know what you are doing
MONGODB_HOST = 'mongo'
MONGODB_PORT = 27017
