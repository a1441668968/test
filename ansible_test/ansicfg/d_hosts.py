from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine(
    'sqlite:////root/test/ansible_test/db.sqlite3',
    encoding='utf8'
)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Group(Base):
    __tablename__ = 'webansi_group'
    id = Column(Integer, primary_key=True)
    hostgroup = Column(String(50))

    def __str__(self):
        return self.hostgroup


class Host(Base):
    __tablename__ = 'webansi_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50))
    ip = Column(String(15))
    group_id = Column(Integer, ForeignKey('webansi_group.id'))


if __name__ == '__main__':
    session = Session()
    qset = session.query(Group.hostgroup, Host.ip).join(Host, Group.id == Host.id)
    host_list = qset.all()
    print(host_list)
    # result = {}
    # for group, ip in host_list:
    #     if group not in result:
    #         result[group] = {'hosts': []}
    #     result[group]['hosts'].append(ip)
    # print(json.dumps(result))
