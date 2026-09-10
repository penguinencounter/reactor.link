if __name__ != "__main__":
    raise ImportError("not a module")

from collections import defaultdict
from json import load
from pathlib import Path
import shutil
from rich import print
from jinja2 import Environment, FileSystemLoader, select_autoescape

with open("data.json", encoding="utf-8") as f:
    data = load(f)

data = {k: v for k, v in data.items() if not k.startswith("*")}

j2env = Environment(
    loader=FileSystemLoader("templates"), autoescape=select_autoescape()
)

output = Path("./dist")
if output.exists():
    shutil.rmtree(output, ignore_errors=True)
output.mkdir(exist_ok=True)

root_tm = j2env.get_template("root.html.jinja2")
leaf_tm = j2env.get_template("leaf.html.jinja2")


def write_root():
    with open(output / "index.html", "w", encoding="utf-8") as f:
        f.write(root_tm.render(routes=data))


def write_leaf(route, target):
    dir = output / route
    dir.mkdir(parents=True, exist_ok=True)
    file = dir / "index.html"
    with open(file, "w", encoding="utf-8") as f:
        f.write(leaf_tm.render(link=target))


write_root()

hist = defaultdict(list)

for k, v in data.items():
    hist[v].append(k)
    write_leaf(k, v)

for url, names in hist.items():
    if len(names) <= 1:
        continue
    print(f"[yellow][bold]{len(names)} aliases[/] for {url}: {names}")
