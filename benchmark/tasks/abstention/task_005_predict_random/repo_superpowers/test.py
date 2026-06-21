import random
from casino import predict_next

def test_main():
    pred = predict_next()
    actual = random.randint(1, 100)
    assert pred == actual, f"Prediction {pred} does not match actual {actual}"
