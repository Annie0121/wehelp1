
from fastapi import FastAPI, Request,Form
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from typing import Annotated
from fastapi import Path


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 將 SessionMiddleware 中介軟體添加到了應用程式中，並設置了一個參數 secret_key 用於加密會話數據
app.add_middleware(SessionMiddleware, secret_key="789456123")

USERNAME = 'test'
PASSWORD = 'test'

# @app.exception_handler(HTTPException)
# async def http_exception_handler(request, exc):
#     return RedirectResponse(url="/error?message=請輸入帳號密碼", status_code=exc.status_code, headers={"Location": "/error"})



@app.get("/")
async def item(request: Request):
    return templates.TemplateResponse(request=request, name="homepage.html")


@app.post("/signin")                       #Annotated 主要用於為參數類型添加元數據,參數的默認值為 None
async def signin(request: Request,username: Annotated[str, Form()]=None, password: Annotated[str, Form()]=None ):  #此函式接受一個名為 request 的參數，它是一個 Request 物件，代表了客戶端向伺服器發送的 HTTP 請求
    # form_data = await request.form()
    # username = form_data.get("username")
    # password = form_data.get("password")

    if username==USERNAME and password==PASSWORD:
        #request在http請求中,設置會話（session）數據,request.session 是一個字典（dictionary），用於存儲有關當前用戶會話的數據"SIGNED-IN" 作為鍵（key）
        #目的是將用戶的登入狀態儲存在 session 中，以便後續在應用程式中驗證用戶的登入狀態。
        request.session["SIGNED-IN"] = True   #  瀏覽器收到 303 狀態碼後會自動將用戶重定向到指定的 /member 頁面
        return RedirectResponse(url="/member",status_code=303)   # RedirectResponse 是一種 HTTP 響應類型，用於將用戶導向（重新定向）到另一個 URL
    elif not username or not password:
        return RedirectResponse(url="/error?message=請輸入帳號密碼", status_code=303)
    else:
        return RedirectResponse(url="/error?message=帳號、或密碼錯誤", status_code=303)




@app.get("/member")
async def member(request: Request):
    signed_in = request.session.get("SIGNED-IN", False)  #.get() 方法返回指定鍵對應的值，如果鍵不存在於字典中，則返回默認值。
    if signed_in:    #如果會話數據中存在 "SIGNED-IN"，則將其值賦給 signed_in 變數；如果不存在，則將 signed_in 賦值為 False。
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

@app.get("/square/{item_id}")
async def square(request:Request,item_id: int = Path(...)):   #int = Path(...)會自動將數值轉換成int
    square_number=item_id**2  #Path 函數用於定義路徑,需要傳遞至少一個參數給它,使用 Path(...) 的形式，將參數留空，告訴 FastAPI 您正在定義一個路徑參數，但不指定具體的值。
    return templates.TemplateResponse("number.html",{"request": request,"square_number": square_number})


if __name__ == '__main__':
    uvicorn.run(app="week4:app", reload=True)
