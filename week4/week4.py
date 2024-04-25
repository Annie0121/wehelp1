
from fastapi import FastAPI, Request,Form
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.add_middleware(SessionMiddleware, secret_key="789456123")

USERNAME = 'test'
PASSWORD = 'test'

# @app.exception_handler(HTTPException)
# async def http_exception_handler(request, exc):
#     return RedirectResponse(url="/error?message=請輸入帳號密碼", status_code=exc.status_code, headers={"Location": "/error"})



@app.get("/")
async def item(request: Request):
    return templates.TemplateResponse(request=request, name="homepage.html")


@app.post("/signin")
async def signin(request: Request ):
    form_data = await request.form()
    username = form_data.get("username")
    password = form_data.get("password")

    if username==USERNAME and password==PASSWORD:
        request.session["SIGNED-IN"] = True
        return RedirectResponse(url="/member",status_code=303)
    elif not username or not password:
        return RedirectResponse(url="/error?message=請輸入帳號密碼", status_code=303)
    else:
        return RedirectResponse(url="/error?message=帳號、或密碼錯誤", status_code=303)




@app.get("/member")
async def member(request: Request):
    signed_in = request.session.get("SIGNED-IN", False)
    if signed_in:
      return templates.TemplateResponse("success.html",{"request":request,"message":"恭喜您，成功登入系統","title":"歡迎光臨，這是會員頁面"})
    else:
        return RedirectResponse(url="/", status_code=303)

@app.get("/signout")
async def signout(request: Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse(url="/", status_code=303)



@app.get("/error")
async def error(request: Request,message:str):
       return templates.TemplateResponse("error.html", {"request": request, "message": message})

if __name__ == '__main__':
    uvicorn.run(app="week4:app", reload=True)
