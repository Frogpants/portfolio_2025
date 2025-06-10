# locate.py
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from math import radians, sin, cos, sqrt, atan2
import csv
import os

locate_api = Blueprint('locate_api', __name__, url_prefix='/api/locate')
api = Api(locate_api)

last_location = None
last_distance = 0

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = sin(dphi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))

def speed_check(velocity):
    if velocity == 0:
        return "no movement"
    elif velocity <= 3:
        return "walk"
    elif velocity <= 5:
        return "run"
    elif velocity <= 8:
        return "bike"

    return "car"

def get_update_rate(velocity):
    if speed_check(velocity) == "walk":
        return 2
    elif speed_check(velocity) == "run":
        return 2
    elif speed_check(velocity) == "bike":
        return 1
    
    return 0.2

class LocateAPI:
    class _Find(Resource):
        def post(self):
            global last_location, last_distance

            data = request.get_json()
            lat = data.get('lat')
            lng = data.get('lng')
            radius = data.get('radius', 160.9)

            if lat is None or lng is None:
                return {"error": "Missing 'lat' or 'lng'"}, 400

            current_location = (lat, lng)

            if last_location is None:
                last_location = current_location
                last_distance = 0
                speed = 0
            else:
                distance = haversine(*last_location, *current_location)
                speed = abs(distance - last_distance)
                last_distance = distance
                last_location = current_location

            movement_mode = speed_check(speed)
            update_rate = get_update_rate(speed)

            results = []
            file_path = os.path.join('datasets', 'treas_parking_meters_loc_datasd.csv')

            try:
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        try:
                            p_lat = float(row['lat'])
                            p_lng = float(row['lng'])
                            dist = haversine(lat, lng, p_lat, p_lng)
                            if dist <= radius:
                                results.append({
                                    "zone": row["zone"],
                                    "area": row["area"],
                                    "sub_area": row["sub_area"],
                                    "pole": row["pole"],
                                    "config_id": row["config_id"],
                                    "config_name": row["config_name"],
                                    "date_inventory": row["date_inventory"],
                                    "lat": p_lat,
                                    "lng": p_lng,
                                    "sapid": row["sapid"],
                                    "distance": round(dist, 2)
                                })
                        except (ValueError, KeyError):
                            continue
            except FileNotFoundError:
                return {"error": "locations.csv not found"}, 500

            return jsonify({
                "nearby_meters": results,
                "user_distance": round(last_distance, 2),
                "speed": round(speed, 2),
                "movement_mode": movement_mode,
                "update_rate": update_rate
            })

api.add_resource(LocateAPI._Find, '/locate')

# meter_history.py
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from model.parking import ParkingAvailabilityModel
import csv
import datetime

app = Flask(__name__)
offset = 0

class history_api:
    def grab_data(self, size):
        now = datetime.datetime.now().hour - offset
        return (now - size), (now + size)

    def fetch_data_in_range(self, csv_file, size=3):
        start_idx, end_idx = self.grab_data(size)
        results = []

        with open(csv_file, newline='') as file:
            reader = list(csv.reader(file))
            headers = reader[0]
            rows = reader[1:]

            start_idx = max(0, start_idx)
            end_idx = min(len(rows) - 1, end_idx)
            selected_rows = rows[start_idx:end_idx + 1]
            results = [headers] + selected_rows

        return results

    @app.route('/api/fetch_data', methods=['GET'])
    def api_fetch_data(self):
        csv_filename = "treas_parking_meters_loc_datasd.csv"
        size = request.args.get('size', default=3, type=int)
        data = self.fetch_data_in_range(csv_filename, size)
        return jsonify(data)

api.add_resource(history_api, '/history')
