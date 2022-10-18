from flask import Flask, render_template
from flask_wtf import FlaskForm
from web_pokedex import get_pokemon_description, get_height_and_weight, \
    get_pokemon_number, get_pokemon_image, get_attacks_list, get_pokemon_type, get_vulnerability_list
from wtforms import StringField, SubmitField
from wtforms.validators import input_required
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = "PokemonKnowledge"
boot = Bootstrap(app)


class PokemonInfo(FlaskForm):
    name = StringField(validators=[input_required()])
    submit_btn = SubmitField(label="Let me know!")


@app.route("/", methods=["POST", "GET"])
def main_screen():
    form_flask = PokemonInfo()
    if form_flask.validate_on_submit():
        pokemon_name = form_flask.name.data
        number = get_pokemon_number(pokemon_name)
        description = get_pokemon_description(number)
        image_link = get_pokemon_image(number)
        attacks = get_attacks_list(number)
        pokemon_type = get_pokemon_type(number)
        vulnerability = get_vulnerability_list(number)
        height_and_weight = get_height_and_weight(number)
        return render_template("result.html", name=pokemon_name, number=number, description=description,
                               image=image_link, attacks=attacks, pkmn_type=pokemon_type, vuln=vulnerability,
                               h_and_w=height_and_weight)
    return render_template("index.html", form=form_flask)


if __name__ == "__main__":
    app.run(debug=True)