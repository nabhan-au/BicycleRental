from utilities.session_db import SessionDB

db = SessionDB()
bicycle = db.get_bicycle().get_bicycle_from_brand('3T')
# users = db.get_bicycle().get_bicycle_from_type('Touring Bike')
print(bicycle)

user = db.get_users().get_user_from_age(30)