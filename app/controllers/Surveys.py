from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)

        self.load_model('Survey')
   
    def index(self):
        if not 'counter' in session:
            session['counter'] = 0
        return self.load_view('index.html')

    def process(self):
        session['counter'] += 1
        data = {
            'name': request.form['name'],
            'language': request.form['lang'],
            'comment': request.form['comment']
        }
        self.models['Survey'].add_survey(data)
        return redirect('/result')

    def result(self):
        data = self.models['Survey'].get_surveys()
        return self.load_view('result.html', surveys=data, counter=session['counter'])

    def magic_method(self):
        print 'You found the secret method!'
        return redirect('/')