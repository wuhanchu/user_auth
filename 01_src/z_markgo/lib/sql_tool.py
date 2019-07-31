
def mysql_page(db,sql,limit,offset):
    total = db.session.execute("select count(*) from (" +sql+") t").fetchall()[0][0]
    sql = sql + " limit %s ,%s "%(offset,limit)
    res = db.session.execute(sql).fetchall()
    return res,total