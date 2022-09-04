from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
from Analyze.Predict import *

from apps import db
from apps.home.models import Analyzes

from collections import Counter

UPLOAD_FOLDER = 'uploads'


@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index')


@blueprint.route('/analyze')
@login_required
def analyze():
    filename = request.args.get('filename')
    # file = request.args.get('file')

    if filename is not None:
        print("--------->", filename)
    text = get_text_from_file(filename)

    model_op = ModelOperations(text)
    transactions = model_op.transactions
    result = model_op.predict()

    # Record the fields to the database
    store_analyze_data(filename=filename, result=result, transactions=transactions)

    return render_template('home/analyze.html', result=result)


def store_analyze_data(filename, transactions, result):
    columns = {'filename': filename, 'transactions': transactions, 'result': result,
               'userId': current_user.id}
    analyze = Analyzes(columns)
    db.session.add(analyze)
    db.session.commit()


def isfloat(num):
    try:
        for l in num:
            float(l)
    except ValueError:
        return False
    return True


def get_text_from_file(filename):
    file = UPLOAD_FOLDER + '/' + filename
    transactions = []
    with open(file, 'r', encoding="utf-8") as f:
        line = f.readline()
        transactions = line.split()
        if not isfloat(transactions):
            raise Exception("Content of the file must consist of numbers.")

        if not len(transactions) == 30:
            raise Exception("There must be 30 columns in the file.")

    return transactions


@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)
        analyzes = None
        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment, analyzes=analyzes,
                               current_user=current_user.username)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment

    except:
        return None
