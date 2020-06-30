import os
import sqlalchemy as sa

from sqlalchemy.orm import sessionmaker

from base import Base
import party, account, policy, claim, assessment

engine = sa.create_engine(
            'sqlite:///pcdm.db',
            echo=True
        )
session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

os.remove('pcdm.db')
