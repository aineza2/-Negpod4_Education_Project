import mysql.connector
# database details
host = "102.22.172.49"
port = 3306
user = "Remote"
password = ""
database = "Trail"
# Forming a connection
connection = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)
# Cursor connection
cursor = connection.cursor()

choice = input("""
Welcome to our language training app.
Enter 1 for registration, or 2 for loging in
""")
# User registration
if choice == '1':
        email = input("Enter your email: ")
        password =  input("Enter a password: ")

        # Check if the email already exists
        cursor.execute("SELECT * FROM Information WHERE Email = %s", (email,))
        if cursor.fetchone():
                print("User with this email already exists. Please choose login instead.")
        else:
                # Insert the new user into the database
                cursor.execute("INSERT INTO Information (Email, Password) VALUES (%s, %s)", (email, password))
                connection.commit()
                print("Registration successful. You can now log in.")

# User login
elif choice == '2':
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        # Check if the email and password match
        cursor.execute("SELECT * FROM Information WHERE Email = %s AND Password = %s", (email, password))
        if cursor.fetchone():
                print("Login successful.")
        else:
                print("Invalid email or password. Please try again.")
else:
        print("Invalid choice")
cursor.close()
connection.close()