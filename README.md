# Health-Tracking-Application

This Python application allows users to track their exercise details using the Nutritionix API and store them in a Google Sheets-like service provided by the Sheety API. Users can record exercises, durations, and calories burned, which are then stored in a structured format for easy tracking and analysis.

Features
Exercise Tracking: Record exercises performed, including name, duration, and calories burned.
Automatic Timestamps: Each exercise entry is automatically timestamped with the date and time of entry.
Data Storage: Utilizes Sheety API to store exercise data securely in a cloud-based spreadsheet.
Installation
To run the application locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/health-tracking-app.git
cd health-tracking-app
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Ensure you have Python installed on your machine.

Set up API keys:

Obtain API keys for Nutritionix and Sheety APIs.
Update the application_id and api_key variables in exerciseData.py with your Nutritionix API credentials.
Ensure the URLs in exerciseData.py point to your Sheety API endpoints.
Usage
Run the application:

bash
Copy code
python exerciseData.py
Input exercise details:

Follow the prompts to enter the exercise you did. The application will fetch exercise details using the Nutritionix API.

View recorded data:

Data is automatically recorded and stored in your Sheety API-connected spreadsheet. You can view and analyze your exercise history directly from the spreadsheet.

Error Handling
The application includes basic error handling to manage API request errors and unexpected inputs. If errors occur during API requests or data processing, appropriate error messages will be displayed to the user.

Contributing
Contributions are welcome! If you have suggestions for improvements or find any issues, please submit a pull request or open an issue.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Notes:

This README provides a basic structure to help users understand, install, and utilize your health tracking application effectively. Adjust it according to your specific project details and audience needs.





