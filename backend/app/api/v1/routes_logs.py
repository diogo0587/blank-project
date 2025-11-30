from fastapi import APIRouter, Header, HTTPException, Request

from app.core.config import get_settings
from app.services.logs_ingest import insert_http_logs, parse_ndjson

router = APIRouter(tags=["logs"])
settings = get_settings()


@router.post("/ingest/logpush/http")
async def ingest_logpush_http(request: Request, authorization: str = Header(None)):
    if authorization != f"Bearer {settings.LOGPUSH_SHARED_SECRET}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    body = await request.body()
    events = parse_ndjson(body)
    insert_http_logs(events)
    return {"ingested": len(events)}