from cherimoya import db, app

db.db.app = app
db.db.create_all()
