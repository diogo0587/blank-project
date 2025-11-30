import json
from typing import Any, Dict, List

from clickhouse_driver import Client

from app.core.config import get_settings

settings = get_settings()
ch_client = Client.from_url(settings.CLICKHOUSE_DSN)


def parse_ndjson(body: bytes) -> List[Dict[str, Any]]:
    lines = body.splitlines()
    events: List[Dict[str, Any]] = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        events.append(json.loads(line))
    return events


def insert_http_logs(events: List[Dict[str, Any]]) -> None:
    if not events:
        return
    rows = []
    for ev in events:
        rows.append(
            [
                ev.get("EdgeStartTimestamp"),
                ev.get("AccountID", ""),
                ev.get("ZoneID", ""),
                ev.get("ZoneName", ""),
                ev.get("ClientIP", ""),
                ev.get("ClientCountry", ""),
                ev.get("ClientASN", 0),
                ev.get("ClientRequestHost", ""),
                ev.get("ClientRequestURI", ""),
                ev.get("ClientRequestMethod", ""),
                ev.get("EdgeResponseStatus", 0),
                ev.get("OriginResponseStatus", 0),
                ev.get("CacheStatus", ""),
                ev.get("BytesSent", 0),
                ev.get("BytesReceived", 0),
                ev.get("RayID", ""),
                ev.get("ClientSSLProtocol", ""),
                ev.get("ClientSSLCipher", ""),
                ev.get("WAFAction", ""),
                ev.get("UserAgent", ""),
            ]
        )
    ch_client.execute(
        """
        INSERT INTO logs_http (
          timestamp,
          account_id,
          zone_id,
          zone_name,
          client_ip,
          client_country,
          client_asn,
          http_host,
          http_path,
          http_method,
          http_status,
          origin_status,
          cache_status,
          bytes_sent,
          bytes_received,
          request_id,
          tls_protocol,
          tls_cipher,
          firewall_action,
          user_agent
        ) VALUES
        """,
        rows,
    )