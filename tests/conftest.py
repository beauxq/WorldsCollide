from collections.abc import Generator
import pytest
import sys


@pytest.fixture(autouse=True)
def reload_modules() -> Generator[None, None, None]:
    original_modules = dict(sys.modules)
    yield
    # clean up the modules after each test
    for name in list(sys.modules):
        if name not in original_modules:
            del sys.modules[name]
    # restore the original modules
    sys.modules.update(original_modules)
