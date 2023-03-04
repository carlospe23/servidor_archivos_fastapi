from fastapi import APIRouter
from fastapi import UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from os import getcwd, remove

router = APIRouter()

@router.post('/upload')
async def upload_file(file:UploadFile = File(...)):
    with open(getcwd() +'/'+ file.filename, 'wb') as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()

    return 'Succes'


@router.get('/file/{file_name}')
def get_file(file_name: str):
    return FileResponse(getcwd() +'/'+ file_name)


@router.get('/download/{file_name}')
def download_file(file_name: str):
    return FileResponse(getcwd() +'/'+ file_name, media_type='application/octet-stream', filename=file_name)


@router.delete('/delete/{file_name}')
def delete_file(file_name: str):
    try:
        remove(getcwd() +'/'+ file_name)
        return JSONResponse(content={
            'removed': True, 
            'message':f'the file was succes fully deleted'}, 
            status_code=200
        )
    except FileNotFoundError as exce:
        return JSONResponse(content={
            'removed': False, 
            'message':f'the file was not removed {exce}'}, 
            status_code=404
        )
    return 'Succes'
