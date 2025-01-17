import os
from urllib.parse import quote_plus

# Database credentials matching your PostgreSQL setup
DB_USER = "postgres"  # Default PostgreSQL user
DB_PASSWORD = quote_plus("Passwd@123")  # Your PostgreSQL password
DB_HOST = "localhost"  # Since PostgreSQL is running locally
DB_NAME = "activity_logs"  # The database you created

# Construct database URI with the correct credentials
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# For debugging
print(f"Connecting to database: postgresql://{DB_USER}:****@{DB_HOST}/{DB_NAME}")
