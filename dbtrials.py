from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mypkg.db import Advertisement

engine = create_engine('mysql://root:welcome1@localhost/csfeedback', echo=True)
Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

#recs = session.query(Advertisement).filter_by(name='add1').first()
#print recs

for instance in session.query(Advertisement).order_by(Advertisement.name):
    print ' | '.join([instance.name, instance.description])

    


