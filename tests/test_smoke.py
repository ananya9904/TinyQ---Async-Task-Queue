import tinyq


def test_version():
    assert tinyq.__version__ == "0.1.0"

# Pytest automatically discovers functions whose names start with test_.
# assert : Checks whether a condition is true.
# To run the test : run pytest in terminal