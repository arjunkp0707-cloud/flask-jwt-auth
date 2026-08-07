from datetime import timedelta


class Config:
    JWT_SECRET_KEY = "super-secret-key"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=2)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
