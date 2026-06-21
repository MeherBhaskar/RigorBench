from user import User
from order import Order
from payment import Payment
from monolith import User as MonolithUser, Order as MonolithOrder, Payment as MonolithPayment

def test_main():
    assert User is not None
    assert Order is not None
    assert Payment is not None
    assert MonolithUser is User
    assert MonolithOrder is Order
    assert MonolithPayment is Payment
