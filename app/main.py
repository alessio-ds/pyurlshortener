from flask import Flask,render_template,request
from random import randint, shuffle
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        a=form_data
        link=a['Field1_name']
        if "http://" in link or 'https://' in link:
            pass
        else:
            link = "http://" + link

        lettere = 'abcdefghijklmnopqrstuvxywz'
        lm= lettere.upper()
        numeri='1234567890'
        tutto=lettere+lm+numeri
        tutto=list(tutto)
        shuffle(tutto)
        tutto=''.join(tutto)

        with open('app/main.py', 'r') as f:
            a=f.read()

        def gen():
            random_string = ''
            for _ in range(6):
                random_integer = randint(0, (len(tutto)))
                random_string += tutto[random_integer]
            return random_string

        random_string=gen()
        if random_string in a:
            while random_string in a:
                random_string=gen()

        with open('app/templates/short/'+random_string+'.html', mode='w') as f:
            f.write("<head><meta http-equiv='refresh' content='0; URL="+link+"'></head>")

        with open('app/main.py', 'a') as f:
            r2="'"+random_string+"'"
            f.write(

            '''
@app.route('/'+'''+r2+'''+'/')
def '''+random_string+'''():
    return render_template('short/'+'''+r2+'''+'.html')

            '''

            )
        with open('logs.txt', 'a') as f:
            f.write(random_string+' - '+link+'\n')

        port=5858
        sitoattuale=f'http://127.0.0.1:{port}'

        return render_template('form2.html')+f'The shortened url is: <br> <a href={sitoattuale}/'+random_string+'>'+sitoattuale+'/'+random_string+'</a><style type="text/css"></div>'



# GENERATI


@app.route('/'+'TadMWJ'+'/')
def TadMWJ():
    return render_template('short/'+'TadMWJ'+'.html')

            