import argparse, os
from rich.console import Console
from os import path, getenv
from dotenv import load_dotenv

load_dotenv()
c = Console()

# Argparser
parser = argparse.ArgumentParser()
parser.add_argument(
    "project_name",
    help="Your project's name",
    type=str,
    metavar="name",
)  # nargs="?",)

args = parser.parse_args()


# Get paths
base = getenv("BASE_DIR")
random_scripts = path.join(base, getenv("SCRIPTS_NAME"))
scripts = path.join(base, getenv("PYTHON_SCRIPTS"))


# Get all matches
for possibility in [base, random_scripts, scripts]:
    route = path.join(possibility, args.project_name)
    if path.exists(route):
        os.system(f"explorer {route}")
        os.system(f"code {route}")
        os.system(f"wt -d {route}")
