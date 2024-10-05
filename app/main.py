from typing import Annotated

import s3fs
from fastapi import FastAPI, File, Form, UploadFile

s3 = s3fs.S3FileSystem(anon=True)

app = FastAPI()


@app.post("/upload/")
async def upload_file(
    name: Annotated[str, Form()],
    delegation: Annotated[str, Form()],
    discipline: Annotated[str, Form()],
    file: Annotated[UploadFile, File()],
):
    contents = await file.read()
    return {
        "file_size": len(contents),
        "s3filename": f"{discipline}/{delegation}/{name}",
    }
