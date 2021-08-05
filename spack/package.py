# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class VolAsync(CMakePackage):
    """An asynchronous I/O framework that provides support for all I/O operations
       and manages data dependencies transparently and automatically."""

    homepage = "https://hdf5-vol-async.readthedocs.io/en/latest/"
    git      = "https://github.com/kencasimiro/vol-async"
    #url      = "https://github.com/kencasimiro/vol-async/archive/refs/tags/0.5.tar.gz"

    maintainers = ['houjun', 'sbyna', 'jeanbez']

    version('develop', branch='develop')

    depends_on('argobots@main')
    depends_on('hdf5@develop-1.13+mpi+threadsafe')



    def cmake_args(self):
        """Populate cmake arguments for HDF5 VOL."""
        spec = self.spec

        args = [
            '-DBUILD_SHARED_LIBS:BOOL=ON',
            '-DBUILD_TESTING:BOOL=ON',
        ]
        return args

    @run_after('install')
    #@on_package_attributes(run_tests=True)


    def check_build(self):
        """Run ctest after building project."""
        with working_dir("test"):
            ctest(parallel=False)