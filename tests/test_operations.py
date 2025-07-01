from app.operations import AddOperation

def test_add():
    op = AddOperation()
    assert op.execute(2, 3) == 5
