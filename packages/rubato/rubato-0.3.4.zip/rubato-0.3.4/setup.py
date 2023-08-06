"""Setup File"""
from setuptools import Extension, setup
from Cython.Build import cythonize
import os

if "RUBATO_VERSION" in os.environ:
    version = os.environ["RUBATO_VERSION"]
else:
    version = "0.0.0"

if "TEST_MODE" in os.environ:
    linetrace = os.environ["TEST_MODE"] == "1"
else:
    linetrace = False


def package_files(directory):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


setup(
    version=version,
    package_data={"rubato": [*package_files("rubato/static"),
                             os.path.join("..", "rubato/c_src/", "cdraw.pxd")]},
    ext_modules=[
        *cythonize(
            Extension(
                "rubato.c_src.c_draw",
                ["rubato/c_src/c_draw.py", "rubato/c_src/cdraw.cpp"],
                extra_compile_args=["-std=c++14"],
                language="c++",
            ),
        ),
        *cythonize(
            "rubato/**/*.py",
            exclude=["rubato/__pyinstaller/**/*", "rubato/static/**/*", "rubato/c_src/**/*"],
            compiler_directives={
                "embedsignature": True,
                "language_level": 3,
                "linetrace": linetrace,
                "emit_code_comments": True,
            },
        ),
    ]
)
