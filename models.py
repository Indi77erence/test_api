from datetime import datetime, date
from typing import Union
import ormar
from ormar import Date, DateTime

from db import metadata, database


class MainMeta(ormar.ModelMeta):
	metadata = metadata
	database = database


class Task(ormar.Model):
	class Meta(MainMeta):
		pass
		
	id: int = ormar.Integer(primary_key=True)
	task_name: str = ormar.String(max_length=50)
	description: str = ormar.String(max_length=1000)
	creat_at: str = ormar.String(max_length=50)


class Files(ormar.Model):
	class Meta(MainMeta):
		pass
		
	id: int = ormar.Integer(primary_key=True)
	title: str = ormar.String(max_length=50)
	description: str = ormar.String(max_length=1000)
	file: str = ormar.String(max_length=100)
	task: Union[Task, int, None] = ormar.ForeignKey(Task)
