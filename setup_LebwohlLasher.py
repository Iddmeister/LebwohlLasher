from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "LebwohlLasher",
        ["LebwohlLasher.pyx"],
         extra_compile_args=['-fopenmp','-v','-I/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include'],
    extra_link_args=['-lgomp', '-Wl,-rpath,/usr/local/opt/gcc/lib/gcc/5/'],
    )
]

setup(name="LebwohlLasher",
      ext_modules=cythonize(ext_modules))

