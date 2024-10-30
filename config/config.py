import os

class Config:
    DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://user:password@localhost/health_ner')
    MODEL_PATH = os.getenv('MODEL_PATH', './models/personalized_ner.pt')
    FEEDBACK_BATCH_INTERVAL = 7  # in days for continuous learning
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', 'your_encryption_key')
