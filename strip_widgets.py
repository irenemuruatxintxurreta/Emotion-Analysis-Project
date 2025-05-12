import nbformat
from glob import glob

for path in glob("notebooks/*.ipynb"):
    nb = nbformat.read(path, as_version=4)
    if "widgets" in nb.metadata:
        del nb.metadata["widgets"]
    for cell in nb.cells:
        if "widgets" in cell.metadata:
            del cell.metadata["widgets"]
    nbformat.write(nb, path)
    print(f"Cleaned {path}")
