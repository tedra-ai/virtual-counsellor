from flask import Flask, render_template, request
import random
import requests
import numpy as np
from dictionary import *
from bs4 import BeautifulSoup
from NeuralNetwork import _model, gradient_bias
app = Flask(__name__)


def search_google(query):
    results = []
    response = requests.get('https://www.google.co.in/search?q=' + query)
    soup = BeautifulSoup(response.text, "lxml")
    results = [item.text for item in soup.find_all('body') if len(item.text) > 50]  # li
    print(results)
    return results


class Chatbot:
    def __init__(self):
        self.notes = []
        self.binary_sentence = []
        self.gist = ''
        self.process = lambda w: [ps.stem(x.lower()) for x in word_tokenize(w)]
        self._model = _model
        self.course_bank = course_bank
        self.word_bank = word_bank
        self.responses = responses

    def search_bank(self, Category, bank):
	results = []
        for category in bank:
            for wrd in bank[category]:
                for word in [ps.stem(wrd.lower())]:
                    if process(word) in process(self.gist) and category == Category:
                        results.append(wrd)
        return results

    def detect_course(self):
	result = search_bank('course', word_bank)
        return result[-1]

    def detect_country(self):
        # returns the last county stated in the gist
        results = search_bank('country', word_bank)
        return ' in '+ results[-1]

    def suggest_courses(self):
	results = search_bank('course_interest', word_bank)
        query = 'best courses for '+ ', '.join(results)
        return self.search_google_results(query,'course')

    def search_google_results(self, query, key):
        suggestions = []
        institutions = search_google(query)
        for key_word in self.word_bank[key]:
            for institution in institutions:
                if key_word.lower() in institution.lower():
                    suggestions.append(key_word)
        return ', '.join(suggestions)

    def chat(self, sentence):
        self.gist += sentence + '. '
        binary_sentence = encode(sentence, self.word_bank)
        prediction =round(_model.predict(binary_sentence)[0] * gradient_bias)
        print(prediction)

        if prediction == 0:
            return random.choice(responses[0])
        # enquiry for institution of study
        elif prediction == 1:
            course = self.detect_course()
            country = self.detect_country()
            query = 'best university to study {} {}'.format(course, country)
            return random.choice(self.responses[1]) + self.search_google_results(query,
                                                                                                        'university')
        # enquiry for country of study
        elif prediction == 2:
            query = 'best countries to study' + self.detect_course()
            return random.choice(self.responses[2]) + self.search_google_results(query,
                                                                                                        'country')
        # enquiry for course to study
        elif prediction == 3:
            return random.choice(self.responses[3]) + self.suggest_courses()
        elif prediction == 5:
            return random.choice(self.responses[5])
        else:
            return random.choice(self.responses[4])


@app.route("/", methods=['POST', 'GET'])
def Chatter():
    API_endpoint = ''
    message = request.data()
    CB = Chatbot()
    reply = CB.chat(message['data'])
    requests.post(API_endpoint, data={'reply': reply})
    return reply


if __name__ == '__main__':
    app.run()
