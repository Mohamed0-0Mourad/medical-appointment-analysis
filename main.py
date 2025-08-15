# import charts
from layouts.home_layout import get_layout
from dash import Dash
from callbacks.update_home import register_callbacks
import preproccessing

external_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css","https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css", "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"]


def main():
    print("Running...")
    app = Dash(__name__, external_stylesheets=external_css)
    app.layout = get_layout()
    register_callbacks(app)
    app.run(debug=True)
    # charts.

if __name__ == "__main__":
    main()