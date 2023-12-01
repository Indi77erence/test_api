from datetime import datetime
from pathlib import Path
from typing import List
import ormar
from fastapi import APIRouter, UploadFile, BackgroundTasks, Form, File
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates
from add_file import save_file
from models import Task, Files
from schemas import CreateTask, AddFiles, GetAllTasks, GetListFile, GetTask

router = APIRouter()
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))


@router.post('/create_task', response_model=CreateTask)
async def create_task(task: Task, task_name: str, description: str):
	task.creat_at = f'{datetime.utcnow()}'
	task.task_name = task_name
	task.description = description
	return await task.save()


@router.get('/file/all_file/{task_pk}', response_model=List[GetListFile])
async def get_list_file_task(task_pk: int):
	file_list = await Files.objects.filter(task=task_pk).all()
	return file_list


@router.get('/task/all_task', response_model=List[GetAllTasks])
async def get_list_task():
	return await Task.objects.all()


@router.get('/task/{task_id}', response_model=GetTask)
async def get_task(task_id: int):
	try:
		return await Task.objects.filter(id=task_id).first()
	except ormar.exceptions.NoMatch as err:
		return JSONResponse(status_code=404, content={"message": "Задача не найден"})


@router.put('/task/{task_id}', response_model=GetTask)
async def update_task(task_id: int, task_name: str = None, description: str = None):
	try:
		task = await Task.objects.filter(id=task_id).first()
		task.id = task_id
		task.task_name = task_name
		task.description = description
		return await task.update()
	except ormar.exceptions.NoMatch as err:
		return JSONResponse(status_code=404, content={"message": "Задача не найден"})


@router.delete('/task/{task_id}', response_model=GetTask)
async def del_task(task_id: int):
	try:
		task = await Task.objects.filter(id=task_id).first()
		await Task.objects.delete(id=task_id)
		return task
	except ormar.exceptions.NoMatch as err:
		return JSONResponse(status_code=404, content={"message": "Задача не найден"})


@router.post('/upload_file', response_model=AddFiles)
async def upload_file(
		task_id: int,
		title: str = Form(...),
		description: str = Form(...),
		file_add: UploadFile = File(...)
):
	task = await Task.objects.filter(id=task_id).first()
	return await save_file(task, file_add, title, description)
