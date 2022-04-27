from utilities.session_db import RentalDB

db = RentalDB()
users = db.get_bicycle().get_bicycle_from_brand('3T')
# users = db.get_bicycle().get_bicycle_from_type('Touring Bike')
print(users)