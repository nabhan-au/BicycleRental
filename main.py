from utilities.session_db import RentalDB

db = RentalDB()
users = db.get_users().get_user_with_id()