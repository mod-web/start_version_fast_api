import uuid
from fastapi import APIRouter, Depends


router = APIRouter()


@router.post(
    '/',
    description='New order creation',
    summary='New order creation',
)
async def new_order(
    # broker: RabbitmqBroker = Depends(get_broker),
) -> str:
    payment_id = str(uuid.uuid4())
    return payment_id
