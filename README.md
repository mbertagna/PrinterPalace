# PrinterPalace
### By Michael Bertagna and Helena Gray

HOW TO USE PrinterPalace:

1. Create a new MySQL database named "PrinterPalace"

2. Open the "PrinterPalace.sql" file and run the entire file to generate the database with dummy data

3. Open the Home.py, Create_Record.py, Update_Record.py, Delete_Record.py, and Search_Database.py files from the source code

4. Update the 
"
db = mysql.connector.connect(
    host = "",
    user = "",
    password = "",
    database = "PrinterPalace"
)
"
section in each file with your host, user, and password

5. Open a console and navigate to the "PrinterPalace" directory

6. Run the command "streamlit run Home.py"

7. The application will open in your default brower and is ready for use!

Dependencies:
streamlit
pandas
mysql.connector
itertools

References:
- Class notes
- https://docs.streamlit.io/library/api-reference
- https://docs.singlestore.com/managed-service/en/reference/troubleshooting-reference/query-errors/error-1205--hy000---lock-wait-timeout-exceeded;-try-restarting-transaction.html
- https://www.tutorialspoint.com/How-to-remove-an-element-from-a-list-by-index-in-Python
- https://stackoverflow.com/questions/10506904/typeerror-can-only-concatenate-tuple-not-list-to-tuple
- https://databasefaqs.com/how-to-call-a-view-in-sql-server/

