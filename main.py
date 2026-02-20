from extractor.asteroids_extractor import AsteroidsExtractor
from client.storage_client import GCSClient
from utils.logger import logger
from utils.helper import validate_date

def main(request):
    request_json = request.get_json(silent=True)

    start_date = request_json.get("start_date")
    end_date = request_json.get("end_date")


    if not start_date or not end_date:
        return {"error": "start_date and end_date are required"}, 400

    if not validate_date(start_date) or not validate_date(end_date):
        return {"error": "Dates must be in YYYY-MM-DD format"}, 400

    extractor = AsteroidsExtractor(start_date, end_date)
    client = GCSClient()
    filename = f"extracted/asteroids_{start_date}_{end_date}.json"
    try:
        data = extractor.get_asteroids_data()

        if not data:
            logger.warning("No asteroids data found")
            return {"message": "No data found"}, 204

        logger.info(f"Uploading asteroid data, file_path: {filename}, record_count: {len(data)}")

        client.upload(data, filename)
        logger.info("Upload successful")
        return {"message": "Extract complete", "file_path": filename}
    except Exception:
        logger.exception("Asteroid extraction failed")
        return {"error": "Internal server error"}, 500
