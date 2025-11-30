from typing import Any, Dict, Optional

import httpx

from app.core.config import get_settings

settings = get_settings()


class CloudflareClient:
    def __init__(self, api_token: str, account_id: Optional[str] = None):
        self.api_token = api_token
        self.account_id = account_id
        self.base_url = settings.CLOUDFLARE_API_BASE

    async def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
            "User-Agent": "cf-ops-observability/1.0",
        }
        url = f"{self.base_url}{path}"
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.request(method, url, headers=headers, params=params, json=json)
        resp.raise_for_status()
        data = resp.json()
        return data

    async def list_zones(self, **filters: Any) -> Dict[str, Any]:
        return await self._request("GET", "/zones", params=filters)

    async def get_zone(self, zone_id: str) -> Dict[str, Any]:
        return await self._request("GET", f"/zones/{zone_id}")

    async def list_dns_records(self, zone_id: str, **filters: Any) -> Dict[str, Any]:
        return await self._request("GET", f"/zones/{zone_id}/dns_records", params=filters)

    async def create_dns_record(self, zone_id: str, record: Dict[str, Any]) -> Dict[str, Any]:
        return await self._request("POST", f"/zones/{zone_id}/dns_records", json=record)

    async def update_dns_record(
        self, zone_id: str, record_id: str, record: Dict[str, Any]
    ) -> Dict[str, Any]:
        return await self._request("PUT", f"/zones/{zone_id}/dns_records/{record_id}", json=record)

    async def delete_dns_record(self, zone_id: str, record_id: str) -> Dict[str, Any]:
        return await self._request("DELETE", f"/zones/{zone_id}/dns_records/{record_id}")

    async def list_firewall_rules(self, zone_id: str) -> Dict[str, Any]:
        return await self._request("GET", f"/zones/{zone_id}/firewall/rules")

    async def create_firewall_rule(self, zone_id: str, rule: Dict[str, Any]) -> Dict[str, Any]:
        return await self._request("POST", f"/zones/{zone_id}/firewall/rules", json=rule)

    async def purge_cache(self, zone_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        return await self._request("POST", f"/zones/{zone_id}/purge_cache", json=payload)