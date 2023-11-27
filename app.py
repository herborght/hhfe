import streamlit as st
import pandas as pd
import numpy as np
import openai
from functions import (
    general_gpt,
    calculate_nozzles,
    calculate_bottles,
    calculate_placement_bottles,
)
import matplotlib.pyplot as plt

st.title("Optimizing nozzles")

# length = 10
# width = 8

with st.form("dimensions"):
    length = st.number_input("length", value=10)
    width = st.number_input("width", value=8)
    height = st.number_input("height", value=3)

    submit = st.form_submit_button("Submit")

if submit:
    # Assuming 'calculate' function is defined elsewhere
    (
        nozzle_x_coords,
        nozzle_y_coords_optimized,
        total_nozzles_optimized,
    ) = calculate_nozzles(width, length, 3.66, 7.32)

    # st.write("x-coords", nozzle_x_coords)
    # st.write("y-coords", nozzle_y_coords_optimized)
    st.write("Total Nozzles", total_nozzles_optimized)

    fig, ax = plt.subplots()

    x_coord_bootles, y_coord_bottles, tubes = calculate_placement_bottles(
        nozzle_x_coords, nozzle_y_coords_optimized, length, width
    )
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
            label="line " + str(tube + 1),
            linewidth=2,
        )

    # Ensure that the lengths of both lists are the same
    for y in nozzle_y_coords_optimized:
        ax.plot(
            nozzle_x_coords,
            [y] * len(nozzle_x_coords),
            "ro",
            label="Optimized Nozzles" if y == nozzle_y_coords_optimized[0] else "",
        )
    ax.plot(x_coord_bootles, y_coord_bottles, "bo")

    ax.set_xlim(0, length)
    ax.set_ylim(0, width)
    ax.set_title("Optimized Floor Plan with Nozzle Placement")
    ax.set_xlabel("Length (m)")
    ax.set_ylabel("Width (m)")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
