import nbformat

with open("test_prepross_tally.ipynb", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)
    cells_to_extract = nb.cells[87:]
    with open("regression.ipynb", "w", encoding="utf-8") as f:
        nbformat.write(
            nbformat.NotebookNode(cells=cells_to_extract),
            f
        )
