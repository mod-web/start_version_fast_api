import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from config import settings
from src.api.v1 import orders, payments, refunds, subscriptions
# from src.services import utils

app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


app.include_router(orders.router, prefix='/api/v1/orders', tags=['Orders'])
app.include_router(payments.router, prefix='/api/v1/payments', tags=['Payments'])
app.include_router(refunds.router, prefix='/api/v1/refunds', tags=['Refunds'])
app.include_router(subscriptions.router, prefix='/api/v1/subscriptions', tags=['Subscriptions'])


@app.get('/')
async def status():
    return {'status': 'OK'}


# @app.on_event('startup')
# async def startup():
#     # url = f'amqp://{settings.broker.login}:{settings.broker.password}@{settings.broker.host}/'
#     # utils.rabbitmq_connection = await aio_pika.connect(url=url)
#     # utils.broker = await RabbitmqBroker().configure()
#
#
# @app.on_event('shutdown')
# async def shutdown():
#     await utils.rabbitmq_connection.close()


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
    )
