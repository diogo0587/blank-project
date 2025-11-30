from datetime import datetime, timedelta
from typing import Any, Dict, Optional

from clickhouse_driver import Client

from app.core.config import get_settings

settings = get_settings()
ch_client = Client.from_url(settings.CLICKHOUSE_DSN)


def get_overview_metrics(zone_id: Optional[str] = None, minutes: int = 60) -> Dict[str, Any]:
    to_ts = datetime.utcnow()
    from_ts = to_ts - timedelta(minutes=minutes)

    filters = "timestamp BETWEEN %(from_ts)s AND %(to_ts)s"
    params: Dict[str, Any] = {"from_ts": from_ts, "to_ts": to_ts}
    if zone_id:
        filters += " AND zone_id = %(zone_id)s"
        params["zone_id"] = zone_id

    q_total = f"""
    SELECT count() AS total
    FROM logs_http
    WHERE {filters}
    """

    q_errors = f"""
    SELECT
      sum(http_status >= 400 AND http_status < 500) AS errors_4xx,
      sum(http_status >= 500 AND http_status < 600) AS errors_5xx
    FROM logs_http
    WHERE {filters}
    """

    total = ch_client.execute(q_total, params)[0][0]
    errors_4xx, errors_5xx = ch_client.execute(q_errors, params)[0]

    return {
        "window_minutes": minutes,
        "total_requests": total,
        "errors_4xx": errors_4xx,
        "errors_5xx": errors_5xx,
        "error_4xx_rate": float(errors_4xx) / float(total) if total else 0.0,
        "error_5xx_rate": float(errors_5xx) / float(total) if total else 0.0,
    }