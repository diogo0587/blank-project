from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.cloudflare_client import CloudflareClient

router = APIRouter(prefix="/zones/{zone_id}/dns-records", tags=["dns"])


class DNSRecordCreate(BaseModel):
    type: str
    name: str
    content: str
    ttl: int = 120
    proxied: bool = False


async def get_cf_client(db: Session = Depends(get_db)) -> CloudflareClient:
    # TODO: buscar token/conta do banco. Por enquanto, placeholder.
    api_token = "CF_API_TOKEN_PLACEHOLDER"
    return CloudflareClient(api_token=api_token)


@router.get("")
async def list_dns_records(zone_id: str, cf: CloudflareClient = Depends(get_cf_client)):
    return await cf.list_dns_records(zone_id)


@router.post("")
async def create_dns_record(
    zone_id: str, record: DNSRecordCreate, cf: CloudflareClient = Depends(get_cf_client)
):
    return await cf.create_dns_record(zone_id, record.dict())