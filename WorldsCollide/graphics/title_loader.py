import pkgutil


def get_title_data() -> bytes:
    data = pkgutil.get_data(__name__, "title/WC Spartan Title Data-CDude.bin")
    assert data, f"no title data {__name__=}"
    return data
