#!/usr/bin/env python3
"""Compose the README "Tech Stack" rows from the tiles in assets/icons/.

Each row is written to assets/skills/<row>.svg with the same geometry that
skillicons.dev uses (256px tiles, 44px gap, rendered 48px high), so the rows
look exactly like the old skillicons.dev images but are served from this repo.

Usage: python3 scripts/build-skill-rows.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
ICONS = ROOT / "assets" / "icons"
OUT = ROOT / "assets" / "skills"

ROWS = {
    "mobile": ["swift", "xcode", "kotlin", "androidstudio", "flutter"],
    "backend": ["java", "spring", "hibernate", "gradle", "go", "nodejs", "python", "ruby", "php", "laravel"],
    "frontend": ["js", "ts", "jquery", "figma"],
    "data": ["mysql", "mongodb", "sqlite", "redis", "rabbitmq"],
    "cloud": ["firebase", "googlecloud", "cloudflare", "docker", "kubernetes", "jenkins", "grafana"],
    "tools": ["idea", "postman", "regex", "arduino"],
}

TILE, GAP, HEIGHT = 256, 44, 48


def scoped(svg: str, prefix: str) -> str:
    """Prefix every id in a tile so tiles can't clash once they share one document."""
    ids = set(re.findall(r'\bid="([^"]+)"', svg))
    for i in sorted(ids, key=len, reverse=True):
        new = f"{prefix}-{i}"
        svg = svg.replace(f'id="{i}"', f'id="{new}"')
        svg = svg.replace(f"url(#{i})", f"url(#{new})")
        svg = svg.replace(f'href="#{i}"', f'href="#{new}"')
    return svg


def build(name: str, icons: list[str]) -> str:
    width = len(icons) * (TILE + GAP) - GAP
    parts = [
        f'<svg width="{width * HEIGHT / TILE:g}" height="{HEIGHT}" viewBox="0 0 {width} {TILE}" fill="none" '
        'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">'
    ]
    for i, icon in enumerate(icons):
        tile = (ICONS / f"{icon}.svg").read_text().strip()
        parts.append(f'<g transform="translate({i * (TILE + GAP)}, 0)">{scoped(tile, icon)}</g>')
    parts.append("</svg>\n")
    return "\n".join(parts)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, icons in ROWS.items():
        (OUT / f"{name}.svg").write_text(build(name, icons))
        print(f"assets/skills/{name}.svg  ({len(icons)} icons)")


if __name__ == "__main__":
    main()
