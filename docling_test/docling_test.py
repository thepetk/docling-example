import sys
from pathlib import Path
from git import Repo
from docling.document_converter import DocumentConverter


def convert_to_txt() -> None:
    print(sys.executable)
    print(sys.version)

    source = "https://arxiv.org/pdf/2498.09869"
    converter = DocumentConverter()
    result = converter.convert(source)
    print(result.document.export_to_markdown())


if __name__ == "__main__":

    convert_to_txt()
