from flask import Flask
from flask import render_template
from random import choices

app = Flask(__name__)


def random_city():
    """Returns random city"""

    cities = ["Bengaluru", "Liverpool", "Kuala Lumpur"]
    return choices(cities)


@app.route("/")
def city():
    """Return random city"""

    my_city = random_city()
    return render_template("index.html", title="Random City", city=my_city)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
