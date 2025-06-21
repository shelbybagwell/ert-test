from flask import Flask, request
import sqlite3

from api import NOAA_SWPC_API


app = Flask(__name__)

db = sqlite3.connect("noaa_data.sqlite")
db.execute(
    "CREATE TABLE IF NOT EXISTS rtsw_data ( \
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
    print(request.args.get("persist"))
    persist = request.args.get("persist")
    if persist != "True" and persist != "true":
        print("thinks persist isnt true")
        persist = False
    else:
        persist = True
    noaa = NOAA_SWPC_API()
    rtsw = noaa.get_RTSW()
    if persist:
        print("Persistance requested, saving data...")
        db = sqlite3.connect("noaa_data.sqlite")
        cursor = db.cursor()
        for el in rtsw:
            data = (
                el["time_tag"],
                el["speed"],
                el["density"],
                el["temperature"],
                el["bx"],
                el["by"],
                el["bz"],
                el["bt"],
                el["vx"],
                el["vy"],
                el["vz"],
                el["propagated_time_tag"],
            )
            cursor.execute(
                "INSERT INTO rtsw_data (time_tag, \
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
                VALUES (?, \
                    ?, \
                    ?, \
                    ?, \
                    ?, \
                    ?, \
                    ?, \
                    ?, \
                    ?, \
                    ?, \
                    ?, \
                    ?);",
                data,
            )
        db.commit()
        db.close()
    return rtsw


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
