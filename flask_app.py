from flask import Flask, render_template
import folium

app = Flask(__name__)

# Animal data with locations, details, and how to help
animal_data = {
    "elephant": {
        "location": [1.3521, 103.8198],  # Example: Singapore
        "details": "Elephants are endangered due to poaching for ivory.",
        "help": "Support anti-poaching laws and promote ethical tourism.",
        "fun_fact": "Elephants can hear through their feet by detecting ground vibrations!"
    },
    "tiger": {
        "location": [20.5937, 78.9629],  # India
        "details": "Tigers are endangered due to habitat loss and poaching.",
        "help": "Support wildlife protection laws and contribute to tiger conservation.",
        "fun_fact": "Tigers' stripe patterns are unique, like human fingerprints."
    },
    "polar_bear": {
        "location": [66.160507, -153.369141],  # Alaska
        "details": "Polar bears are endangered due to melting sea ice from climate change.",
        "help": "Reduce carbon footprints and support climate change initiatives.",
        "fun_fact": "Polar bears have black skin under their white fur to absorb heat!"
    },
    # Add additional animal data here
    # "red_panda": { "location": [...], "details": "...", "help": "...", "fun_fact": "..." }
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
