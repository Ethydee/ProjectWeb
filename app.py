from flask import Flask, url_for, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = "supersecretkey"


# TODO add more store items and categories


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/pizza")
def pizza():
    pizzas = {"Cheese": {"image": url_for("static", filename="imgs/cheese.png"), "cost": 8},
              "Pepperoni" : {"image": url_for("static", filename="imgs/pep.png"), "cost": 8},
              "Meat Lover": {"image": url_for("static", filename="imgs/meat.png"), "cost": 10},
              "Pineapple": {"image": url_for("static", filename="imgs/pine.png"), "cost": 8},
              "BBQ Chicken": {"image": url_for("static", filename="imgs/chicken.png"), "cost": 10}}
    return render_template("pizza.html", title="Order Pizza", pizzas=pizzas)


@app.route("/drinks")
def drinks():
    pizzas = {"Coke": {"image": url_for("static", filename="imgs/coke.png"), "cost": 1},
              "Pepsi" : {"image": url_for("static", filename="imgs/pepsi.png"), "cost": 1},
              "Sprite": {"image": url_for("static", filename="imgs/sprite.png"), "cost": 1},
              "Fanta Orange": {"image": url_for("static", filename="imgs/fanta.webp"), "cost": 1},
              "Mountain Dew": {"image": url_for("static", filename="imgs/dew.png"), "cost": 1}}
    return render_template("drinks.html", title="Order Drinks", pizzas=pizzas)


@app.route("/sides")
def sides():
    pizzas = {"Cheese Bread": {"image": url_for("static", filename="imgs/bread.png"), "cost": 8},
              "Pasta" : {"image": url_for("static", filename="imgs/pasta.png"), "cost": 8},
              "Bread Sticks": {"image": url_for("static", filename="imgs/sticks.png"), "cost": 10},
              "Hot Wings": {"image": url_for("static", filename="imgs/wings.png"), "cost": 8},
              "Sandwich": {"image": url_for("static", filename="imgs/sandwich.png"), "cost": 10}}
    return render_template("sides.html", title="Order Sides", pizzas=pizzas)


@app.route("/cart")
def cart():
    return  render_template("cart.html", title="Cart", noHR=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
