from setuptools import Extension, setup

from Cython.Build import cythonize

at_dir = "third-party/autotrace/src/"

at_sources = [
    "fit.c",
    "bitmap.c",
    "spline.c",
    "curve.c",
    "epsilon-equal.c",
    "vector.c",
    "color.c",
    # "datetime.c",
    "autotrace.c",
    # "output.c",
    # "input.c",
    "pxl-outline.c",
    "median.c",
    "thin-image.c",
    "logreport.c",
    "filename.c",
    "despeckle.c",
    "exception.c",
    "image-proc.c",
    "module.c",
    "output-eps.c",
    "output-er.c",
    "output-fig.c",
    "output-sk.c",
    "output-svg.c",
    "output-ugs.c",
    "output-p2e.c",
    "output-emf.c",
    "output-dxf.c",
    "output-epd.c",
    "output-pdf.c",
    "output-mif.c",
    "output-cgm.c",
    "output-dr2d.c",
    "output-pov.c",
    "output-plt.c",
    "output-ild.c",
    # "input-bmp.c",
    # "input-pnm.c",
    # "input-tga.c",
    # "input-gf.c",
]

at_sources = [at_dir + s for s in at_sources]

extensions = [
    Extension(
        "autotrace._autotrace",
        sources=[
            "autotrace/_autotrace.pyx",
            "autotrace/overrides.cpp",
            *at_sources,
        ],
        include_dirs=[
            at_dir,
            "third-party/autotrace/distribute/win/3rdparty/glib/include/glib-2.0/",
            "third-party/autotrace/distribute/win/3rdparty/glib/lib/glib-2.0/include/",
        ],
        define_macros=[
            ("AUTOTRACE_VERSION", '"0.40.0"'),
            ("AUTOTRACE_WEB", '"https://github.com/autotrace/autotrace"'),
            ("HAVE_MAGICK_READERS", 1),
            ("GLIB_STATIC_COMPILATION", 1),
        ],
    ),
]

with open("readme.md", "r") as file:
    long_description = file.read()

setup(
    name="pyautotrace",
    version="0.0.2",
    description="Python bindings for AutoTrace.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="LemonPi314",
    author_email="",
    url="https://github.com/LemonPi314/pyautotrace",
    license="MIT",
    keywords=["autotrace", "bitmap", "vector", "graphics", "tracing"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Cython",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    packages=["autotrace"],
    package_data={
        "autotrace": ["py.typed"],
    },
    python_requires=">=3.7.9",
    ext_modules=cythonize(extensions, compiler_directives={"language_level": 3}),
)
