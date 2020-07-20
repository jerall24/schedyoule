# create_db.py

from app.website import db
from app.models import Role

# create the database and the db table
db.create_all()

# commit the changes
db.session.commit()