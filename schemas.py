from ormar import DateTime
from pydantic import BaseModel
from pydantic.schema import datetime



class CreateTask(BaseModel):
	id: int
	task_name: str
	creat_at: str


# timestamp: datetime


class GetListFile(BaseModel):
	title: str
	description: str


# time: datetime.utcnow()


class GetAllTasks(BaseModel):
	id: int
	task_name: str
	description: str
	creat_at: str

# timestamp: datetime.utcnow()


class GetTask(BaseModel):
	id: int
	task_name: str
	description: str
	creat_at: str

# timestamp: datetime.utcnow()


class AddFiles(BaseModel):
	title: str
	description: str


# time: datetime.utcnow()


class GetFiles(BaseModel):
	id: int
	title: str
	task: GetTask
# time: datetime.utcnow()
