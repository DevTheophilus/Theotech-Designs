from flask import Flask, render_template, request
import os

app = Flask(__name__)

def download_youtube_video(video_url, output_path="."):
    # Your download_youtube_video function code goes here (same as previous examples)

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            video_url = request.form["video_url"]
        output_path = os.path.join("downloads")
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        download_youtube_video(video_url, output_path)
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
