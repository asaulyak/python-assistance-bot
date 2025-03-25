import pickle
from execution_context import ExecutionContext


def save_data(context: ExecutionContext, filename="data.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(context, file)


def load_data(filename="data.pkl") -> ExecutionContext:
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return ExecutionContext()
