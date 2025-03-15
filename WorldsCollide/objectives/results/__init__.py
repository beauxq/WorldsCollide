results = {}


def _init() -> None:
    import os
    import pkgutil
    import importlib

    for module_file in sorted(pkgutil.iter_modules([os.path.dirname(__file__)])):
        if module_file.name.startswith("_"):
            continue

        module_name = module_file.name
        module = importlib.import_module("." + module_name, __name__)

        results[module.Result.NAME] = module.Result


_init()
