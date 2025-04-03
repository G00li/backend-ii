
from fastapi import FastAPI
from .payments import PaymentService, PaymentGateway
from .factory import shape_factory
from .observe import Subject, ConcreteObserver

api= fastapi.FastAPI()

@api.get("/")
def index():
    return {"message": "Hello, World!"}


@api.post("/pay")
def process_payment(method: str):

    payment_service: PaymentService = PaymentGateway.build(method=method)
    return payment_service.process()


@api.get("/shapes/{shape_type}")
def get_shape(shape_type: str):
    shape = shape_factory(shape_type)
    return shape.draw()


@api.post("/observe")
def observe(state: str):
    subject = Subject()
    observer = ConcreteObserver("Observer 1")
    subject.add_observer(observer)
    subject.set_state(state)
