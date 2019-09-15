# pydimacs

Python module to manipulate CNF DIMACS formulas (using z3).

**This an experimental utility module**. If you are looking to solve
CNF formula using SAT solvers I recommend giving a look at: https://github.com/pysathq/pysat


# Installation

The main dependency of `pydimacs` is the Z3 python bindings. They are unfortunately
not provided via pip. They can be installed by installing z3 from Github: https://github.com/Z3Prover/z3#python.

Then the installation is then straightforward:

```bash
python3 setup.py install
```

# Usage

## Command line

A very simple utility all generating DIMACS from SMT2 and also JSON
graph from DIMACS. The file type detection is based on file extensions.
Thus make sure it match the file format. The command can be used as follows:

```bash
# convert SMT2 to DIMACS
pydimacs my_formula.smt2 output.cnf

# Generate the graph (and layout) from a CNF formula
pydimacs formula.cnf -x --dim 3 --iter 12 output.json
```

## Python API

```python
from pydimacs import CNFFormula

f = CNFFormula.from_dimacs_file("myformula.cnf")

print(f.clauses_num, f.variables_num)

for clause in f.clauses:
    # doing someting

f.to_graph_file("formula.json")
```
