import nbformat
from tqdm import tqdm

with open('regression.ipynb', encoding='utf-8') as f:
    nb1 = nbformat.read(f, as_version=4)

cells_to_extract = nb1.cells[9:]

for i in tqdm(range(4)):

    nb1['cells'].extend(cells_to_extract)

with open('regression.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb1, f)
