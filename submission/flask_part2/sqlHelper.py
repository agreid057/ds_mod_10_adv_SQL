import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, func
import datetime

import pandas as pd
import numpy as np

# The Purpose of this Class is to separate out any Database logic
class SQLHelper():
    #################################################
    # Database Setup
    #################################################

    # define properties
    def __init__(self):
        self.engine = create_engine("sqlite:///hawaii.sqlite")
        self.Base = None

        # automap Base classes
        self.init_base()

    def init_base(self):
        # reflect an existing database into a new model
        self.Base = automap_base()
        # reflect the tables
        self.Base.prepare(autoload_with=self.engine)

    #################################################
    # Database Queries
    #################################################

    def query_precipitation_orm(self):
        # Save reference to the table
        Measurement = self.Base.classes.measurement

        # Create our session (link) from Python to the DB
        session = Session(self.engine)

        # Calculate the date one year from the last date in data set.
        start_date = datetime.date(2016, 8, 23)

        # Perform a query to retrieve the data and precipitation scores
        results = session.query(Measurement.date, Measurement.station, Measurement.prcp).\
        filter(Measurement.date >= start_date).\
        order_by(Measurement.date.asc()).\
        all()

        # Save the query results as a Pandas DataFrame. Explicitly set the column names
        station_year = pd.DataFrame(results,columns = ["Date", "Station", "precipitation"])

        # Sort the dataframe by date
        station_year["Date"] = pd.to_datetime(station_year['Date'])
        station_year = station_year.sort_values(by= "Date", ascending = True).reset_index(drop= True)

        # close session
        session.close()

        data = station_year.to_dict(orient="records")
        return(data)
    
    
    
