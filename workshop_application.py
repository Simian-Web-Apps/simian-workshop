"""Workshop application.

Built for simian.gui 3.0.0.
"""

import numbers

import plotly.express
from pandas import DataFrame as pandas_DataFrame
from simian.gui import Form, component, component_properties, utils

# Import the GAP Minder data from the Plotly Express module.
# The resulting GAP_DATA is a pandas.DataFrame. The columns that will be used are:
# "year" and "continents"
GAP_DATA = plotly.express.data.gapminder()
GAP_DATA.insert(0, "id", GAP_DATA.index)  # 'id' is needed in DataTables, so we are adding it here.


if __name__ == "__main__":
    # Run Workshop application locally as a script.
    from simian.local import Uiformio

    Uiformio("workshop_application", window_title="Workshop application", show_refresh=True)


def gui_init(_meta_data: dict) -> dict:
    """Initializes the form.

    Initialization of the form and the components therein.

    Returns:
        payload:    Form definition.
    """
    # Create a form and add a label.
    # form = Form(from_file=__file__)
    form = Form("form")

    # Programmatically add a label.
    label = component.HtmlElement(key="Empty", parent=form)
    label.content = "<b>Intentionally left empty</b>"

    # Put the form in the outputs and set a title and subtitle.
    payload = {
        "form": form,
        "navbar": {
            "title": "Workshop application",
            "subtitle": "<small>Simian Web Apps</small>",
        },
    }

    return payload


def gui_event(meta_data: dict, payload: dict) -> dict:
    """Event handling of the application.

    Args:
        meta_data:      Form meta data.
        payload:        Current status of the Form's contents.

    Returns:
        payload:        Updated Form contents.
    """
    if payload["event"] == "LoadData":
        utils.addAlert(payload, "The Load data button was clicked.", "info")

    else:
        utils.addAlert(payload, f"Unexpected event '{payload['event']}' encountered.", "danger")

    return payload


def filter_data(selected_years: list) -> pandas_DataFrame:
    """Filter GAP data based on selected years."""
    if isinstance(selected_years, numbers.Number):
        # Selected year is a number. Put in a list for use in the filtering.
        selected_years = [selected_years]

    # Filter the GAP data.
    new_gap = GAP_DATA[GAP_DATA["year"].isin(selected_years)]

    return new_gap


def update_plot(payload: dict, filtered_gap_data: pandas_DataFrame = GAP_DATA) -> None:
    """Update the plot with a 'filtered' set of data."""
    # Recreate the Plotly object.
    plot_obj = utils.getSubmissionData(payload, key="plot")[0]

    # Plot the new newly calculated x and y values, append the legend and put the plotly
    # object in the submission data.
    if len(filtered_gap_data) == 0:
        # No data. Empty the plot.
        plot_obj.figure = None

    else:
        # Fill the plot with data.
        # https://plotly.com/python/line-and-scatter/
        plot_obj.figure = plotly.express.scatter(
            filtered_gap_data,
            x="gdpPercap",
            log_x=True,
            y="lifeExp",
            symbol="year",
            size="pop",
            size_max=60,
            color="continent",
            hover_name="country",
        )

    # Put the new plot contents in the payload.
    utils.setSubmissionData(payload, "plot", plot_obj)
