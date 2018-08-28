from sqlalchemy_test import Departments, Session, Salary, Employees
from sqlalchemy import and_, or_

session = Session()

qselect1 = session.query(Departments).order_by(Departments.dep_id)
print(qselect1)
for dep in qselect1:
    print(dep)

qselect2 = session.query(Departments.dep_id, Departments.dep_name).order_by(Departments.dep_id)
print(qselect2)
for id, name in qselect2:
    print(id, name, sep=':')

qcut = session.query(Departments)[1:3]
print(qcut)
for dep in qcut:
    print(dep.dep_name)

qfilter = session.query(Departments.dep_name).filter(Departments.dep_id == 2)
print(qfilter)
for dep in qfilter:
    print(dep.dep_name)

qselect3 = session.query(Salary.date, Salary.id, Salary.basic + Salary.awards)
print(qselect3)
for date, id, money in qselect3:
    print(date, id, money, sep=':')

qfind = session.query(Departments.dep_id).filter(Departments.dep_name.in_(['运维部', '开发部']))
print(qfind)
for id in qfind:
    print(id)

qnotfind = session.query(Departments.dep_id).filter(~Departments.dep_name.in_(['运维部', '开发部']))
print(qnotfind)
for id in qnotfind:
    print(id)

qselect4 = session.query(Employees).filter(and_(Employees.gender == 'male', Employees.dep_id == 2))
print(qselect4)
for employ in qselect4:
    print(employ.name)

qselect5 = session.query(Employees).filter(or_(Employees.gender == 'female', Employees.dep_id == 1))
print(qselect5)
for employ in qselect5:
    print(employ.name)

print(qselect2.all())
print(qselect2.first())
print(qselect5.one())
print(qselect5.scalar())

qcount = session.query(Departments).count()
print(qcount)

qjoin = session.query(Employees.name, Departments.dep_name).join(Departments, Employees.dep_id == Departments.dep_id)
print(qjoin.all())
