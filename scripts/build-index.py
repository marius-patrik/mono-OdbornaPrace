"""Builds the super-repository's documentation site.

The submodules each publish their own site; this one exists to point at them, so it is an index
rather than a rebuild. Rebuilding them here would typeset the same thesis twice and publish two
copies that could disagree.
"""

import html
import os
import re
from typing import List, Tuple

#: Submodule path -> (title, description), in the order they should be listed.
ENTRIES: List[Tuple[str, str, str]] = [
    ("prace", "Odborná práce", "Vlastní text práce, sázený v Typstu"),
    ("template", "Šablona", "Šablona pro odbornou práci na GJKT"),
    ("darkfactory", "DarkFactory", "Praktická část — autonomní vývojový systém"),
]

#: Submodule path -> the release asset that repository publishes, if any.
#:
#: The thesis is a PDF, and a page about a thesis that does not show the thesis is a page about
#: nothing. `releases/latest/download/` always resolves to the newest release, so the link needs no
#: version in it and nothing here has to be bumped when one is cut.
ASSETS = {"prace": "prace.pdf"}

#: Submodule path -> the repository it points at, read from `.gitmodules`.
REPO_PATTERN = re.compile(
    r'\[submodule "(?P<name>[^"]+)"\][^\[]*?url\s*=\s*\S*?/(?P<repo>[^/\s]+?)(?:\.git)?\s*$',
    re.M | re.S,
)


def repositories(root: str = ".") -> dict:
    """Reads each submodule's repository name from `.gitmodules`.

    Args:
        root: Repository root.

    Returns:
        Mapping of submodule name to repository name.
    """
    path = os.path.join(root, ".gitmodules")
    if not os.path.isfile(path):
        return {}
    with open(path, encoding="utf-8") as handle:
        return {
            m.group("name"): m.group("repo")
            for m in REPO_PATTERN.finditer(handle.read())
        }


def build(root: str = ".", out: str = "site") -> str:
    """Writes the index page.

    Args:
        root: Repository root.
        out: Directory to write into.

    Returns:
        Path of the written file.
    """
    repos = repositories(root)
    owner = os.environ.get(
        "GITHUB_REPOSITORY", "marius-patrik/mono-OdbornaPrace"
    ).split("/")[0]
    cards = []
    embed = ""
    for name, title, description in ENTRIES:
        repo = repos.get(name, name)
        asset = ASSETS.get(name)
        pdf = (
            f"https://github.com/{html.escape(owner)}/{html.escape(repo)}"
            f"/releases/latest/download/{html.escape(asset)}"
            if asset
            else ""
        )
        cards.append(
            f'<li><a href="https://{owner}.github.io/{html.escape(repo)}/">'
            f"<strong>{html.escape(title)}</strong></a> — {html.escape(description)}<br>"
            f'<a href="https://github.com/{html.escape(owner)}/{html.escape(repo)}">'
            f"github.com/{html.escape(owner)}/{html.escape(repo)}</a>"
            + (f' · <a href="{pdf}">PDF</a>' if pdf else "")
            + "</li>"
        )
        if pdf and not embed:
            # Shown rather than only linked, and below the work it belongs to. `<object>` falls
            # back to its own contents where a browser will not render a PDF inline, which is most
            # phones - so the link inside it is the answer there, not a blank frame.
            embed = (
                f'<h2>Text práce</h2>\n<object data="{pdf}" type="application/pdf" '
                'class="pdf" title="Odborná práce (PDF)">'
                f'<p>Prohlížeč nezobrazuje PDF přímo — <a href="{pdf}">stáhnout PDF</a>.</p>'
                "</object>\n"
                f'<p class="fallback"><a href="{pdf}">Stáhnout PDF</a></p>\n'
            )
    os.makedirs(out, exist_ok=True)
    target = os.path.join(out, "index.html")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(
            "<!doctype html>\n<meta charset=utf-8>\n"
            "<meta name=viewport content='width=device-width,initial-scale=1'>\n"
            "<title>Odborná práce — GJKT</title>\n"
            "<style>body{font:16px/1.6 system-ui,sans-serif;max-width:44rem;margin:3rem auto;"
            "padding:0 1rem}li{margin:1rem 0}a{color:#0b4f9e}"
            "h2{margin-top:3rem;font-size:1.1rem}"
            ".pdf{width:100%;height:min(80vh,900px);border:1px solid #d5d9e0;border-radius:4px}"
            ".fallback{margin-top:.75rem;font-size:.9rem}"
            "@media(prefers-color-scheme:dark){body{background:#12151a;color:#e6e8ec}"
            "a{color:#7fb2f0}.pdf{border-color:#2b3038}}</style>\n"
            "<h1>Odborná práce</h1>\n"
            "<p>Text práce, šablona, ze které vznikla, a software, který je její praktickou "
            "částí.</p>\n"
            f"<ul>\n{chr(10).join(cards)}\n</ul>\n"
            f"{embed}"
        )
    return target


if __name__ == "__main__":
    print(build(os.environ.get("GITHUB_WORKSPACE", ".")))
