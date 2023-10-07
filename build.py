import os
import json
import argparse
import bruhcolor
import subprocess

package_json = json.load(open("./package.json", "r", encoding="utf8"))

version = package_json.get("version")

parser = argparse.ArgumentParser()

parser.add_argument(
    "--mode",
    choices=["clean", "dev"],
    default="clean",
    help="way to build the extension"
)

args = parser.parse_args()

modes = {
    "clean": "package, publish, and clean",
    "dev": "package and install locally"
}

if args.mode:
    if args.mode == "clean":
        package = subprocess.Popen(["vsce", "package"], shell=True)
        package_out, package_err = package.communicate()

        publish = subprocess.Popen(["vsce", "publish"], shell=True)
        publish_out, publish_err = publish.communicate()

        clean = subprocess.Popen(["python", "clean.py"], shell=True)
        clean_out, clean_err = clean.communicate()
    else:
        package = subprocess.Popen(["vsce", "package"], shell=True)
        package_out, package_err = package.communicate()

        local_install = subprocess.Popen(["code", "--install-extension", f"nolang-{version}.vsix"], shell=True)
        local_install_out, local_install_err = local_install.communicate()
