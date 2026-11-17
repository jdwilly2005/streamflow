import matplotlib.pyplot as plt
import numpy as np


# AI-assisted (Step 3): Claude helped move the existing load and plot code into
# these two functions. The comments below explain what each part does.

def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    # load csv as strings, skipping the "Site Number:" header row
    data = np.genfromtxt(filename, delimiter=",", skip_header=1, dtype=str)

    # column 0 holds the date/time of each 15-minute reading
    dates = data[:, 0].astype("datetime64[s]")

    # columns 1-5 hold the five gauges; slicing them all at once (1:) and
    # converting to float gives a 2D array with one row per reading and one
    # column per gauge (this replaces the separate y_1 through y_5 arrays)
    flows = data[:, 1:].astype(float)

    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
    # plot one line per gauge: column i of flows goes with site number sites[i]
    for i in range(len(sites)):
        plt.plot(dates, flows[:, i], label="Site " + sites[i])

    # plot title
    plt.title("Provo River Streamflow, June 2021")

    # plot axis labels
    plt.xlabel("Date")
    plt.ylabel("Streamflow (cfs)")

    # add legend and grid
    plt.legend()
    plt.grid(True)

    # save the figure as an image in the project folder (must come before
    # plt.show(), because closing the plot window clears the figure)
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")

    plt.show()


# Main program
# site numbers in the same order as the columns in the CSV
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
