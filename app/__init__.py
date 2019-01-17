import psycopg2, os
from bless.libs import utils

CUR_DIR = os.getcwd()
config_data = utils.yaml_read(CUR_DIR+"/config.ocha")['config']

username = config_data['database']['username']
database = config_data['database']['name']
ssl = config_data['database']['ssl']
port = config_data['database']['port']
host = config_data['database']['host']

conn = psycopg2.connect(
    database=database,
    user=username,
    sslmode=ssl,
    port=port,
    host=host
)

conn.set_session(autocommit=True)
db = conn.cursor()