from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.api.v1 import routes_zones, routes_dns, routes_logs, routes_metrics

settings = get_settings()

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajuste em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_prefix = settings.API_V1_PREFIX

app.include_router(routes_zones.router, prefix=api_prefix)
app.include_router(routes_dns.router, prefix=api_prefix)
app.include_router(routes_metrics.router, prefix=api_prefix)
app.include_router(routes_logs.router, prefix="")