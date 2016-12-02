from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class User(Base):

    __tablename__ = 'user'


    id = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql//root:root@localhost:3306/test?charset=utf8',echo=True)

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_user = User(id='5', name='Bob')


session.add(new_user)
session.commit()
session.close()


session = DBSession()
user = session.query(User).filter(User.id == '5').one()

print 'type: ', type(user)
print 'name: ', user.name

