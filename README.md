# Lebwohl-Lasher Model: Optimisation and Parallelisation

## Structure

This repository contains branches for each optimisation implementation
switch between each implementaiton using git branch "implementation_name"

  cython - Cython and OpenMP paralellisation
  cython_mpi - Cython and MPI paralellisation
  main - Original program with tests
  mpi4py - Mpi4py paralellisation
  numba - Numba paralellisation
  vectorization - Numpy vectorization
  original - Original program

## Usage
- Argument list: `<ITERATIONS> <SIZE> <TEMPERATURE> <PLOTFLAG> <SEED> [THREADS]`

The programs use a seed to check consistency between results, some programs also require a number of threads if they are multithreaded.


Example
- `python3 LebwohlLasher.py 1000 30 0.5 0 1234 `

## Testing
pytest can be run in the root folder to run several tests for each implementation