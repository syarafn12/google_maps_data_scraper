import requests
import pandas as pd
import os

# set file path 
file_path = "C:/Users/YourName/Documents/"  

# Set API KEY, Location and Radius
API_KEY = "YOUR_API_KEY" # put your API KEY
LOCATION = "40.712776,-74.005974"  # Example: New York City
RADIUS = 1000  # 1km

# Function to fetch places from Google Places API
def get_places(place_type):
    """Fetch places of a specific type from Google Places API."""
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={LOCATION}&radius={RADIUS}&type={place_type}&key={API_KEY}"
    response = requests.get(url).json()

    # Extract relevant data including latitude & longitude
    places = []
    for place in response.get("results", []):
        name = place.get("name", "N/A")
        address = place.get("vicinity", "N/A")
        lat = place["geometry"]["location"]["lat"]
        lng = place["geometry"]["location"]["lng"]
        rating = place.get("rating", "N/A")  # Some places may not have ratings

        places.append({"Name": name, "Address": address, "Latitude": lat, "Longitude": lng, "Rating": rating})

    return places

# define places that you want to get from Google Maps API
clinics = get_places("clinic")
residential = get_places("residential complex")
schools = get_places("school")

# Convert to DataFrame for easy analysis
df_clinics = pd.DataFrame(clinics)
df_schools = pd.DataFrame(schools)
df_residential = pd.DataFrame(residential)

# Save each CSV file using os.path.join
df_clinics.to_csv(os.path.join(file_path, "Clinics.csv"), index=False)
df_residential.to_csv(os.path.join(file_path, "Residential.csv"), index=False)
df_schools.to_csv(os.path.join(file_path, "Schools.csv"), index=False)

# Print confirmation messages
print(f"Clinics data saved successfully at: {os.path.join(file_path, 'Clinics.csv')}")
print(f"Residential data saved successfully at: {os.path.join(file_path, 'Residential.csv')}")
print(f"Schools data saved successfully at: {os.path.join(file_path, 'Schools.csv')}")

