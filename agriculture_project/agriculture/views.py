from django.shortcuts import render


# Sample crop recommendation logic
def get_crop_recommendation(soil_type, rainfall, temperature, location):
    crop_data = {
        "sandy": ["Maize", "Millet", "Groundnut"],
        "clay": ["Rice", "Wheat", "Barley"],
        "loamy": ["Tomato", "Potato", "Carrot"],
        "black": ["Cotton", "Soybean", "Pulses"]
    }

    # Simple logic: Recommend crops based on soil type
    recommended_crops = crop_data.get(soil_type.lower(), ["No suitable crop found"])

    # Further filter based on temperature and rainfall
    if int(temperature) > 30:
        recommended_crops = [crop for crop in recommended_crops if crop not in ["Wheat", "Barley"]]
    if int(rainfall) < 50:
        recommended_crops = [crop for crop in recommended_crops if crop not in ["Rice"]]

    return recommended_crops


# Home Page
def home(request):
    return render(request, 'home.html')


# Crop Recommendation Page
def crop_recommendation(request):
    recommendation = None

    if request.method == "POST":
        soil_type = request.POST.get("soilType")
        rainfall = request.POST.get("rainfall")
        temperature = request.POST.get("temperature")
        location = request.POST.get("location")  # Future use if needed

        recommendation = get_crop_recommendation(soil_type, rainfall, temperature, location)

    return render(request, 'crop_recommendation.html', {"recommendation": recommendation})


# Fertilizer Suggestion Page (Placeholder)
def fertilizer_suggestion(request):
    return render(request, 'fertilizer_suggestion.html')


# Disease Detection Page (Placeholder)
def disease_detection(request):
    return render(request, 'disease_detection.html')


# About Page
def about(request):
    return render(request, 'about.html')


# Contact Page
def contact(request):
    return render(request, 'contact.html')
