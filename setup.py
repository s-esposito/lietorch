from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import os
import os.path as osp

ROOT = osp.dirname(osp.abspath(__file__))

CUDA_HOME = os.environ.get("CUDA_HOME", None)
if CUDA_HOME is None:
    raise ValueError("Please set CUDA_HOME environment variable to the path of your CUDA installation")

setup(
    name='lietorch',
    version='0.2',
    description='Lie Groups for PyTorch',
    author='teedrz',
    packages=['lietorch'],
    ext_modules=[
        CUDAExtension('lietorch_backends', 
            include_dirs=[
                osp.join(ROOT, 'lietorch/include'), 
                osp.join(ROOT, 'eigen'),
                f"{CUDA_HOME}/include"
            ],
            library_dirs=[f"{CUDA_HOME}/lib"],
            libraries=['cudart'],
            sources=[
                'lietorch/src/lietorch.cpp', 
                'lietorch/src/lietorch_gpu.cu',
                'lietorch/src/lietorch_cpu.cpp'
            ],
            extra_compile_args={
                'cxx': ['-O2'], 
                'nvcc': [
                    '-O2',
                    '-gencode=arch=compute_60,code=sm_60',
                    '-gencode=arch=compute_61,code=sm_61',
                    '-gencode=arch=compute_70,code=sm_70',
                    '-gencode=arch=compute_75,code=sm_75',
                    '-gencode=arch=compute_80,code=sm_80',
                    '-gencode=arch=compute_86,code=sm_86',
                    '-gencode=arch=compute_89,code=sm_89',
                    '-gencode=arch=compute_90,code=sm_90',
                    '-gencode=arch=compute_90,code=compute_90'
                ]
            }),

        CUDAExtension('lietorch_extras', 
            include_dirs=[f"{CUDA_HOME}/include"],
            library_dirs=[f"{CUDA_HOME}/lib"],
            libraries=['cudart'],
            sources=[
                'lietorch/extras/altcorr_kernel.cu',
                'lietorch/extras/corr_index_kernel.cu',
                'lietorch/extras/se3_builder.cu',
                'lietorch/extras/se3_inplace_builder.cu',
                'lietorch/extras/se3_solver.cu',
                'lietorch/extras/extras.cpp',
            ],
            extra_compile_args={
                'cxx': ['-O2'], 
                'nvcc': [
                    '-O2',
                    '-gencode=arch=compute_60,code=sm_60',
                    '-gencode=arch=compute_61,code=sm_61',
                    '-gencode=arch=compute_70,code=sm_70',
                    '-gencode=arch=compute_75,code=sm_75',
                    '-gencode=arch=compute_80,code=sm_80',
                    '-gencode=arch=compute_86,code=sm_86',
                    '-gencode=arch=compute_89,code=sm_89',
                    '-gencode=arch=compute_90,code=sm_90',
                    '-gencode=arch=compute_90,code=compute_90'
                ]
            }),
    ],
    cmdclass={'build_ext': BuildExtension}
)


