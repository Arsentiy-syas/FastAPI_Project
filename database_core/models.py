import datetime
from typing import Optional, Annotated
from sqlalchemy import ForeignKey, Table, Column, Integer, String, MetaData, func, text
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base
import enum


idpk = Annotated[int, mapped_column(primary_key=True)]
create_at = Annotated[datetime.datetime, mapped_column(server_default=text('TIMEZONE("uts, now()")'))]
update_at = Annotated[datetime.datetime, mapped_column(
        server_default=text('TIMEZONE("uts, now()")'),
        onupdate=datetime.datetime.utcnow,)]


class WorkersOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[idpk]
    username: Mapped[str]


class Workload(enum.Enum):
    parttime = 'parttime'
    fulltime = 'fulltime'


class ResumesOrm(Base):
    __tablename__ = 'resumes'

    id: Mapped[idpk]
    title: Mapped[str] = mapped_column(String(25))
    compensation: Mapped[str | None]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey('workers.id', ondelete='CASCADE'))
    create_at = Mapped[create_at]
    update_at: Mapped[update_at]






























metadata_obj = MetaData()

workers_table = Table(
    'workers',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String),
)