import io
import os
from typing import Union

from typing.io import BinaryIO

from .compression import CompressionFactory


class ToVariableWriter:
    def __init__(self):
        self._data_bytes = []

    @property
    def data_bytes(self):
        return b"".join(self._data_bytes)

    @property
    def data_str(self):
        return self.data_bytes.decode("utf-8")

    def write(self, d: bytes):
        self._data_bytes.append(d)


def save_object(
    obj: Union[bytes, BinaryIO],
    file_name: str,
    path: str,
    compression: CompressionFactory = CompressionFactory.NONE,
) -> str:
    compression = compression.value()
    if isinstance(obj, bytes):
        obj = io.BytesIO(obj)
    file_name = f"{file_name}{compression.extension}"
    save_path = os.path.join(path, file_name)
    with open(save_path, "wb") as out_file:
        compression.compress(read_stream=obj, write_stream=out_file)
    return save_path


def load_object(path, as_bytes=True) -> Union[str, bytes]:
    compression_extension = path.split(".")[-1]
    compression = CompressionFactory[compression_extension].value()
    to_var = ToVariableWriter()
    with open(path, "rb") as in_file:
        compression.decompress(read_stream=in_file, write_stream=to_var)
        in_file.close()
    if as_bytes:
        return to_var.data_bytes
    return to_var.data_str
