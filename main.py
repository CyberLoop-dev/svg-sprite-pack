#!/usr/bin/env python3
"""Pack separate SVG icons into a single <symbol> sprite."""
import argparse
import re
import xml.etree.ElementTree as ET
from pathlib import Path

SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)

def safe_id(name):
    value = re.sub(r"[^a-zA-Z0-9_-]+", "-", Path(name).stem).strip("-").lower()
    if not value or value[0].isdigit():
        value = "icon-" + value
    return value

def pack_svgs(paths):
    root = ET.Element(f"{{{SVG_NS}}}svg", {"style": "display:none"})
    used = set()
    for path in paths:
        source = ET.parse(path).getroot()
        if source.tag.split("}")[-1] != "svg":
            raise ValueError(f"{path}: root element is not svg")
        view_box = source.get("viewBox")
        if not view_box:
            width, height = source.get("width"), source.get("height")
            if not width or not height:
                raise ValueError(f"{path}: missing viewBox and width/height")
            view_box = f"0 0 {width.rstrip('px')} {height.rstrip('px')}"
        ident = safe_id(path.name)
        if ident in used:
            raise ValueError(f"Duplicate icon id: {ident}")
        used.add(ident)
        symbol = ET.SubElement(root, f"{{{SVG_NS}}}symbol", {"id": ident, "viewBox": view_box})
        for child in list(source):
            symbol.append(child)
    return ET.tostring(root, encoding="unicode", xml_declaration=True)

def main():
    parser = argparse.ArgumentParser(description="Pack SVG files into a symbol sprite.")
    parser.add_argument("directory", type=Path)
    parser.add_argument("--output", type=Path, default=Path("icons.svg"))
    args = parser.parse_args()
    paths = sorted(args.directory.glob("*.svg"))
    if not paths:
        parser.error("No .svg files found in the directory.")
    try:
        result = pack_svgs(paths)
    except (OSError, ET.ParseError, ValueError) as exc:
        parser.error(str(exc))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result, encoding="utf-8")
    print(f"Packed {len(paths)} icons into {args.output}")
if __name__ == "__main__":
    main()
