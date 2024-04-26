#!/usr/bin/python3
"""
Module that prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
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

    data = session.query(State, City).filter(State.id == City.state_id).\
        order_by(City.id).all()

    for state, city in data:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
