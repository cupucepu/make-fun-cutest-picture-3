"""Entry for make.fun cutest-picture-01: "Otter Hug".

Copies the vendored picture.jpg to /output/entry.png and verifies the
copy byte for byte, so the graded file is exactly the picture shipped
in this repository.
"""

import os
import struct
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "picture.jpg")


def jpeg_dimensions(data: bytes) -> tuple[int, int]:
    """Read width and height from a JPEG header (stdlib only).

    Walks the JPEG segments: checks the SOI marker, skips padding and
    standalone markers, and reads the dimensions from the first SOF
    segment (SOF0/SOF1/SOF2).
    """
    if data[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG (missing SOI marker)")
    pos = 2
    while pos < len(data) - 1:
        if data[pos] != 0xFF:
            raise ValueError("bad JPEG marker")
        marker = data[pos + 1]
        while marker == 0xFF:  # padding
            pos += 1
            marker = data[pos + 1]
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        size = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(">HH", data[pos + 5:pos + 9])
            return width, height
        pos += 2 + size
    raise ValueError("no SOF segment found")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)

    with open(SRC, "rb") as f:
        data = f.read()
    with open(out, "wb") as f:
        f.write(data)

    with open(out, "rb") as f:
        back = f.read()
    if back != data:
        print("error: /output/entry.png differs from picture.jpg", file=sys.stderr)
        sys.exit(1)

    width, height = jpeg_dimensions(back)
    if (width, height) != (1024, 1024):
        print(f"error: unexpected JPEG dimensions {width}x{height}", file=sys.stderr)
        sys.exit(1)

    print("ok: /output/entry.png is a byte-identical 1024x1024 copy of picture.jpg")


if __name__ == "__main__":
    main()
