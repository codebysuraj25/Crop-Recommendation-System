from flask import Flask, render_template, request

app = Flask(__name__)

def recommend_crop(soil, season, rainfall, temperature):

    if soil == "Black" and season == "Kharif":
        return "Cotton 🌱"
    elif soil == "Alluvial" and season == "Rabi":
        return "Wheat 🌾"
    elif soil == "Red" and season == "Kharif":
        return "Groundnut 🥜"
    elif soil == "Sandy" and season == "Summer":
        return "Watermelon 🍉"
    elif rainfall == "High" and season == "Kharif":
        return "Rice 🌾"
    elif rainfall == "Low" and season == "Rabi":
        return "Gram (Chana) 🌱"
    elif temperature == "High" and soil == "Sandy":
        return "Bajra (Pearl Millet) 🌾"
    elif temperature == "Low" and season == "Rabi":
        return "Mustard 🌼"
    else:
        return "Maize 🌽"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    soil = request.form.get("soil")
    season = request.form.get("season")
    rainfall = request.form.get("rainfall")
    temperature = request.form.get("temperature")

    crop = recommend_crop(soil, season, rainfall, temperature)

    crop_images = {
        "Rice 🌾": "rice.png",
        "Wheat 🌾": "wheat.png",
        "Cotton 🌱": "cotton.png",
        "Maize 🌽": "maize.png",
        "Mustard 🌼": "mustard.png",
        "Watermelon 🍉": "watermelon.png",
        "Gram (Chana) 🌱": "gram.png",
        "Groundnut 🥜": "groundnut.png",
        "Bajra (Pearl Millet) 🌾": "bajra.png"
    }

    crop_image = crop_images.get(crop, "default.png")

    return render_template("result.html",
                           soil=soil,
                           season=season,
                           rainfall=rainfall,
                           temperature=temperature,
                           crop=crop,
                           crop_image=crop_image)


if __name__ == "__main__":
    app.run(debug=True)
