from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# the c++ extension module (needs to be linked in with dbg.o ...)
extension_mod = Extension("_dbg",
                          sources=["_dbgmodule.pyx"],
                          extra_compile_args=['-g'],
                          language="c++",
                          include_dirs=['../lib',],
                          library_dirs=['../lib',],
                          extra_objects=['../lib/dbgraph.o',
                                         '../lib/2d.o'],
                          depends=['../lib/dbg.hh',
                                   '../lib/2d.hh',
                                   '../lib/dbgraph.hh',]
                          )

# python modules: only 'dbg'
py_mod = 'dbg'

setup(name = "dbg", version = "0.1",
      description = 'de Bruijn graph library',
      author = 'Jason Pell',
      author_email = 'pelljaso@msu.edu',
      license='New BSD License',
      packages = [py_mod,],
      ext_modules = [extension_mod,],
      cmdclass = {'build_ext': build_ext},
)
