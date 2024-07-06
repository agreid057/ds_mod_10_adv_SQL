
from flask import Flask, jsonify
import pandas as pd
import numpy as np
from sqlHelper import SQLHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sql = SQLHelper()

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation_orm<br/>"
      
    )

# SQL Queries
@app.route("/api/v1.0/precipitation_orm")
def precipitation_orm():
    data = sql.query_precipitation_orm()
    return(jsonify(data))


# Run the App
if __name__ == '__main__':
    app.run(debug=True)
