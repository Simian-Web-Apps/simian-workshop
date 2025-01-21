"""Run workshop example."""

if __name__ == "__main__":
    from simian.local import Uiformio

    Uiformio(
        "simian.examples.workshop_example",
        window_title="Workshop application",
        # debug=True,  # Enable to get a webbrowser developer tools window.
        show_refresh=True,  # Adds a refresh button to reload Python code.
    )
