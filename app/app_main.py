from fastapi import FastAPI
from router import history_rt, ai_serarch_rt, user_rt


app = FastAPI()
# 用户注册登录
app.include_router(user_rt.router)

# 对于历史消息管理
app.include_router(history_rt.router)

# 智能体搜索
app.include_router(ai_serarch_rt.router)

if __name__=='__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    