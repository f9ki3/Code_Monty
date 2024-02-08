from flask import Flask, render_template
import data
app = Flask(__name__)


@app.route ('/')
def home():
    return render_template('base.html', about_dev=data.about_dev, about_codemonty=data.about_codemonty, banner1=data.banner1, banner2=data.banner2, table_of_content=data.table_of_content, what_is_codemonty=data.what_is_codemonty)

