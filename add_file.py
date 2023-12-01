import re
from uuid import uuid4

import aiofiles
from _asyncio import Task
from fastapi import UploadFile

from models import Files
from schemas import AddFiles


async def save_file(task: Task, file_add: UploadFile, title: str, description: str):
	format_file = '.' + re.findall(r'\w+', file_add.filename)[1]
	path_file = f'media/task_file/{task.id}_{uuid4()}{format_file}'
	await write_video(path_file, file_add)
	info = AddFiles(title=title, description=description)
	return await Files.objects.create(file=path_file, task=task.id, title=info.title, description=info.description)


async def write_video(file_name: str, file_add: UploadFile):
	async with aiofiles.open(file_name, 'wb') as buffer:
		data = await file_add.read()
		await buffer.write(data)