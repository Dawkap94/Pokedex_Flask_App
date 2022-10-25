from flask import Flask, render_template
from flask_wtf import FlaskForm
import opposite_types
from pokedex_classes import PokemonInfo
from wtforms import StringField, SubmitField
from wtforms.validators import input_required
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = "PokemonKnowledge"
boot = Bootstrap(app)


class PokeInfo(FlaskForm):
    name = StringField(validators=[input_required()])
    submit_btn = SubmitField(label="Let me know!")


@app.route("/", methods=["POST", "GET"])
def main_screen():
    form_flask = PokeInfo()
    if form_flask.validate_on_submit():
        pokemon_name = form_flask.name.data
        if pokemon_name.lower() not in opposite_types.all_pokemons:
            return render_template("404.html")
        Pokemon = PokemonInfo(pokemon_name)
        description = Pokemon.get_pokemon_description()
        attacks = Pokemon.get_pokemon_attacks()
        vulnerability = Pokemon.get_vulnerability()
        height_and_weight = Pokemon.get_height_and_weight()
        evolutions = Pokemon.get_evolutions()
        evolutions_links = Pokemon.get_evolutions_pictures()
        return render_template("result.html", name=Pokemon.name, number=Pokemon.number, description=description,
                               image=Pokemon.image, attacks=attacks, pkmn_type=Pokemon.type, vuln=vulnerability,
                               h_and_w=height_and_weight, evolutions=evolutions, evos_links=evolutions_links)
    return render_template("index.html", form=form_flask)


if __name__ == "__main__":
    app.run(debug=True)