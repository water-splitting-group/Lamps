from setuptools import setup, find_packages

# Read the requirements
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='Lamps',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'run-myapp = Lamps.app:main',
        ],
    },
    author='Alexander Eith',
    description='Application to calculate the setting for a given power based on LED lamp data in the advanced irradiation setup V1.0',
    url='https://github.com/YOUR-USERNAME/YOUR-REPO',  # ← Replace this
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Streamlit',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
