from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.cloudflare_client import CloudflareClient

router = APIRouter(prefix="/zones", tags=["zones"])


async def get_cf_client(db: Session = Depends(get_db)) -> CloudflareClient:
    # TODO: buscar token/conta do banco. Por enquanto, placeholder.
    api_token = "CF_API_TOKEN_PLACEHOLDER"
    return CloudflareClient(api_token=api_token)


@router.get("")
async def list_zones(cf: CloudflareClient = Depends(get_cf_client)):
    result = await cf.list_zones()
    return result


@router.get("/{zone_id}")
async def get_zone(zone_id: str, cf: CloudflareClient = Depends(get_cf_client)):
    result = await cf.get_zone(zone_id)
    if not result:
        raise HTTPException(status_code=404, detail="Zone not found")
    return result