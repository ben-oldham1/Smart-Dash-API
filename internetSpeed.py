import speedtest
import ssl
import json
import datetime

# Load existing data from the JSON file
def load_data_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

# Save data to the JSON file
def save_data_to_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def getInternetSpeed():
    # Disable SSL verification
    ssl._create_default_https_context = ssl._create_unverified_context

    # Run the speed test
    st = speedtest.Speedtest(secure=True)
    st.get_best_server()
    st.download()
    st.upload()

    result = st.results.dict()


    # Path to the JSON file
    json_file_path = "internetSpeedData.json"

    # Load existing data from the JSON file
    records = load_data_from_json(json_file_path)

    # Calculate current internet speed
    current_time = datetime.datetime.now().strftime("%H:%M")
    download_speed, upload_speed = round((result['download'] / 1000000), 1), round((result['upload'] / 1000000), 1)

    # Append the new record to the list
    records.append({
        "time": current_time,
        "download": download_speed,
        "upload": upload_speed
    })

    # Keep only the last 6 records
    records = records[-8:]

    # Save updated data to the JSON file
    save_data_to_json(json_file_path, records)


    return result, records