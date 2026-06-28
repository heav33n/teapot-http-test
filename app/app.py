from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(
    debug=False,
    title="TestApp",
    version="0.0.1",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    swagger_ui_oauth2_redirect_url="/api/docs/oauth2-redirect",
)

app.frontend("/", directory="dist")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["teapot-http-test-production.up.railway.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/response")
def return_tea(is_tea: bool = False):
    if not is_tea:
        return JSONResponse(
            status_code=418,
            content={"response": "I'm not making coffee, sorry."},
        )

    return {"response": "I'm making tea."}
