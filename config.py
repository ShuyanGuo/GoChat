import os

class Config:
    SECRET_KEY = 'hard to guess'
    MONGODB_SETTINGS = {
        "db": "userdb",
        "host": "127.0.0.1",
        "port": 27017
    }
    MAIL_SERVER = "gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    WEBCHAT_MAIL_SUBJECT_PREFIX = "[GoChat]"
    WEBCHAT_MAIL_SENDER = "GoChat Admin <guoshuyan88123@gmail.com>"
    CELERY_BROKER_URL = "amqp://guest@localhost//"
    ROOM_INFO_KEY = "room_info_key_{room}"
    ROOM_ONLINE_USER_CHANNEL = "room_online_user_channel_{room}"
    ROOM_CONTENT_CHANNEL = "room_content_channel_{room}"
    ROOM_INCR_KEY = "room_incr_key"
    ROOM_CONTENT_INCR_KEY = "room_content_incr_key"