from fastapi import APIRouter, Query

from app.services.metrics_engine import get_overview_metrics

router = APIRouter(prefix="/metrics", tags=["metrics"])


@router.get("/overview")
def metrics_overview(
    zone_id: str | None = Query(default=None),
    minutes: int = Query(default=60, ge=1, le=1440),
):
    return get_overview_metrics(zone_id=zone_id, minutes=minutes)