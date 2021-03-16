from getgauge.python import step, before_scenario, Messages
import requests

@step("User can get location for US.")
def get_post():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200

