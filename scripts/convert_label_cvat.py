"""Convert a Day 3 classes.json file into the CVAT Raw-label format."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def rgb_to_hex(rgb: list[int]) -> str:
    """Convert an RGB list [R, G, B] to a hexadecimal color string."""
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def convert_to_cvat_raw(input_filename: Path, output_filename: Path) -> None:
    """Write the task's class names and colors in CVAT Raw-label JSON."""
    with input_filename.open(encoding="utf-8") as source:
        data = json.load(source)

    colors = data.get("colors", {})
    labels = [
        {
            "name": class_name,
            "color": rgb_to_hex(colors.get(class_name, [0, 0, 0])),
            "attributes": [],
            "type": "any",
        }
        for class_name in data.get("classes", [])
    ]

    with output_filename.open("w", encoding="utf-8") as destination:
        json.dump(labels, destination, indent=2)
        destination.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert a Day 3 classes.json file to CVAT Raw-label JSON."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default=Path("classes.json"),
        help="Input classes.json path (default: classes.json)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("cvat-labels.json"),
        help="Output CVAT Raw-label JSON path (default: cvat-labels.json)",
    )
    arguments = parser.parse_args()
    convert_to_cvat_raw(arguments.input, arguments.output)
    print(f"Wrote CVAT Raw labels to {arguments.output}")
