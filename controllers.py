import sqlite3
from models import validate_name, validate_bus_number, validate_date
from src.logger import setup_logger

logger = setup_logger()

def create_booking(name, bus_number, date):
    try:
        if not all([validate_name(name), validate_bus_number(bus_number), validate_date(date)]):
            error_msg = f"Validation failed - Name: {name}, Bus: {bus_number}, Date: {date}"
            logger.error(error_msg)
            raise ValueError("Invalid input format")
            
        conn = sqlite3.connect('bus_booking.db')
        c = conn.cursor()
        c.execute("INSERT INTO bookings (name, bus_number, date) VALUES (?, ?, ?)", 
                 (name, bus_number, date))
        conn.commit()
        conn.close()
        
        logger.info(f"Booking created successfully - Name: {name}, Bus: {bus_number}, Date: {date}")
        
    except Exception as e:
        logger.error(f"Error creating booking: {str(e)}")
        raise

def get_bookings():
    try:
        conn = sqlite3.connect('bus_booking.db')
        c = conn.cursor()
        c.execute("SELECT * FROM bookings")
        bookings = c.fetchall()
        conn.close()
        
        logger.info(f"Retrieved {len(bookings)} bookings")
        return bookings
        
    except Exception as e:
        logger.error(f"Error retrieving bookings: {str(e)}")
        raise
