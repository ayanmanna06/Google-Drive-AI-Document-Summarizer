from flask import Flask, render_template,send_file
from controller.drive_controller import process_drive_documents

app = Flask(__name__)

@app.route("/")
def home():

    results = process_drive_documents()

    return render_template(
        "index.html",
        results=results
    )

@app.route("/download-report")
def download_report():

    return send_file(
        "reports/document_summary_report.csv",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)