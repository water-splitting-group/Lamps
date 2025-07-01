# Lamp Interpolation App

This is a small Streamlit-based tool to calculate power settings for different lamp configurations using cubic spline interpolation. The app allows selection of lamp types and input of desired power, then returns the appropriate setting and a plot of the data.

## 📦 Installation

You can install the app directly from this repository using pip:

    pip install git+https://github.com/AlexEith/Lamps.git

## ▶️ Usage

To run the Streamlit app:

    streamlit run streamlit_app/lamps.py

## 📁 Data File Format

Your CSV data files must be placed in a folder named `lamps/` in the same directory where you run the app. Filenames must follow this format:

    <type>_<wavelength>_<power_source>_<beamcombiner>.csv

      type: HP or UHP
      wavelength: 365, 405, 6500K or analog
      power_source: 1000mA-1-LED-1, 13A-1, 18A-1 or analog
      beamcombiner: noBC, above415 or below400
  
Example:

    HP_415-1_1000mA-1-LED-2_above415.csv

Each file should contain at two columns:
- `power`: Measured power values
- `setting`: Corresponding device settings

## 🧾 Requirements

All required packages are listed in `requirements.txt` and will be installed automatically when using pip.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

