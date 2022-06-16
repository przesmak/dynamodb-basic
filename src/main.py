import boto3
from tables.add_config import add_config

if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4566')
    try:
        meter_table = dynamodb.Table("MeterConfigs")
        meter_table.load()
    except Exception as exc:
        raise Exception("somethign wrong: {}".format(exc)) 

    add_config(meter_table, "7in :: beta 0.55", "Shell", {
                            "meterType": "subsea",
                            "meterSize": "7in :: beta 0.55",
                            "commType": "serial_communication",
                            "measurementMode": "wetgas",
                            "salinityMeasurement": "formation_water_detection",
                            "transmitterConfiguration": {
                                "dualPressure": True,
                                "dualTemperature": True,
                                "dualDpInlet": True,
                                "DpOutlet": True,
                                "dualGamma": True
                            }})
