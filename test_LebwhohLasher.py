
from LebwohlLasher import *
import pytest
import expected_test_results as expected

@pytest.mark.parametrize("size, seed, expect", [
    (10, 0, expected.init_data_size_10_seed_0),
    (10, 56, expected.init_data_size_10_seed_56),
    (1, 100, expected.init_data_size_1_seed_100),
    (7, 0, expected.init_data_size_7_seed_0),
])

def test_initdat(size, seed, expect):

    np.random.seed(seed)

    arr = initdat(size)

    assert np.array_equal(arr.shape, expect.shape)
    #Compare Arrays within a tolerance of 1e-10
    assert np.allclose(arr, expect, 1e-10)

@pytest.mark.parametrize("lattice, ix, iy, nmax, expect", [
    (expected.init_data_size_10_seed_56, 0, 0, 10, -1.4875965848430321),
    (expected.init_data_size_10_seed_56, 4, 5, 10, -3.5331651246635865),
    (expected.init_data_size_10_seed_56, 0, 9, 10, -2.6255787210330035),
    (expected.init_data_size_7_seed_0, 6, 6, 7, -0.6029266302470666),
    
])

def test_one_energy(lattice, ix, iy, nmax, expect):

    assert one_energy(lattice, ix, iy, nmax) == expect


@pytest.mark.parametrize("lattice, nmax, expect", [
    (expected.init_data_size_10_seed_56, 10, -98.36698204484836),
    (expected.init_data_size_10_seed_0, 10, -128.29884226224496),
    (expected.init_data_size_7_seed_0, 7, -50.73994466257066),
    
])

def test_all_energy(lattice, nmax, expect):

    assert all_energy(lattice, nmax) == expect


@pytest.mark.parametrize("lattice, nmax, expect", [
    (expected.init_data_size_10_seed_56, 10, 0.28023363225683656),
    (expected.init_data_size_10_seed_0, 10, 0.3690539325939002),
    (expected.init_data_size_7_seed_0, 7, 0.36083921010274533),
    
])

def test_get_order(lattice, nmax, expect):

    assert get_order(lattice, nmax) == expect


@pytest.mark.parametrize("lattice, Ts, nmax, seed, expect", [
    (expected.init_data_size_10_seed_56, 1.0, 10, 0, 0.67),
    (expected.init_data_size_10_seed_0, 1.0, 10, 111, 0.67),
    (expected.init_data_size_7_seed_0, 1.0, 7, 0, 0.7142857142857143),
    (expected.init_data_size_10_seed_56, 2.0, 10, 0, 0.74),
    (expected.init_data_size_10_seed_0, 1.9999, 10, 0, 0.69),
    (expected.init_data_size_7_seed_0, 0.0000001, 7, 0, 0.3673469387755102),
    
])


def test_MC_step(lattice, Ts, nmax, seed, expect):

    np.random.seed(seed)

    assert MC_step(lattice, Ts, nmax) == expect

@pytest.mark.parametrize("lattice, nsteps, Ts, runtime, ratio, energy, order, nmax, expect_filepath", [
    (expected.init_data_size_10_seed_56, 100, 1.0, 0.256650, expected.savedat_steps_100_size_10_ratio, expected.savedat_steps_100_size_10_energy, expected.savedat_steps_100_size_10_order, 10, "expected_test_output_1.txt"),
])


def test_savedat(lattice, nsteps, Ts, runtime, ratio, energy, order, nmax, expect_filepath):

    savedat(lattice, nsteps, Ts, runtime, ratio, energy, order, nmax, "test_output.txt")

    with open("output/test_output.txt") as test_f:

        with open(expect_filepath) as expected_f:


            test_lines = test_f.readlines()
            expected_lines = expected_f.readlines()


            for i, test_line in enumerate(test_lines):
                #Skip line containing date
                if i == 1:
                    continue

                assert test_line == expected_lines[i]

      

@pytest.mark.parametrize("nsteps, nmax, temp, seed, expect_filepath", [
    (100, 10, 1.0, 0, "expected_test_output_2.txt"),
])


def test_main(nsteps, nmax, temp, seed, expect_filepath):

    np.random.seed(seed)

    main("test", nsteps, nmax, temp, 0, _filename="test_output.txt")
      
    with open("output/test_output.txt") as test_f:

        with open(expect_filepath) as expected_f:


            test_lines = test_f.readlines()
            expected_lines = expected_f.readlines()


            for i, test_line in enumerate(test_lines):
                #Skip line containing date
                if i == 1:
                    continue

                #Skip line containing run time
                if i == 5:
                    continue

                assert test_line == expected_lines[i]

def test_MPI_initialized():
    assert MPI.Is_initialized()
