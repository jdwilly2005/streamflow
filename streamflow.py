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


# AI-assisted (Step 5): Claude wrote this function. The comments explain each part.
def summarize(dates, flows, sites):
    """Print a table of max, date of max, min, and average flow for each gauge, and save it to streamflow_summary.csv."""
    # Excel check for gauge 10163000: MAX = 131 cfs, AVERAGE = 56.95 cfs
    # (matches this function's output: max 131.0, avg 57.0 after rounding)

    # print the table header; the numbers after the colons are column widths
    # (< means left-aligned, > means right-aligned) so the columns line up
    print(f"{'Gauge':<10}{'Max (cfs)':>10}  {'Date of max':<18}{'Min (cfs)':>10}{'Avg (cfs)':>10}")

    # open the CSV file for writing ("w" creates it or replaces an old copy);
    # the with-block closes the file automatically when it ends
    with open("streamflow_summary.csv", "w") as file:
        # first line of the CSV is the column names
        file.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")

        # loop over the gauges; column i of flows is the gauge sites[i]
        for i in range(len(sites)):
            gauge_flows = flows[:, i]         # every reading for this gauge

            max_flow = np.max(gauge_flows)    # highest flow
            min_flow = np.min(gauge_flows)    # lowest flow
            avg_flow = np.mean(gauge_flows)   # average flow

            # np.argmax gives the row number of the highest flow; the same row
            # in dates is when it happened. datetime_as_string with unit="m"
            # turns it into text down to the minute ("2021-06-01T00:00"), and
            # replace swaps the T for a space to match the table format
            max_row = np.argmax(gauge_flows)
            max_date = np.datetime_as_string(dates[max_row], unit="m").replace("T", " ")

            # print one row of the table; .1f means 1 decimal place
            print(f"{sites[i]:<10}{max_flow:>10.1f}  {max_date:<18}{min_flow:>10.1f}{avg_flow:>10.1f}")

            # write the same values to the CSV, separated by commas
            file.write(f"{sites[i]},{max_flow:.1f},{max_date},{min_flow:.1f},{avg_flow:.1f}\n")


# Main program
# site numbers in the same order as the columns in the CSV
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")

# print and save the summary first, so the table shows up before the plot
# window opens (the program pauses at plt.show() until the window is closed)
summarize(dates, flows, sites)

plot_streamflow(dates, flows, sites)
