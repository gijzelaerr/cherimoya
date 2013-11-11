from cherimoya.db import db

db.engine.echo = True
db.create_all()
