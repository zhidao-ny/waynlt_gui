import sqlite3
from visual import drawbarchart

db = sqlite3.connect('testdb.sqlite')
cursor = db.cursor()
import pandas as pd
def companysearch(companyname):
    sql = "select skill, num from company_skill where comp_name = ? order by num desc limit 5"
    df = pd.read_sql(sql, db, params= [companyname])
    print(df)
    drawbarchart(df)
    return df
def skillsearch(skillname):
    sql = "select comp_name, num from company_skill where skill = ? order by num desc limit 5"
    df = pd.read_sql(sql, db, params= [skillname])
    print(df)
    drawbarchart(df)
    return df


