import uvicorn, yaml, os, aiofiles, settings, crud, models, requests, json
import pandas as pd
import sqlalchemy
from sqlalchemy.orm import Session
from fastapi import FastAPI, File, UploadFile, Cookie, Form, Depends
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from annotated_types import Annotated

from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

template = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static", html=True), name="static")



def get_db():
    db = settings.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def req_test_budy():
    q = """query getListDevices {
        data: Device {
            data: getList(filter:{}, perPage: 10000) {
            items {
                ...DeviceFragment
            }
            }
        }
        }

        fragment DeviceFragment on Device {
        id active
        asset { 
            id name deleted
            tagsByDatagrid {id value type quality timestamp}
            createdAt createdById
        }
        }
        """
    
    return q

def test_user(token):
    url = 'https://dispatcher.farvater.group/api/gateway/'
    schema = {"query":req_test_budy()}
    headers  = {'Authorization': f'Bearer {token}'}
    req = requests.post(url= url,json = schema, headers=headers)
    return json.loads(req.content)

@app.get("/")
async def redirect(request: Request):
    return RedirectResponse("/auth", status_code=301)

@app.get("/auth")
async def redirect(request: Request):
    return template.TemplateResponse("auth.html", {'request':request})


@app.get("/admin")
async def admin(request: Request, token_autz = Cookie(None)):
    test = test_user(token_autz)
    print(token_autz)
    print(test)
    if 'errors' in dict(test).keys():
        raise HTTPException(403)
    else:
        return template.TemplateResponse("admin.html", {'request':request})

@app.post("/admin")
async def admin_post(request: Request, files: list[UploadFile], db: Session = Depends(get_db), token_autz = Cookie(None)):
    test = test_user(token_autz)
    print(token_autz)
    print(test)
    if 'errors' in dict(test).keys():
        raise HTTPException(403)
    else:
        try:
            for file in files:
                if not file.filename.endswith(".xlsx") and not file.filename.endswith(".xls"):
                    raise Exception("Invalid file type")
                with open(file.filename, "wb") as f:
                    f.write(file.file.read())
                sheets = pd.ExcelFile(file.filename).sheet_names
                for sheet in sheets:
                    df = pd.read_excel(file.filename, sheet_name=sheet, index_col=0, header=1, usecols="A:E", na_values=False)
                    with settings.engine.connect() as con:
                        df.to_sql(sheet, con, if_exists='replace', index=False)

        except Exception as e:
            print(e)

@app.get('/get_db')
async def get_db(request: Request, db: Session = Depends(get_db)):
    data = crud.read_all(db)
    return json.dumps(data)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT)