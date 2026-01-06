from sqlalchemy import text, insert, select
from .database import sync_engine, async_engine, session_factory, asyc_session_factory
from .models import metadata_obj, workers_table, WorkersOrm
from .core import SyncCore

class SyncORM:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with session_factory() as session:
            worker_bobr = WorkersOrm(username='Jhon')
            worker_volk = WorkersOrm(username='Miha')
            session.add_all([worker_bobr, worker_volk])
            session.flush()
            session.commit()

    @staticmethod
    def select_workers():
        with session_factory() as session:
            query = select(WorkersOrm)
            result = session.execute(query)
            workers = result.scalars().all()
            print(f'{workers=}')

    @staticmethod
    def update_data(worker_id: int = 2, new_username: str = 'Michael'):
        with session_factory() as session:
            worker_Misha = session.get(WorkersOrm, worker_id)
            worker_Misha.username = new_username
            session.commit()