import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    result = {
        "classification": "Health",
        "priority": "High"
    }

    return func.HttpResponse(
        json.dumps(result),
        mimetype="application/json"
    )
