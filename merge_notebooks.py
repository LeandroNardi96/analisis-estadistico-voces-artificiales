import nbformat
from tqdm import tqdm

for i in tqdm(range(3)):

    with open('regression.ipynb', encoding='utf-8') as f:
        nb1 = nbformat.read(f, as_version=4)

    cells_to_extract = nb1.cells[33:]

    nb1['cells'].extend(cells_to_extract)

    with open('regression_v1.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb1, f)
