from fastapi import Request

async def simple_log(request: Request, call_next):
    print(f"Route requested: {request.url.path} ({request.method})")
    response = await call_next(request)
    return response