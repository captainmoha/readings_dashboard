from flask import render_template

from flaskapp import app, db
from flaskapp.models import Log

import pandas as pd


def get_readings_df():

    readings_df = pd.read_sql_table('readings',
                                    con=db.engine,
                                    coerce_float=False)

    readings_df.set_index(['index'], inplace=True)
    readings_df.index.name = None
    readings_df.columns.name = 'ID'

    return readings_df


@app.route('/')
def index():

    readings_df = get_readings_df()

    # for getting stats on durations(max, std, mean)
    duration_series = pd.to_timedelta(readings_df['duration'])

    # log data access
    new_log = Log()
    db.session.add(new_log)
    db.session.commit()

    # get logs
    req_count = new_log.id
    last_access = new_log.time_stamp

    
    return render_template('layout.html', count=req_count,
                           data=readings_df.to_html(na_rep='-', justify='center'),
                           last_access=last_access,
                           stats={'temp': readings_df['temperature'],
                           'duration': duration_series.dt.total_seconds()
                           })
