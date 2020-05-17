import os

DB_NAME = 'capstone'
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_PORT = os.getenv('DB_PORT', 5432)
DB_HOST = os.getenv('DB_HOST', 'database-1.cruf3coihsjk.us-east-2.rds.amazonaws.com')

db_uri = f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
