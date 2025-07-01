from setuptools import setup, find_packages

# Read the requirements
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='my_streamlit_app',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'run-myapp = my_streamlit_app.app:main',
        ],
    },
    author='Alexander Eith',
    description='A small Streamlit app.',
    url='https://github.com/YOUR-USERNAME/YOUR-REPO',  # ← Replace this
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Streamlit',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
