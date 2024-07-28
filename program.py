from tkinter import *
import mysql.connector

# Function to get values from the form and insert them into the MySQL database
def getvals():
    name = nameval.get()
    phone = phoneval.get()
    gmail = gmailval.get()
    gender = genderval.get()
    paymentmood = paymentmoodval.get()
    remember_me = checkvalue.get()
    
    # Print values to the console (for debugging purposes)
    print(f"Name: {name}, Phone: {phone}, Gmail: {gmail}, Gender: {gender}, Payment Mood: {paymentmood}, Remember Me: {remember_me}")
    
    # Database connection
    try:
        conn = mysql.connector.connect(
            host="localhost",       # Replace with your host name
            user="root",   # Replace with your MySQL username
            password="pass@pratiksha02", # Replace with your MySQL password
            database="form"  # Replace with your database name
        )
        cursor = conn.cursor()

        # Insert data into the database
        query = "INSERT INTO register(name, phone, gmail, gender, paymentmood, remember_me) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, phone, gmail, gender, paymentmood, remember_me)
        cursor.execute(query, values)
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        print("Data inserted successfully")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
# Create the main window
root = Tk()
root.geometry("500x300")

# Heading
Label(root, text="Python Registration Form", font="arial 20 bold").grid(row=0, column=3)

# Field names
Label(root, text="Name").grid(row=1, column=2)
Label(root, text="Phone").grid(row=2, column=2)
Label(root, text="Gmail").grid(row=3, column=2)
Label(root, text="Gender").grid(row=4, column=2)
Label(root, text="Payment Mood").grid(row=5, column=2)

# Variables for storing data
nameval = StringVar()
phoneval = StringVar()
gmailval = StringVar()
genderval = StringVar()
paymentmoodval = StringVar()
checkvalue = IntVar()

# Creating entry fields
Entry(root, textvariable=nameval).grid(row=1, column=3)
Entry(root, textvariable=phoneval).grid(row=2, column=3)
Entry(root, textvariable=gmailval).grid(row=3, column=3)
Entry(root, textvariable=genderval).grid(row=4, column=3)
Entry(root, textvariable=paymentmoodval).grid(row=5, column=3)

# Creating checkbox
Checkbutton(root, text="Remember me?", variable=checkvalue).grid(row=6, column=3)

# Submit button
Button(root, text="Submit", command=getvals).grid(row=7, column=3)

# Start the main event loop
root.mainloop()
