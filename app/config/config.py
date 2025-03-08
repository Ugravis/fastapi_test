from dotenv import load_dotenv
import os

load_dotenv()

class Config: 
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development") # development par défaut, au cas où le projet est lancé avec la commande standard de FastAPI

    PROD_DB_USER: str = os.getenv("PROD_DB_USER")
    PROD_DB_PASSWORD: str = os.getenv("PROD_DB_PASSWORD")
    PROD_DB_HOST: str = os.getenv("PROD_DB_HOST")
    PROD_DB_NAME: str = os.getenv("PROD_DB_NAME")

    DEV_DB_USER: str = os.getenv("DEV_DB_USER")
    DEV_DB_PASSWORD: str = os.getenv("DEV_DB_PASSWORD")
    DEV_DB_HOST: str = os.getenv("DEV_DB_HOST")
    DEV_DB_NAME: str = os.getenv("DEV_DB_NAME")

    if ENVIRONMENT == "production": 
        DATABASE_URL: str = f"mysql+pymysql://{PROD_DB_USER}:{PROD_DB_PASSWORD}@{PROD_DB_HOST}/{PROD_DB_NAME}?charset=utf8mb4"
    else:
        DATABASE_URL: str = f"mysql+pymysql://{DEV_DB_USER}:{DEV_DB_PASSWORD}@{DEV_DB_HOST}/{DEV_DB_NAME}?charset=utf8mb4"

config = Config()