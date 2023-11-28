import streamlit as st
import openai
import numpy as np
import matplotlib.pyplot as plt


@st.cache_data
def general_gpt(prompt: str):
    # make chat gpt completion function with streamlit
    openai.api_key = st.secrets["openai"]["api_key"]
    openai.api_type = "azure"
    openai.api_base = "https://cog-fxpoc-tonality-dev-01.openai.azure.com/"
    openai.api_version = "2023-03-15-preview"
    gpt_model = "gpt-4"
    completion = openai.ChatCompletion.create(
        deployment_id=gpt_model,
        messages=[
            {
                "role": "user",
                "content": "{}".format(prompt),
            }
        ],
        temperature=0.2,
        max_tokens=1500,
        top_p=1.0,
        frequency_penalty=0.1,
        presence_penalty=0.1,
    )
    return str(completion.choices[0].message.content)


def calculate_nozzles(
    length, width, max_distance_from_wall, max_distance_between_nozzles
):
    # Optimizing the placement of nozzles

    # Plotting the optimized floor plan with the nozzles
    plt.figure(figsize=(8, 5))
    plt.plot(
        [0, width, width, 0, 0],
        [0, 0, length, length, 0],
        "k-",
        label="Room boundary",
    )  # Room boundary

    # Calculate the number of nozzles needed along the width and length of the room
    nozzles_along_length = np.ceil(width / max_distance_between_nozzles)
    nozzles_along_width = (
        np.ceil((length - 2 * max_distance_from_wall) / max_distance_between_nozzles)
        + 1
    )

    # Calculate the spacing between nozzles
    spacing_length = width / nozzles_along_length
    spacing_width = length / nozzles_along_width

    # Generate the coordinates for the nozzles
    nozzle_x_coords = np.linspace(
        max_distance_from_wall,
        width - max_distance_from_wall,
        int(nozzles_along_length),
    )
    nozzle_y_coords_optimized = np.linspace(
        max_distance_from_wall,
        length - max_distance_from_wall,
        int(nozzles_along_width),
    )

    # Calculate the total number of nozzles in the optimized layout
    total_nozzles_optimized = int(nozzles_along_length * nozzles_along_width)
    return nozzle_x_coords, nozzle_y_coords_optimized, total_nozzles_optimized


def calculate_bottles(width, length, height):
    # (rommets m2 x rommets høyde)/43 = antall flasker
    number_of_bottles = width * length * height / 43
    return number_of_bottles


def calculate_placement_bottles(nozzles_x, nozzles_y, width, length):
    highest_x_cord = nozzles_x[-1]
    highest_y_cord = nozzles_y[-1]

    length_x_cord = len(nozzles_x)
    length_y_cord = len(nozzles_y)

    calc_distance_from_x = length_x_cord * highest_y_cord
    calc_distance_from_y = length_y_cord * highest_x_cord
    for x_elm in nozzles_x:
        calc_distance_from_x += abs(x_elm - (width / 2))

    for y_elm in nozzles_y:
        calc_distance_from_y += abs(y_elm - (length / 2))
    if calc_distance_from_x < calc_distance_from_y:
        x_coord = width / 2
        y_coord = 0
        tubes = length_x_cord
    else:
        x_coord = 0
        y_coord = length / 2
        tubes = length_y_cord

    return x_coord, y_coord, tubes
