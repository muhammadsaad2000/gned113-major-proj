from flask import Flask, render_template
import folium

app = Flask(__name__)

# Animal data with locations, details, help, and fun facts
animal_data = {
    "elephant": {
        "location": [1.3521, 103.8198],
        "details": "Elephants are endangered due to poaching for ivory.",
        "help": "Support anti-poaching laws and promote ethical tourism.",
        "fun_fact": "Elephants can hear through their feet by detecting ground vibrations!"
    },
    "tiger": {
        "location": [20.5937, 78.9629],
        "details": "Tigers are endangered due to habitat loss and poaching.",
        "help": "Support wildlife protection laws and contribute to tiger conservation.",
        "fun_fact": "Tigers' stripe patterns are unique, like human fingerprints."
    },
    "polar_bear": {
        "location": [66.160507, -153.369141],
        "details": "Polar bears are endangered due to melting sea ice from climate change.",
        "help": "Reduce carbon footprints and support climate change initiatives.",
        "fun_fact": "Polar bears have black skin under their white fur to absorb heat!"
    },
    "orangutan": {
        "location": [-2.5489, 118.0149],
        "details": "Orangutans are endangered due to deforestation and illegal pet trade.",
        "help": "Avoid products with unsustainable palm oil and support wildlife rescues.",
        "fun_fact": "Orangutans are the heaviest tree-dwelling animals, with arms up to 7 feet long!"
    },
    "sea_turtle": {
        "location": [15.7835, -90.2308],
        "details": "Sea turtles are endangered due to pollution, climate change, and poaching.",
        "help": "Reduce plastic use, support marine clean-ups, and protect nesting sites.",
        "fun_fact": "Sea turtles have existed for over 100 million years!"
    },
    "amur_leopard": {
        "location": [45.7619, 134.2355],
        "details": "Amur leopards are endangered due to habitat destruction and poaching.",
        "help": "Support anti-poaching and habitat restoration programs.",
        "fun_fact": "Amur leopards are the rarest big cats, with only about 100 left in the wild."
    },
    "pangolin": {
        "location": [30.5595, 22.9375],
        "details": "Pangolins are heavily trafficked for their scales and meat.",
        "help": "Support laws against wildlife trafficking and donate to anti-poaching organizations.",
        "fun_fact": "Pangolins are the only mammals fully covered in scales!"
    },
    "vaquita": {
        "location": [31.8024, -116.5576],
        "details": "Vaquitas are endangered due to bycatch in illegal gillnets.",
        "help": "Support efforts to eliminate illegal fishing practices and marine conservation.",
        "fun_fact": "The vaquita is the smallest and most endangered marine mammal!"
    },
    "red_panda": {
        "location": [27.533, 88.5122],
        "details": "Red pandas are endangered due to deforestation and illegal pet trade.",
        "help": "Support reforestation and avoid products that contribute to deforestation.",
        "fun_fact": "Red pandas use their bushy tails as blankets in the cold."
    },
    "blue_whale": {
        "location": [-54.4296, 3.3166],
        "details": "Blue whales are endangered due to ship collisions and climate change.",
        "help": "Support marine conservation, reduce ocean pollution, and protect whale habitats.",
        "fun_fact": "Blue whales are the largest animals on Earth, weighing up to 200 tons!"
    }
}

@app.route('/<animal_name>')
def show_animal(animal_name):
    animal = animal_data.get(animal_name, None)

    if animal:
        # Create map centered on the animal's location
        animal_map = folium.Map(location=animal["location"], zoom_start=4)

        # Add marker with information about the animal
        folium.Marker(
            location=animal["location"],
            popup=f"Fun Fact: {animal['fun_fact']}\nWhy Endangered: {animal['details']}\nHow to Help: {animal['help']}",
            icon=folium.Icon(icon="info-sign")
        ).add_to(animal_map)

        # Save the map as HTML
        animal_map.save('static/map.html')

        # Render the template and show the map
        return render_template('map.html', details=animal['details'], fun_fact=animal['fun_fact'], help=animal['help'])
    else:
        return "Animal not found", 404

if __name__ == '__main__':
    app.run(debug=True)
