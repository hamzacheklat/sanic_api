import os

class Config:
    def __init__(self):
        pass

    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/app")


class DevelopmentConfig(Config):
    def __init__(self):
        super().__init__()

    DEBUG = True

class ProductionConfig(Config):
    def __init__(self):
        super().__init__()

    DEBUG = False

config = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig
}

current_config = config[os.getenv("ENV", "dev")]
