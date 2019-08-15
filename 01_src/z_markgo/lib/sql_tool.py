# 原生sql分页查询
def mysql_page(db,sql,offset,limit,sort=None):
    total = db.session.execute("select count(*) from (" +sql+") t").fetchall()[0][0]
    page_sql = "select * from ( %s) t "%sql
    asc = " asc "
    if sort:
        if sort[0] == "-":
            sort = sort[1:]
            asc = " desc "
    page_sql = page_sql + "order by %s %s"%(sort,asc)
    page_sql = page_sql + " limit %s ,%s "%(offset,limit)
    res = db.session.execute(page_sql).fetchall()
    return res,total

#SQLAlchemy 对象分页查询
def model_page(query,limit,offset,sort=None):
    total = query.count()
    asc = True
    if sort:
        if sort[0] == "-":
            sort = sort[1:]
            asc = False
        for col in query.column_descriptions:
            if col["name"] == sort:
                if asc:
                    query = query.order_by(col["expr"].asc())
                else:
                    query = query.order_by(col["expr"].desc())
                break
    res = query.offset(offset).limit(limit).all()
    return res,total