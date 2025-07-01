import os
import streamlit as st
import pandas as pd
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def main():
    st.title("LED Lamp Settings Calculator")
    st.write("This app calculates the setting for a given power based on LED lamp data.")

    # Get the absolute path of the folder containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(script_dir, "..", "lamps")

    
    if not os.path.exists(data_folder):
        st.error(f"Data folder does not exist at this path: `{data_folder}`")
        return

    # Case-insensitive extension check here:
    all_files = [f for f in os.listdir(data_folder) if f.lower().endswith(".csv")]
    
    if not all_files:
        st.warning("No CSV files found in the folder.")
        return

    file_tuples = [tuple(f[:-4].split('_')) for f in all_files if len(f[:-4].split('_')) == 4]

    if not file_tuples:
        st.warning("No CSV files with the correct filename pattern found.")
        return

    # Dropdown 1: first part
    first_options = sorted(set(p[0] for p in file_tuples))
    selected_first = st.selectbox("LED type (HP = high power, UHP = ultra high power)", first_options)

    # Dropdown 2: second part (filtered by first)
    filtered_second = [p for p in file_tuples if p[0] == selected_first]
    second_options = sorted(set(p[1] for p in filtered_second))
    selected_second = st.selectbox("Lightsource", second_options)

    # Dropdown 3: third part (filtered by first and second)
    filtered_third = [p for p in filtered_second if p[1] == selected_second]
    third_options = sorted(set(p[2] for p in filtered_third))
    selected_third = st.selectbox("Power source", third_options)

    # Dropdown 4: fourth part (filtered by first, second, and third)
    filtered_fourth = [p for p in filtered_third if p[2] == selected_third]
    fourth_options = sorted(set(p[3] for p in filtered_fourth))
    selected_fourth = st.selectbox("Beamcombiner: no = noBC, yes = BC", fourth_options)

    # Construct final filename
    final_filename = f"{selected_first}_{selected_second}_{selected_third}_{selected_fourth}.csv"

    file_path = os.path.join(data_folder, final_filename)

    desired_power_w = st.number_input("Enter desired power (in W)", value=0.100, step=0.001, format="%.3f")

    if os.path.exists(file_path):
        data = pd.read_csv(file_path, delimiter=';')
        df_sorted = data.sort_values('power').drop_duplicates('power')
        settings = df_sorted['setting'].values
        power_values = df_sorted['power'].values

        cs_inverse = CubicSpline(power_values, settings)
        calculated_setting = cs_inverse(desired_power_w)
        power_per_area = desired_power_w / 1.13 * 1000

        st.write(f"**Using file:** `{final_filename}`")
        st.write(f"**Calculated setting for {desired_power_w:.3f} W:** {calculated_setting:.3f}")
        st.write(f"**Power per cm²:** {power_per_area:.4f} mW/cm²")

        # Plot
        x_smooth = np.linspace(power_values.min(), power_values.max(), 300)
        y_smooth = cs_inverse(x_smooth)
        fig, ax = plt.subplots()
        ax.plot(power_values, settings, 'o', label='Data points', color='blue')
        ax.plot(x_smooth, y_smooth, label='Cubic Spline', color='green')
        ax.set_xlabel("Power [mW]")
        ax.set_ylabel("Setting [-]")
        ax.legend()
        st.pyplot(fig)
    else:
        st.error("The selected file does not exist.")

if __name__ == "__main__":
    main()
