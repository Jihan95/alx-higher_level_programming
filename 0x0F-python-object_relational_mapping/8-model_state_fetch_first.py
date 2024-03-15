#!/usr/bin/python3
"""
Module that lists all State objects from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    first = sys.argv[1]
    second = sys.argv[2]
    third = sys.argv[3]
    en = 'mysql+mysqldb://{}:{}@localhost/{}'.format(first, second, third)
    engine = create_engine(en, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
