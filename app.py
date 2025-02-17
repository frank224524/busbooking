from flask import Flask, render_template, request, redirect, url_for
from models import init_db
from controllers import create_booking, get_bookings
from src.logger import setup_logger
#frankhi
logger = setup_logger()
app = Flask(__name__)
@dhffcgfjh
@app.before_first_request
def initialize():
    try:
        init_db()
        logger.info("Application initialized successfully")
    except Exception as e:
        logger.error(f"Application initialization failed: {str(e)}")
        raise

@app.route('/')
def index():
    logger.info("Accessed index route")
    return render_template('index.html')

@app.route('/login')
def login():
    logger.info("Accessed login route")
    return render_template('login.html')

@app.route('/register')
def register():
    logger.info("Accessed register route")
    return render_template('register.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        try:
            name = request.form['name']
            bus_number = request.form['bus_number']
            date = request.form['date']
            create_booking(name, bus_number, date)
            logger.info(f"Booking created from form - Name: {name}, Bus: {bus_number}, Date: {date}")
            return redirect(url_for('index'))
        except Exception as e:
            logger.error(f"Error processing booking form: {str(e)}")
            return render_template('book.html', error=str(e))
    
    logger.info("Accessed book route (GET)")
    return render_template('book.html')

@app.route('/bookings')
def bookings():
    try:
        bookings = get_bookings()
        logger.info(f"Displaying {len(bookings)} bookings")
        return render_template('bookings.html', bookings=bookings)
    except Exception as e:
        logger.error(f"Error retrieving bookings: {str(e)}")
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    logger.info("Starting application")
    app.run(debug=True)
