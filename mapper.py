if __name__ != "__main__":
    raise ImportError("not a module")

from rich import print
from rich.prompt import Prompt

print()
print("[green]mapper: utility to help with bulk importing of gdrive links[/]")
print("[yellow]hold CTRL and manually select files in order to avoid mixing up links[/]")
print()

first_row = Prompt.ask("Enter aliases (separate by spaces)")
second_row = Prompt.ask("Enter GDrive links (select many, then paste)")

aliases = [x.strip() for x in first_row.split(" ") if x.strip()]
links = [x.strip() for x in second_row.split(",")]

if len(aliases) != len(links):
    print(f"[red]mismatched inputs: {len(aliases)} aliases, but {len(links)} links[/]")

print()
for k, v in zip(aliases, links):
    print(f'"{k}": "{v}",')
print()
