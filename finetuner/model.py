from _finetuner.runner.stubs import model
from _finetuner.runner.stubs.model import *  # noqa F401
from _finetuner.runner.stubs.model import _EmbeddingModelStub


def get_header() -> Tuple[str, ...]:
    """Get table header."""
    return 'name', 'task', 'output_dim', 'architecture', 'description'


def get_row(model_stub) -> Tuple[str, ...]:
    """Get table row."""
    return (
        model_stub.display_name,
        model_stub.task,
        str(model_stub.output_shape[1]),
        model_stub.architecture,
        model_stub.description,
    )


def list_model_classes() -> Dict[str, ModelStubType]:
    rv = {}
    members = inspect.getmembers(model, inspect.isclass)
    parent_class = _EmbeddingModelStub
    for name, stub in members:
        if (
            name != 'MLPStub'
            and not name.startswith('_')
            and type(stub) != type
            and issubclass(stub, parent_class)
        ):
            rv[name] = stub
    return rv
