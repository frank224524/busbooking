import sqlite3
import re
from src.logger import setup_logger

logger = setup_logger()

def validate_name(name):
    """Validate name format (Arabic/English letters and spaces)"""
    result = re.match(r'^[a-zA-Z\u0600-\u06FF\s]+$', name) is not None
    logger.info(f"Name validation result: {result} for input: {name}")
    return result

def validate_bus_number(bus_number):
    """Validate bus number format (2 letters + 3 numbers)"""
    result = re.match(r'^[A-Z]{2}\d{3}$', bus_number) is not None
    logger.info(f"Bus number validation result: {result} for input: {bus_number}")
    return result

def validate_date(date):
    """Validate date format (YYYY-MM-DD)"""
    result = re.match(r'^\d{4}-\d{2}-\d{2}$', date) is not None
    logger.info(f"Date validation result: {result} for input: {date}")
    return result

def init_db():
    try:
        conn = sqlite3.connect('bus_booking.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS bookings
                     (id INTEGER PRIMARY KEY, name TEXT, bus_number TEXT, date TEXT)''')
        conn.commit()
        conn.close()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {str(e)}")
        raise
