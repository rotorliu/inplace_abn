from os import path, listdir

import setuptools
from torch.utils.cpp_extension import BuildExtension, CUDAExtension


def find_sources(root_dir):
    sources = []
    for file in listdir(root_dir):
        _, ext = path.splitext(file)
        if ext in [".cpp", ".cu"]:
            sources.append(path.join(root_dir, file))

    return sources


here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    # Meta-data
    name="inplace-abn",
    author="Lorenzo Porzi",
    author_email="lorenzo@mapillary.com",
    description="In-Place Activate BatchNorm for Pytorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mapillary/inplace_abn",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],

    # Versioning
    use_scm_version={"root": ".", "relative_to": __file__, "write_to": "inplace_abn/_version.py"},

    # Requirements
    setup_requires=["setuptools_scm"],
    python_requires=">=3, <4",

    # Package description
    packages=["inplace_abn"],
    ext_modules=[
        CUDAExtension(
            name="inplace_abn._backend",
            sources=find_sources("src"),
            extra_compile_args={
                "cxx": ["-O3"],
                "nvcc": []
            },
            include_dirs=["include/"],
        )
    ],
    cmdclass={"build_ext": BuildExtension}
)
