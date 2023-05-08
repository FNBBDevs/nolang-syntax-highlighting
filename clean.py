import os
import json

def clean():
    # Get current package.json
    with open('package.json', 'r', encoding='utf-8') as f:
        package = json.load(f)

    # Increase the version number
    previous, version = package['version'], package['version']
    version = [int(val) for val in version.split('.')]
    version[2] = version[2] + 1
    version = '.'.join([str(val) for val in version])
    package['version'] = version
    print(f'CLEAN: increasing version by one: {previous} -> {version}')

    # Update the package.json
    with open('package.json', 'w', encoding='utf-8') as f:
        json.dump(package, f)

    # Remove the vsix file that was created
    print(f'CLEAN: removing .vsix file for version {previous}')
    os.remove(f"nolang-{previous}.vsix")

if __name__ == "__main__":
    clean()
