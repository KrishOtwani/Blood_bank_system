from app import db, track  # Import your SQLAlchemy database object and model

# Query all records from the 'track' table
tracks = track.query.all()

# Print the contents of the 'track' table
for track in tracks:
    print(track.id, track.type, track.units, track.date_created)
