# 原生sql分页查询
def mysql_page(db,sql,offset,limit):
    total = db.session.execute("select count(*) from (" +sql+") t").fetchall()[0][0]
    sql = sql + " limit %s ,%s "%(offset,limit)
    res = db.session.execute(sql).fetchall()
    return res,total

#SQLAlchemy 对象分页查询
def model_page(query,limit,offset):
    total = query.count()
    res = query.offset(offset).limit(limit).all()
    return res,total