from cmaketools import setup

setup(
    name="pybind_example",
    version="0.0.1",
    author="Takeshi (Kesh) Ikuma",
    author_email="tikuam@gmail.com",
    description="A test package using pybind11",
    url="https://github.com/python-cmaketools/pybind-example.git",
    license="MIT License",
    src_dir="src",
    ext_module_hint=r"pybind11_add_module",
    has_package_data=False,
)
