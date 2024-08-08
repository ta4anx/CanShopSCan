#CanShopsCan - Shopping List Subsystem with USB Barcode Reader and Raspberry Pi using Python and SQL
#   _____             _____ _                 _____  _____            
#  / ____|           / ____| |               / ____|/ ____|           
# | |     __ _ _ __ | (___ | |__   ___  _ __| (___ | |     __ _ _ __  
# | |    / _` | '_ \ \___ \| '_ \ / _ \| '_ \\___ \| |    / _` | '_ \ 
# | |___| (_| | | | |____) | | | | (_) | |_) |___) | |___| (_| | | | |
#  \_____\__,_|_| |_|_____/|_| |_|\___/| .__/_____/ \_____\__,_|_| |_|
#                                      | |                            
#                                      |_|                            
#A shopping list subsystem with usb Barcode Reader and raspberry pi with python and sql
import sqlite3
import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

# Initialize LCD
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# Connect to the databasee
conn = sqlite3.connect('shopping_list.db')
cursor = conn.cursor()


# Create the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        quantity INTEGER
    )
''')


# Read barcode input from the USB Barcode Reader
def read_barcode():
    # Add your code here to read the barcode input from the USB Barcode Reader
    barcode = input("Enter barcode: ")
    return barcode


# Add item to the shopping list
def add_item(barcode):
    # Add your code here to retrieve item details from the barcode
    name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))

    # Insert the item into the database
    cursor.execute('''
        INSERT INTO items (name, quantity)
        VALUES (?, ?)
    ''', (name, quantity))
    conn.commit()

    # Display item added message on LCD
    lcd.clear()
    lcd.message('Item added to\nshopping list')

# Main loop
while True:
    # Display barcode read message on LCD
    lcd.clear()
    lcd.message('Barcode read')
    barcode = read_barcode()
    add_item(barcode)

    
