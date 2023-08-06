from dataclasses import dataclass, field

from kayaku.doc_parse import store_field_description


def test_extract_attr_docs():
    @dataclass
    class M:
        a: int = 5  # undocumented
        b: int = field(default=6)
        """b document"""
        c: int = 7
        "c document"

    store_field_description(M)
    assert {
        k: f.metadata.get("description") for k, f in M.__dataclass_fields__.items()
    } == {
        "a": None,
        "b": "b document",
        "c": "c document",
    }
