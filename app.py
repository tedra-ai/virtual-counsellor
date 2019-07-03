from flask import Flask, render_template, request
import random
import requests
import numpy as np
from dictionary import *
from bs4 import BeautifulSoup
from NeuralNetwork import _model, gradient_bias
app = Flask(__name__)

#search google for answers to suspected user enquiry
def search_google(query):
    response = requests.get('https://www.google.co.in/search?q=' + query)
    soup = BeautifulSoup(response.text, "lxml")
    results = [item.text for item in soup.find_all('body') if len(item.text) > 50]  # li
    return results

# Create the chatbot
class Chatbot:
    def __init__(self):
        self.binary_sentence = []
        self.gist = ''
	self.exit_code = 0 # Tells if the bot is ready to exit, after exit, gist is wiped.
        self._model = _model # Bot's main model
        self.course_bank = course_bank # intended for bot's second neural network; aborted for lack of training data
        self.word_bank = word_bank # word bank for bot's main neural network
        self.responses = responses # bot's responses

    # search word bank for words of interest
    def search_bank(self, Category, bank):
	results = []
        for category in bank:
            for wrd in bank[category]:
                for word in [ps.stem(wrd.lower())]:
                    if process(word) in process(self.gist) and category == Category:
                        results.append(wrd)
        return results

    # returns the last concluded course in the course
    def detect_course(self):
	result = search_bank('course', word_bank)
        return result[-1]

    def detect_country(self):
        # returns the last concluded county in the gist
        results = search_bank('country', word_bank)
        return ' in '+ results[-1]
    
    #suggests a course from the word bank according to users interest 
    def suggest_courses(self):
	results = search_bank('course_interest', word_bank)
        query = 'best courses for '+ ', '.join(results)
        return self.search_google_results(query,'course')

    # Search google results for words of interest
    def search_google_results(self, query, key):
        suggestions = []
        institutions = search_google(query)
        for key_word in self.word_bank[key]:
            for institution in institutions:
                if key_word.lower() in institution.lower():
                    suggestions.append(key_word)
        return ', '.join(suggestions)
    # Chat
    def chat(self, sentence):
	# add sentence to gist
        self.gist += sentence + '. '
	# encode sentence and predict encoded sentence
        binary_sentence = encode(sentence, self.word_bank)
        prediction =round(_model.predict(binary_sentence)[0] * gradient_bias)
	
        # if prediction is an enquiry for institution of study
        if prediction == 1:
            course = self.detect_course()
            country = self.detect_country()
            query = 'best university to study {} {}'.format(course, country)
            return random.choice(self.responses[1]) + self.search_google_results(query,
                                                                                                        'university')
        # if prediction is an enquiry for country of study
        elif prediction == 2:
            query = 'best countries to study' + self.detect_course()
            return random.choice(self.responses[2]) + self.search_google_results(query,
                                                                                                        'country')
        # if prediction is an enquiry for course to study
        elif prediction == 3:
            return random.choice(self.responses[3]) + self.suggest_courses()
	# greetings or ununderstood meassag
	
        else:
            return random.choice(self.responses[prediction])


# Main flask app
@app.route("/", methods=['POST', 'GET'])
def Chatter():
    while True:
        API_endpoint = ''
        message = request.data()
        CB = Chatbot()
        reply = CB.chat(message['data'])
        requests.post(API_endpoint, data={'reply': reply})
        if CB.exit_code:
		break


if __name__ == '__main__':
app.run()
