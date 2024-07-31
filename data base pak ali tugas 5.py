# ARDIAN SETIAWAN - 41823010043
# Universitas Mercu Buana
# Tugas 5 - Pemrograman Lanjut

import MySQLdb

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '',
    'db': 'fastapi',
}

# Create a connection to the database``
conn = MySQLdb.connect(**db_config)