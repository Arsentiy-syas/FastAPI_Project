# from database_core.core import create_tables, insert_data

import asyncio
from database_core.orm import SyncORM
from database_core.core import SyncCore



SyncORM.create_tables()
SyncORM.insert_workers()
SyncORM.select_workers()
SyncORM.update_data()

# SyncCore.create_tables()
# SyncCore.insert_data()
# SyncCore.select_workers()
# SyncCore.update_workers()
