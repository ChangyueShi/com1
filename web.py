from flask import Flask, abort, send_from_directory, request
import spider
import visualization
from gevent.pywsgi import WSGIServer

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/', methods = ['GET', 'POST'])
def root():
    if request.method == "GET":
        try:
            return send_from_directory(".", "index.html")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=} while forwarding request")
            abort(500)
    elif request.method == "POST":
        # try:
        #     csv_file = spider.search_video(request.form.get("video_name"))
        #     return send_from_directory(".", visualization.wordCloud(csv_file, request.form.get("shape")))
        # except Exception as err:
        #     print(f"Unexpected {err=}, {type(err)=} while forwarding request")
        #     abort(500)

        try:
            result_type = request.form.get("type")
            video_name = request.form.get("video_name")

            if result_type == "wordcloud":
                shape = request.form.get("shape")
                csv_file = spider.search_video(video_name)
                result_file = visualization.wordCloud(csv_file, shape)
                return send_from_directory(".", result_file)
            elif result_type == "sentiment":
                csv_file = spider.search_video(video_name)
                result_file = visualization.emotionAnalysis(csv_file)
                return send_from_directory(".", result_file)
            elif result_type == "highlight":
                csv_file = spider.search_video(video_name)
                result_file = visualization.hightlights(csv_file)
                return send_from_directory(".", result_file)
            else:
                return "Invalid result type"

        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=} while forwarding request")
            abort(500)
    else:
        return "Method Not Allowed"

app.run("0.0.0.0", 3000)
# http_server = WSGIServer(("0.0.0.0", 3000), app)
# http_server.serve_forever()