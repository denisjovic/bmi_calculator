from flask import Flask, render_template, request, url_for, flash

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    height = ''
    mass = ''
    bmi = ''
    status = ''
    if request.method == 'POST':
        height = request.form.get('height')
        mass = request.form.get('weight')
        bmi = round(int(mass) / ((int(height) / 100) ** 2),1)
        if 18.5 < bmi < 24.5:
            status = 'Healthy'
        elif bmi < 18.5:
            status = 'Thin'
        elif 25 < bmi < 30:
            status = 'Overweight'
        else:
            status = 'Obese'
    return render_template('index.html', bmi=bmi, status=status)


app.run()
