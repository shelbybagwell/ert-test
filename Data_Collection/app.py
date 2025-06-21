from flask import Flask, Response, jsonify, request
import sqlite3

import jsonpickle

from api import NOAA_SWPC_API
from models import RTSW_data


app = Flask(__name__)

db = sqlite3.connect("noaa_data.sql")
db.execute(
    "CREATE TABLE IF NOT EXISTS data ( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        time_tag TEXT, \
        speed REAL, \
        density REAL, \
        temperature INTEGER, \
        bx REAL, \
        by REAL,\
        bz REAL, \
        bt REAL, \
        vx REAL, \
        vy REAL, \
        vz REAL, \
        propogated_time_tag TEXT \
    );"
)


@app.route("/rtsw", methods=["GET"])
def get_rtsw_data():
    persist = request.args.get("persist")
    if persist != "True" or persist != "true":
        persist = False
    else:
        persist = True
    noaa = NOAA_SWPC_API()
    rtsw = noaa.get_RTSW()
    # print(data)
    if persist:
        db = sqlite3.connect("noaa_data.sql")
        for el in rtsw:
            db.execute(
                f"INSERT INTO rtsw_data (time_tag, \
                    speed, \
                    density, \
                    temperature, \
                    bx, \
                    by, \
                    bz, \
                    bt, \
                    vx, \
                    vy, \
                    vz, \
                    propogated_time_tag) \
                VALUES ({el['time_tag']}, \
                    {el['speed']}, \
                    {el['density']}, \
                    {el['temperature']}, \
                    {el['bx']}, \
                    {el['by']}, \
                    {el['bz']}, \
                    {el['bt']}, \
                    {el['vx']}, \
                    {el['vy']}, \
                    {el['vz']}, \
                    {el['propagated_time_tag']});"
            )
    return rtsw


app.run(debug=True, host="0.0.0.0", port=5002)
