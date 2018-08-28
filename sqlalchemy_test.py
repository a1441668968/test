from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:@localhost/tarena', encoding='utf8', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Departments(Base):
    __tablename__ = 'departments'
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)

    def __str__(self):
        return '[%s:%s]' % (self.dep_id, self.dep_name)


class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    gender = Column(String(6))
    birthday = Column(Date)
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return '[%s:%s]' % (self.id, self.name)


class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True)
    date = Column(Date)
    id = Column(Integer, ForeignKey('employees.id'))
    basic = Column(Integer)
    awards = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    hr = Departments(dep_name='人事部')
    op = Departments(dep_id=2, dep_name='运维部')
    dev = Departments(dep_id=3, dep_name='开发部')
    qa = Departments(dep_id=4, dep_name='测试部')
    bob = Employees(id=1, name='bob', gender='male', birthday='1992-05-15', email='bob@tedu.cn', dep_id=2)
    alice = Employees(id=2, name='alice', gender='female', birthday='1999-12-28', email='alice@tedu.cn', dep_id=1)
    tom = Employees(id=3, name='tom', gender='male', birthday='1989-01-01', email='tom@tedu.cn', dep_id=3)
    session = Session()
    session.add(hr)
    session.add_all([op, dev, qa])
    session.commit()
    session.add_all([bob, alice, tom])
    session.commit()
    up1 = session.query(Departments).filter(Departments.dep_id == 1)
    up1.update({Departments.dep_name: '人力资源部'})
    session.commit()
    up2 = session.query(Departments).get(1)
    up2.dep_name = '人事部'
    session.commit()
    qdel = session.query(Employees).get(3)
    session.delete(qdel)
    session.commit()
    session.close()
