from fastapi import FastAPI, Header
import os

app = FastAPI()

# MySQL configuration
USERINFO_DB_CONFIG = {
    "host": os.getenv("USERINFO_DB_HOST", "localhost"),  # oder die IP-Adresse
    "user": os.getenv("USERINFO_DB_USER", "root"),
    "password": os.getenv("USERINFO_DB_PASSWORD", ""),
    "database": os.getenv("USERINFO_DB_NAME", "test"),
}

BILLING_DB_CONFIG = {
    "host": os.getenv("BILLING_DB_HOST", "localhost"),
    "user": os.getenv("BILLING_DB_USER", "root"),
    "password": os.getenv("BILLING_DB_PASSWORD", ""),
    "database": os.getenv("BILLING_DB_NAME", "test"),
}

# Check for module availability
mysql_available = True
try:
    import mysql.connector
    from mysql.connector import Error
except ModuleNotFoundError:
    mysql_available = False
    print("Module 'mysql.connector' is not installed. Please install it to enable database connectivity.")


@app.get("/")
def read_headers(
    username_header: str = Header(None),
    pass_header: str = Header(None),
):
    if not mysql_available:
        return {"error": "Module 'mysql.connector' is missing. Please install it to enable database connectivity."}

    try:
        # Connect to the user database
        try:
            connection_userinfo = mysql.connector.connect(**USERINFO_DB_CONFIG)
            cursor_userinfo = connection_userinfo.cursor()

            sqlGetUserInfo = f"SELECT * FROM userData WHERE benutzername = %s AND password = %s"
            cursor_userinfo.execute(sqlGetUserInfo, (username_header, pass_header))
            user_result = cursor_userinfo.fetchall()

            if not user_result:
                return {
                    "header": username_header,
                    "message": "Access Denied - Username or password not found in user database"
                }
        except Error as user_error:
            return {"error": f"Failed to connect to user database: {str(user_error)}"}

        # Connect to the billing database
        try:
            connection_billing = mysql.connector.connect(**BILLING_DB_CONFIG)
            cursor_billing = connection_billing.cursor()

            sqlGetBillingInfo = f"SELECT hasPaid FROM userBilling WHERE benutzername = %s"
            cursor_billing.execute(sqlGetBillingInfo, (username_header,))
            billing_result = cursor_billing.fetchall()

            if not billing_result:
                return {
                    "header": username_header,
                    "message": "Access Denied - No billing information found for user"
                }

            hasPaid = billing_result[0][0]

            if hasPaid == 1:
                return {
                    "header": username_header,
                    "user_data": user_result,
                    "billing_status": "Paid"
                }
            else:
                return {
                    "header": username_header,
                    "message": "Access Denied - User has not paid"
                }
        except Error as billing_error:
            return {"error": f"Failed to connect to billing database: {str(billing_error)}"}

    finally:
        # Close connections safely
        if 'connection_userinfo' in locals() and connection_userinfo.is_connected():
            cursor_userinfo.close()
            connection_userinfo.close()
        if 'connection_billing' in locals() and connection_billing.is_connected():
            cursor_billing.close()
            connection_billing.close()

# Wenn ja, dann abfrage in der Billing DB ob Rechnung bezahlt, wenn ja dann Daten aus mysql-container liefern. Wenn NEIN, dann eine "Access Denied" meldung zürückschicken
