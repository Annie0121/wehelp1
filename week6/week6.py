
from fastapi import FastAPI, Request,Form
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from typing import Annotated
from fastapi import Path
import mysql.connector
import config


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=config.password,
  database="website"
)
mycursor = mydb.cursor()

app = FastAPI()
templates = Jinja2Templates(directory="templates")


app.add_middleware(SessionMiddleware, secret_key="789456123")







@app.get("/")
async def item(request: Request):
    return templates.TemplateResponse(request=request, name="homepage.html")




@app.post("/signup")
async def signup(request: Request,name: Annotated[str, Form()]=None,username: Annotated[str, Form()]=None, password: Annotated[str, Form()]=None):
    cursor = mydb.cursor()
    sql = "INSERT INTO member(name, username, password) VALUES (%s, %s, %s);"
    val = (name, username, password)

    check_sql = "SELECT username FROM member WHERE username = %s"
    cursor.execute(check_sql, (username,))
    records = cursor.fetchall()


    if records:
       return RedirectResponse(url="/error?message=帳號已被註冊", status_code=303)

    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    return RedirectResponse(url="/", status_code=303)



@app.post("/signin")
async def signin(request: Request,username: Annotated[str, Form()]=None, password: Annotated[str, Form()]=None ):
    mycursor = mydb.cursor()
    check_username = 'SELECT id ,name,username from member WHERE  username = %s and password = %s'
    mycursor.execute(check_username, (username, password))
    records = mycursor.fetchall()

    if  records:

        ID = records[0][0]
        name = records[0][1]
        username = records[0][2]

        request.session["ID"] = ID
        request.session["NAME"] = name
        request.session["USERNAME"] = username
        request.session["SIGNED-IN"] = True

        return RedirectResponse(url="/member",status_code=303)
    elif not password or not username:
        return RedirectResponse(url="/error?message=請輸入帳號密碼", status_code=303)
    else:
        return RedirectResponse(url="/error?message=帳號、或密碼錯誤", status_code=303)




@app.get("/member")
async def member(request: Request):
    signed_in = request.session.get("SIGNED-IN", False)
    username = request.session.get("USERNAME")
    ID =request.session.get("ID")
    name =request.session.get("NAME")
    contents_and_names = []
    mycursor.execute(
        "select message.content ,member.name from message left outer join member on member.id = message.member_id ;")
    infos = mycursor.fetchall()
    for i in infos:
        content = i[0]
        uname = i[1]
        contents_and_names.append((content, uname))

    template_context={"request": request,
                     "message": f"{name}， 歡迎登入系統",
                     "title": "歡迎光臨，這是會員頁面",
                      "contents_and_names": contents_and_names
                      }


    if signed_in:
        return templates.TemplateResponse("member.html", template_context)

    else:
        return RedirectResponse(url="/", status_code=303)

@app.post("/createMessage")
async  def createMessage(request: Request,message: Annotated[str, Form()]=None):

    ID = request.session.get("ID")
    cursor = mydb.cursor()
    message_id='INSERT INTO message (content, member_id) SELECT %s,  id FROM member WHERE id = %s;'
    mycursor.execute(message_id,(message,ID))
    mydb.commit()
    cursor.close()
    return RedirectResponse(url="/member", status_code=303)



@app.get("/signout")
async def signout(request: Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse(url="/", status_code=303)



@app.get("/error")
async def error(request: Request,message:str):
       return templates.TemplateResponse("error.html", {"request": request, "message": message})




if __name__ == '__main__':
    uvicorn.run(app="week6:app", reload=True)
