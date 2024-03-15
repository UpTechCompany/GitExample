from flask import Flask
from storage import storage
from logic.convert_factory import convert_factory
import os
from logic.data_factory import data_factory
app = Flask(__name__)

@app.route("/api/report/<storage_key>/<format>", methods=["GET"])
def get_report(storage_key: str, format: str):
    s = storage.storage()
    if storage_key.lower() not in s.get_all_keys():
        response_type = app.response_class(
            response=f"Такого ключа не существует",
            status=500,
            mimetype="application/text"
        )

        return response_type

    if format.lower() not in [x.split(".")[0][5:] for x in os.listdir("logic/formats")]:
        response_type = app.response_class(
            response=f"Ключ существует, но этот формат экспорта недоступен",
            status=500,
            mimetype="application/text"
        )
        return response_type


    response_type = app.response_class(
        response=f"{storage_key}, {convert_factory()}",
        status=200,
        mimetype=f"application/{format}"
    )

    return response_type


if __name__ == "__main__":
    app.run(debug=True)
