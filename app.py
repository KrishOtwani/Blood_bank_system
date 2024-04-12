from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import func

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


class Track(db.Model):
    """A Model for an Item in the Todo List

    Args:
        db (_type_): database model

    Returns:
        __repr__: string rep.
    """
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))
    units = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    # def __repr__(self):
    #     return f'<Task {self.id}'

with app.app_context():
    db.create_all()


@app.route('/', methods=["POST","GET"])
def index():

    num_units_Apos = db.session.query(func.sum(Track.units)).filter(Track.type == 'A+').scalar()
    num_units_Apos = num_units_Apos or 0

    num_units_Aneg = db.session.query(func.sum(Track.units)).filter(Track.type == 'A-').scalar()
    num_units_Aneg = num_units_Aneg or 0

    num_units_Bpos = db.session.query(func.sum(Track.units)).filter(Track.type == 'B+').scalar()
    num_units_Bpos = num_units_Bpos or 0

    num_units_Bneg = db.session.query(func.sum(Track.units)).filter(Track.type == 'B-').scalar()
    num_units_Bneg = num_units_Bneg or 0

    num_units_ABpos = db.session.query(func.sum(Track.units)).filter(Track.type == 'AB+').scalar()
    num_units_ABpos = num_units_ABpos or 0

    num_units_ABneg = db.session.query(func.sum(Track.units)).filter(Track.type == 'AB-').scalar()
    num_units_ABneg = num_units_ABneg or 0

    num_units_Opos = db.session.query(func.sum(Track.units)).filter(Track.type == 'O+').scalar()
    num_units_Opos = num_units_Opos or 0

    num_units_Oneg = db.session.query(func.sum(Track.units)).filter(Track.type == 'O-').scalar()
    num_units_Oneg = num_units_Oneg or 0

    num_units=[num_units_Apos,num_units_Aneg,num_units_Bpos,num_units_Bneg,num_units_ABpos,num_units_ABneg,num_units_Opos,num_units_Oneg]

    return render_template('homepage2.html', num_rows=num_units)

@app.route('/donate', methods=["POST","GET"])
def donate():

    if request.method == "GET":
        # num_rows_A_plus = track.session.query(track).filter(track.type == 'A+').count()
        # num_rows = db.session.query(Track).count() , num_rows=num_rows
        return render_template('donate2.html')

    else:   
        units = request.form['units']
        blood_group = request.form['blood-group']
        new_task = Track(type=blood_group, units=units)
        
        # units = request.form['units']
        # new_task = track(units=units)

        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/') 
        
        except Exception as e:
            print(f"Error:{e}")
            return f'Error:{e}'
        
        

    

@app.route('/receive', methods=["POST","GET"])
def receive():
    
    
    if request.method == "POST":   
        print("hiiiii")
        units = int(request.form['units'])
        print(units)
    
        negunits = -units
        print(negunits)

        blood_group = request.form['blood-group']
        new_task = Track(type=blood_group, units=negunits)
        if units==None:
            print("hehehehe")
        print("hi", units)
        # units = request.form['units']
        # new_task = track(units=units)
        # blood_record = Track.query.filter_by(b_group=blood_group).first()

        # if blood_record:
        #     # Add the negative units to the existing units in the database
        #     blood_record.units -= units
                
        #     db.session.commit()
        #     return redirect('/')
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/') 
        
        except Exception as e:
            print(f"Error:{e}")
            return f'Error:{e}'
        
    if request.method == "GET":
        return render_template('receive2.html')


@app.route('/view_tracks', methods = ["POST","GET"])
def view_tracks():
    tracks = Track.query.all()
    for track in tracks:
        print(track.id, track.type, track.units, track.date_created)
    return "Tracks viewed successfully!"


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)