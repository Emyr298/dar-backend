from fastapi import FastAPI
import uvicorn
import firebase_admin

from config import Config
from interceptors.middlewares.auth import AuthMiddleware
from exceptions.handler import exception_handler

from routes.http.auth_router import router as auth_router
from routes.http.user_router import router as user_router

# Firebase
firebase_admin.initialize_app(Config.firebase.credentials)

# FastAPI app
app = FastAPI()
app.add_exception_handler(handler=exception_handler, exc_class_or_status_code=Exception)

# Middlewares
app.add_middleware(middleware_class=AuthMiddleware)

# Routers
app.include_router(auth_router, prefix='/auth')
app.include_router(user_router, prefix='/user')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
