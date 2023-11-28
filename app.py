import streamlit as st
import pandas as pd
import numpy as np
import openai
from functions import (
    calculate_nozzles,
    calculate_bottles,
    calculate_placement_bottles,
)
import matplotlib.pyplot as plt

st.title("Optimering for HH Fire Eater")

# Start form for describing the room
with st.form("dimensions"):
    st.subheader("Dimensjoner i rommet")
    length = st.number_input("Lengde (m)", value=10)
    width = st.number_input("Bredde (m)", value=16)
    height = st.number_input("Høyde (m)", value=3)

    submit = st.form_submit_button("Send")

# Plot and print the output of calculations based on the info from the form
if submit:
    (
        nozzle_x_coords,
        nozzle_y_coords_optimized,
        total_nozzles_optimized,
    ) = calculate_nozzles(length, width, 3.66, 7.32)

    (
        x_coord_bootles,
        y_coord_bottles,
        tubes,
        distance_tubes,
    ) = calculate_placement_bottles(
        nozzle_x_coords, nozzle_y_coords_optimized, width, length
    )

    fig, ax = plt.subplots()
    for tube in range(tubes):
        if y_coord_bottles == 0:
            bottle_axis = [x_coord_bootles, x_coord_bootles] + [
                nozzle_x_coords[tube] for _ in range(len(nozzle_y_coords_optimized) + 1)
            ]
            other_list = (
                [y_coord_bottles]
                + [2 for _ in range(2)]
                + [elm for elm in nozzle_y_coords_optimized]
            )
        else:
            other_list = [y_coord_bottles, y_coord_bottles] + [
                nozzle_y_coords_optimized[tube] for _ in range(len(nozzle_x_coords) + 1)
            ]
            bottle_axis = (
                [x_coord_bootles]
                + [2 for _ in range(2)]
                + [elm for elm in nozzle_x_coords]
            )

        ax.plot(
            bottle_axis,
            other_list,
            "g-",
            label="Rør " + str(tube + 1),
            linewidth=2,
        )

    for y in nozzle_y_coords_optimized:
        ax.plot(
            nozzle_x_coords,
            [y] * len(nozzle_x_coords),
            "ro",
            label="Dyser" if y == nozzle_y_coords_optimized[0] else "",
        )
    ax.plot(x_coord_bootles, y_coord_bottles, "bo", label="Flasker")

    ax.set_xlim(0, width)
    ax.set_ylim(0, length)
    ax.set_title("Optimert plassering av dyser, flasker og rør i et rom")
    ax.set_xlabel("Bredde (m)")
    ax.set_ylabel("Lengde (m)")
    ax.legend()

    st.write("Totalt antall dyser: ", str(total_nozzles_optimized), "m")
    st.write(
        "Antall flasker som trengs: ",
        str(int(np.ceil(calculate_bottles(width, length, height)))),
        "m",
    )
    st.write("Antall meter med rør som trengs: ", str(distance_tubes), "m")
    st.pyplot(fig)
