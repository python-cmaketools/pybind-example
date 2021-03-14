from cmaketools import setup

setup(
    name="pybind_example",
    version="0.1.0",
    author="Takeshi (Kesh) Ikuma",
    author_email="tikuma@gmail.com",
    description="A test package using pybind11",
    url="https://github.com/python-cmaketools/pybind-example.git",
    license="MIT License",
    src_dir="src",
    ext_module_hint=r"pybind11_add_module",
    has_package_data=False,
)
