import requests
from datetime import datetime


def exerciseData():
    
    # today date and time using datetime module
    today = datetime.now().strftime("%y/%m/%d")
    time = datetime.now().time().strftime("%I:%M")

    
    # using nutritionix api to find the health tracker details like calories and more
    
    # https://trackapi.nutritionix.com/v2/natural/exercise
    
    
    application_id = "c538c062"
    api_key = "4a9d4a92879d064d84aced06f53a217f"
    url_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

    header = {
        "Content-Type": "application/json",
        "x-app-id": application_id,
        "x-app-key": api_key,
    }
    
    
    body = {"query": input("What exercise you did:-   "), "age": "20", "gender": "male"}
    response = requests.post(url=url_endpoint, json=body, headers=header)
    data = response.json()
    exercises = data["exercises"]
    
    
    
    for exercise in exercises:
        # parameter sequence in the of body for inserting data
        body = {
            "sheet1": {
                "date": today,
                "time": time,
                "exercise": exercise["name"],
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
        }
        
        # Using sheety api to insert data into the google sheets
        url = "https://api.sheety.co/162ce777f84396a7d41f65fbc4caef28/myworkout/sheet1"
        
        # Header is necessary to insert data into the google sheets
        header = {
            "Content-Type": "application/json",
        }

        response = requests.post(url, json=body, headers=header)
        data = requests.get(
            "https://api.sheety.co/162ce777f84396a7d41f65fbc4caef28/myworkout/sheet1"
        )


exerciseData()
