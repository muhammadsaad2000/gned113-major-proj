from flask import Flask, render_template
import folium

app = Flask(__name__)

# Animal data
animal_data = {
    "elephant": {
        "location": [1.3521, 103.8198],
        "details": "Elephants face habitat loss, poaching for ivory, and human-wildlife conflict.",
        "help": [
            "Support anti-poaching laws.",
            "Donate to wildlife conservation organizations.",
            "Spread awareness about the ivory trade."
        ],
        "fun_fact": "Elephants can communicate using infrasound, which travels long distances."
    },
    "tiger": {
        "location": [20.5937, 78.9629],
        "details": "Tigers are endangered due to habitat destruction, poaching, and human conflict.",
        "help": [
            "Support wildlife protection laws.",
            "Avoid products made from tiger parts.",
            "Contribute to tiger conservation programs."
        ],
        "fun_fact": "A tiger's roar can be heard up to two miles away!"
    },
    "polar_bear": {
        "location": [70.0000, -120.0000],
        "details": "Polar bears are affected by climate change, which reduces their sea ice habitat.",
        "help": [
            "Reduce your carbon footprint.",
            "Support organizations like Polar Bears International.",
            "Advocate for climate action policies."
        ],
        "fun_fact": "Polar bears can swim for days to find food, sometimes covering over 60 miles."
    },
    "orangutan": {
        "location": [3.2028, 113.4914],
        "details": "Orangutans are endangered due to deforestation for palm oil plantations and illegal pet trade.",
        "help": [
            "Choose products made with sustainable palm oil.",
            "Support organizations like Orangutan Foundation International.",
            "Avoid contributing to illegal wildlife trade."
        ],
        "fun_fact": "Orangutans share 97% of their DNA with humans and are highly intelligent tool users."
    },
    "sea_turtle": {
        "location": [15.5000, -90.3000],
        "details": "Sea turtles are endangered due to poaching, bycatch, climate change, and marine pollution.",
        "help": [
            "Reduce plastic use to prevent ocean pollution.",
            "Support marine cleanup initiatives.",
            "Protect nesting sites by volunteering or donating."
        ],
        "fun_fact": "Sea turtles can hold their breath for up to 7 hours while sleeping underwater."
    },
    "amur_leopard": {
        "location": [45.0000, 130.0000],
        "details": "Amur leopards face habitat loss, poaching, and prey scarcity.",
        "help": [
            "Support habitat restoration programs.",
            "Donate to organizations like WWF.",
            "Spread awareness about the importance of predators in ecosystems."
        ],
        "fun_fact": "Amur leopards can jump more than 10 feet vertically, making them excellent hunters."
    },
    "pangolin": {
        "location": [6.4281, -9.4295],
        "details": "Pangolins are heavily trafficked for their scales and meat.",
        "help": [
            "Support anti-trafficking laws and enforcement.",
            "Spread awareness about illegal wildlife trade.",
            "Avoid products derived from pangolins."
        ],
        "fun_fact": "Pangolins can roll into a tight ball when threatened, using their tough scales for protection."
    },
    "vaquita": {
        "location": [31.5000, -114.0000],
        "details": "Vaquitas are critically endangered due to bycatch in illegal fishing nets.",
        "help": [
            "Support efforts to remove illegal fishing gear.",
            "Donate to organizations like Sea Shepherd.",
            "Advocate for sustainable fishing practices."
        ],
        "fun_fact": "Vaquitas are the smallest porpoises and have distinctive dark rings around their eyes."
    },
    "red_panda": {
        "location": [27.0000, 87.0000],
        "details": "Red pandas face deforestation, habitat fragmentation, and illegal pet trade.",
        "help": [
            "Support reforestation projects in the Himalayas.",
            "Avoid contributing to illegal wildlife trade.",
            "Donate to organizations like the Red Panda Network."
        ],
        "fun_fact": "Red pandas use their bushy tails for balance and as blankets in the cold."
    },
    "blue_whale": {
        "location": [-8.7832, -124.5085],
        "details": "Blue whales are endangered due to ship strikes, climate change, and ocean pollution.",
        "help": [
            "Advocate for stricter marine traffic regulations.",
            "Support organizations like Ocean Conservancy.",
            "Reduce ocean pollution by avoiding single-use plastics."
        ],
        "fun_fact": "The blue whale’s heart weighs as much as a small car, and their tongue can weigh as much as an elephant!"
    }
}



@app.route('/<animal_name>')
def show_animal(animal_name):
    animal = animal_data.get(animal_name)

    if animal:
        # Create a map centered on the animal's location with dynamic size
        animal_map = folium.Map(location=animal["location"], zoom_start=4)

        # Add a marker
        folium.Marker(
            location=animal["location"],
            popup=f"<b>Fun Fact:</b> {animal['fun_fact']}<br><b>Why Endangered:</b> {animal['details']}",
            icon=folium.Icon(icon="info-sign", color="green")
        ).add_to(animal_map)

        # Save the map to HTML
        animal_map.save('static/map.html')

        # Render the template
        return render_template(
            'map.html',
            details=animal['details'],
            fun_fact=animal['fun_fact'],
            help=animal['help']
        )
    else:
        return "Animal not found", 404

if __name__ == '__main__':
    app.run(debug=True)