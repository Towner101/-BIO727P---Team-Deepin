import sqlite3

def get_db_connection():
    conn = sqlite3.connect('Static/SNPdatabase.db')
    return conn

def get_snp_data(snp_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SIBStats WHERE snpstatsID=?", (snp_id,))
    result = cursor.fetchone()
    conn.close()
    return result

test=get_snp_data('1:10420:A:C')
print(test)
