import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station



#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start date<br/>"
        f"/api/v1.0/start date/end date"
    )


@app.route("/api/v1.0/precipitation")
def prcp():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    result = session.query(Measurement.date,Measurement.prcp).order_by(Measurement.date).all()
    
    session.close()
    
    # Create a dictionary from the row data and append to a list of all_passengers
    all_prcp = []
    for date,prcp in result:
        prcp_dict = {}
        prcp_dict[date] = prcp
        all_prcp.append(prcp_dict)
    return jsonify(all_prcp)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    result = session.query(Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation).all()
    
    session.close()
    
    
    return jsonify(result)

@app.route("/api/v1.0/tobs")
def tob():
    session = Session(engine)
    
    sel_2 = [Station.station,Station.name,func.count(Measurement.station)]
    
    stations_ranking = session.query(*sel_2).filter(Station.station == Measurement.station).\
                            group_by(Measurement.station).\
                            order_by(func.count(Measurement.station).desc()).all()
    
    the_most_active_station_id = stations_ranking[0][0]

    last_day = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    first_day = dt.date(2017,8,23) - dt.timedelta(days=365)

    result = session.query(Measurement.date,Measurement.prcp).\
                filter(Measurement.date >= first_day).\
                filter(Measurement.station == the_most_active_station_id).\
                order_by(Measurement.date).all()
    session.close()
    
    return jsonify(result)

@app.route("/api/v1.0/<start>")
def start_only(start):
    session = Session(engine)
    
    sel = [func.min(Measurement.tobs),
          func.avg(Measurement.tobs),
          func.max(Measurement.tobs)]
    
    year, month, day = map(int, start.split('-'))
    start_date = dt.date(year, month, day)

    
    result = session.query(*sel).filter(Measurement.date >= start_date).all()
    session.close()
    
    return jsonify(result)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    session = Session(engine)
    
    sel = [func.min(Measurement.tobs),
          func.avg(Measurement.tobs),
          func.max(Measurement.tobs)]
    
    year_start, month_start, day_start = map(int, start.split('-'))
    start_date = dt.date(year_start, month_start, day_start)
    
    year_end, month_end, day_end = map(int, end.split('-'))
    end_date = dt.date(year_end, month_end, day_end)
    
    result = session.query(*sel).filter(Measurement.date >= start_date).\
                                 filter(Measurement.date <= end_date).all()
    session.close()
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)