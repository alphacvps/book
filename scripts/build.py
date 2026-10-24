from pathlib import Path
import argparse
import subprocess
import sys

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "book.yml"

FORMATS = {
    "pdf": ("print", ".pdf"),
    "epub": ("ebook", ".epub"),
    "html": ("web", ".html"),
    "docx": ("docx", ".docx"),
}


def load_yaml(path):
    with path.open(encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def build(fmt, profile_override=None):
    config = load_yaml(CONFIG)
    metadata = config["metadata"]
    output_dir = ROOT / config["project"]["output_dir"]

    profile_name, extension = FORMATS[fmt]
    profile_name = profile_override or profile_name
    profile = ROOT / "profiles" / f"{profile_name}.yaml"

    if not profile.is_file():
        raise FileNotFoundError(f"Profilo non trovato: {profile}")

    # L'ordine dei capitoli è esplicito nel progetto.
    chapters = sorted(
        (ROOT / config["project"]["source"]).glob("*.md")
    )
    if not chapters:
        raise RuntimeError("Nessun capitolo Markdown trovato.")

    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"book{extension}"

    command = [
        "pandoc",
        "--defaults", str(profile),
        "--metadata-file", str(ROOT / metadata),
        *map(str, chapters),
        "--output", str(output),
    ]

    print("Eseguo:", " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)
    print(f"Creato: {output}")


def main():
    parser = argparse.ArgumentParser(
        description="Compila il libro con Pandoc."
    )
    parser.add_argument(
        "--format",
        choices=[*FORMATS, "all"],
        required=True,
    )
    parser.add_argument("--profile")
    args = parser.parse_args()

    formats = list(FORMATS) if args.format == "all" else [args.format]

    try:
        for fmt in formats:
            build(fmt, args.profile)
    except (OSError, RuntimeError, KeyError, subprocess.CalledProcessError) as exc:
        print(f"Errore di compilazione: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
