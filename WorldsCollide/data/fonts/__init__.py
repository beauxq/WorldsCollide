def __init__():
    from ...data.fonts.widths import Widths
    widths = Widths()

    import sys
    import inspect
    module = sys.modules[__name__]
    module.widths = widths
__init__()
