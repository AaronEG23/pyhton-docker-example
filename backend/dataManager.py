import constant
import sqlite3

def createConnection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def prepareDatabase():
	con = createConnection(constant.DATABASE)
	cur = con.cursor()
	cur.execute('DROP TABLE IF EXISTS passiveRate')
	cur.execute('CREATE TABLE passiveRate (year INT, month INT, day INT, value REAL)')


def insert(pYear, pMonth, pDay, pValue): 

	conn = createConnection(constant.DATABASE)
	with conn:
		passiveRate = (int(pYear),int(pMonth),int(pDay),float(pValue))
		sql = ''' INSERT INTO passiveRate(year,month,day,value)
	              VALUES(?,?,?,?) '''
		cur = conn.cursor()
		cur.execute(sql, passiveRate)

def select(pYearStart, pYearEnd, pMonthStart, pMonthEnd):
	con = createConnection(constant.DATABASE)
	cur = con.cursor()
	addAnd = False
	baseQuery = "SELECT avg(value) FROM passiveRate"
	if (pYearStart != None or pYearEnd != None or pMonthStart != None or pMonthEnd != None):
		baseQuery = baseQuery + " WHERE"
	
	if (pYearStart != None):
		baseQuery = baseQuery + " year>="+str(pYearStart)
		addAnd = True

	if (pYearEnd != None):
		if (addAnd):
			baseQuery = baseQuery + " AND"
		baseQuery = baseQuery + " year<="+str(pYearEnd)
		addAnd = True

	if (pMonthStart != None):
		if (addAnd):
			baseQuery = baseQuery + " AND"
		baseQuery = baseQuery + " month>="+str(pMonthStart)
		addAnd = True

	if (pMonthEnd != None):
		if (addAnd):
			baseQuery = baseQuery + " AND"
		baseQuery = baseQuery + " month<="+str(pMonthEnd)
		addAnd = True
	cur.execute(baseQuery)
	result = cur.fetchall()[0][0]
	return result
