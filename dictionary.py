import numpy as np
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
word_bank = {
    'inquiry':
        ['analysis', 'where', 'what', 'examination', 'hearing', 'inspection', 'interrogation', 'investigation', 'probe',
         'query', 'ask', 'question', 'request', 'research', 'search', 'study', 'survey',
         'check', 'disquisition', 'explore', 'grilling', 'inquest', 'inquisition',
         'interrogatory', 'poll', 'pursuit', 'quest', 'Q and A', 'catechizing', 'delving', 'fishing expedition',
         'legwork', 'probing', 'quizzing', 'third degree', 'trial balloon'],
    'interest': ['interest', 'love', 'judge', 'like', 'study', 'learn', 'understand', 'facinated', 'enthusiasm'],
    'dislikes': ['issue', 'hate', 'dislike', ''],
    'greeting': ['hello', 'letter', 'nod', 'ovation', 'reception', 'salute', 'accosting', 'acknowledgment',
                 'address',
                 'aloha', 'compliments', 'hail', 'heralding', 'hi',
                 'how-do-you-do', 'howdy', 'regards', 'salaam', 'salutation',
                 'best wishes', 'compellation', 'good wishes',
                 "what's happening", 'hey'],
    'university': ['Harvard University', 'University of California–Berkeley', 'University of Chicago',
                   'University of Michigan', 'Columbia University', 'Yale University', 'Princeton University',
                   'Massachusetts Institute of Technology (MIT)', 'University of Cambridge',
                   'Stanford University',
                   'Oxford University', 'Cornell University', 'University of California–Los Angeles',
                   'University of Wisconsin–Madison', 'University of Toronto', 'University of Manchester',
                   'Duke University', 'New York University', 'Johns Hopkins University',
                   'University of Pennsylvania',
                   'University of Minnesota Twin Cities', 'University of California–San Diego',
                   'University of Paris (Sorbonne)', 'Northwestern University', 'McGill University',
                   'Hebrew University of Jerusalem', 'University of Washington',
                   'The University of Texas at Austin',
                   'University of British Columbia', 'King’s College London', 'University of Bristol',
                   'Rutgers University', 'London School of Economics',
                   'University of Illinois at Urbana-Champaign',
                   'University of Southern California', 'University of Edinburgh', 'Brown University',
                   'California Institute of Technology', 'University of Munich',
                   'University of North Carolina at Chapel Hill', 'Moscow State University',
                   'University College London', 'University of Vienna', 'University of Maryland',
                   'University of Pittsburgh', 'Pennsylvania State University',
                   'University of California–Irvine',
                   'Australian National University', 'Swarthmore College', 'University of Bonn',
                   'University of Birmingham', 'Boston University', 'University of Tübingen',
                   'University of Sussex',
                   'University of Warwick', 'University of Sheffield', 'University of Arizona',
                   'University of Virginia', 'University of Leeds', 'University of Rochester',
                   'University of Amsterdam', 'Heidelberg University', 'Syracuse University',
                   'University of Massachusetts–Amherst', 'University of Utah',
                   'Washington University in St Louis',
                   'Leiden University', 'Free University of Berlin', 'University of Notre Dame',
                   'Rice University',
                   'University of Oslo', 'Birkbeck, University of London', 'Utrecht University',
                   'Wesleyan University',
                   'City University of New York', 'Imperial College London', 'University of Göttingen',
                   'University of California–Davis', 'Dartmouth College', 'University of Sydney',
                   'National Autonomous University of Mexico', 'University of Buenos Aires',
                   'Goethe University Frankfurt', 'Ohio State University', 'University of Copenhagen',
                   'Arizona State University', 'University of Southampton', 'Florida State University',
                   'University of Calcutta', 'University of Georgia', 'The University of Tokyo',
                   'University of Melbourne', 'University of Florida', 'Brandeis University',
                   'Stockholm University',
                   'Vanderbilt University', 'Case Western Reserve University', 'University of Warsaw',
                   'University of Cologne', 'Michigan State University', 'University of Ibadan',
                   'University of Nigeria', 'Obafemi Awolowo University', 'Covenant University',
                   'Ahmadu Bello University', 'University of Lagos', 'Federal University of Technology Minna',
                   'University of Ilorin', 'University of Port Harcourt',
                   'Federal University of Technology Akure', '	Adekunle Ajasin University',
                   'Federal University of Technology Owerri',
                   'Lagos State University', 'University of Uyo', 'University of jos',
                   'Ladoke Akintola University of Technology',
                   'Ladoke Akintola University of Technology', 'Bayero University Kano',
                   'University of Calabar', 'Olabisi Onabanjo University (Ogun State University)',
                   'Rivers State University of Science & Technology', 'Nnamdi Azikiwe University',
                   'University of Abuja', 'University of Maiduguri',
                   'Usmanu Danfodiyo University', ' Ebonyi State University', 'American University of Nigeria',
                   'Abubakar Tafawa Balewa University',
                   'Michael Okpara University of Agriculture Umudike', 'Delta State University Nigeria',
                   'Federal University of Agriculture Makurdi', 'Federal University Oye Ekiti Ekiti State',
                   'Niger Delta University', 'Cross River State University of Science & Technology Calabar',
                   'Benue State University', 'Ekiti State University Ado Ekiti (University of Ado Ekiti)',
                   'Federal University of Petroleum Resources Effurun',
                   'Abia State University Uturu', 'Landmark University',
                   'African University of Science & Technology Abuja', 'Babcock University',
                   'Technical University Ibadan', 'Federal University Ndufu Alike Ikwo FUNAI',
                   'Osun State University', 'Ambrose Alli University Ekpoma', 'Redeemer’s University',
                   'Enugu State University of Science & Technology',
                   'Joseph Ayo Babalola University', 'Imo State University', 'Umaru Musa Yar’Adua University',
                   'Kwara State University', 'Federal University Dutsin Ma', 'Kogi State University',
                   'Bowen University', 'Lagos Business School Pan Atlantic University',
                   'Federal University Otuoke Bayelsa', 'Auchi Polytechnic',
                   'Federal University Dutse Jigawa State',
                   'Akwa Ibom State University of Technology', 'Nasarawa State University',
                   'Nigerian Defence Academy Kaduna', 'Yaba College of Technology',
                   'Modibbo Adama University of Technology Yola ', 'Pan African University Lagos',
                   'Edo State Polytechnic Usen', 'Edo University Iyamho', 'Lead City University Ibadan',
                   'Federal University Lokoja Kogi State', 'Adeleke University Ede',
                   'Tai Solarin University of Education', 'Ajayi Crowther University Oyo',
                   'Godfrey Okoye University', 'Kebbi State University',
                   'Rivers State College of Arts and Science', 'Igbinedion University',
                   'Ibrahim Badamasi Babangida University', 'Kaduna State University',
                   'Federal Polytechnic Ilaro',
                   'Chukwuemeka Odumegwu Ojukwu University', 'University of Medical Sciences Ondo',
                   'Taraba State University', 'Alvan Ikoku Federal College of Education',
                   'Al Hikmah University', 'Federal Polytechnic Ede', 'Benson Idahosa University',
                   'Ondo State University of Science & Technology', 'Federal University Lafia Nasarawa State',
                   'Elizade University', 'Bingham University', 'Bauchi State University',
                   'Nile University of Nigeria', 'Polytechnic Ibadan',
                   'Kano University of Science & Technology', 'Lagos State Polytechnic',
                   'Federal University Kashere', 'Federal University Wukari', 'Baze University',
                   'Yobe State University', 'Northwest University'
                                            'University of Benin', 'University of Agriculture Abeokuta'],
    'course': ['Computer Science', 'Accounting and Finance', 'Agriculture Science', 'Architecture',
               'Biochemistry',
               'Business Administration', 'Chemical and Petroleum Engineering', 'Civil Engineering',
               'Computer Engineering and Information Technology', 'Economics', 'Electrical Engineering',
               'Estate Management', 'Geology', 'Law', 'Mass Communication', 'Marketing',
               'Medical Laboratory Science',
               'Medicine', 'Nursing', 'Рharmacy', 'Theatre Arts', 'Archeology', 'Demography', 'Linguistics',
               'English', 'software engineering', 'music', 'art', 'Medicine',
               'Spanish'],
    'institution': ['University', 'Polytechnic', 'Collage', 'learning', 'institution'],
    'preference': ['private', 'public'],
    'country': ['France', 'Nigeria', 'Norway', 'Uganda', 'United States', 'Uganda', 'Australia',
                'United kingdom', 'Canada', 'Germany', 'Israel', 'China', 'Japan', 'Finland'],
    'course interest': ['computers', 'programming', 'electronics', 'machine learning',
                        'Artificial Interlligence', 'Problem solving', 'software', 'software engineering',
                        'computer science', 'data processing', 'design', 'data science', 'machine learning',
                        'building', 'electronics', 'drawing', 'painting', 'art', 'design', 'sketching', 'cooking',
                        'food', 'nutrition', 'animals',
                        'treat', 'vetenary', 'heal', 'treat', 'help', 'medicine', 'drugs', 'biology',
                        'chemistry', 'biology', 'drugs', 'biochemistry',
                        'english', 'statistics', 'budgeting', 'accounting', 'finance', 'reading', 'languages',
                        'writing',
                        'speaking', 'casting', 'music', 'listen', 'singing', 'beats', 'trance', 'human',
                        'human behaviour',
                        'animal behaviour', 'humans think', 'behaviour', 'industry', 'chemistry', 'manufacturing',
                        'mechanics',
                        'physics', 'engineering', 'industry', 'physics', 'manufacturing'],
    'question': ['?'],
    'exclamation': ['!'],
    'close': ['goodbye', 'adios', 'later', 'bye', 'thank you']}

responses = [['Greetings', 'Hey', 'Hello', 'Hi'], ['check out : ', 'look up : '],
             ['look up : '],
             ['you may be interested in ', 'you may like to study '], ['okay...', 'sorry'], ['Goodbye']]


process = lambda w: ' '.join([ps.stem(x.lower()) for x in word_tokenize(w)])

# Encode the 
def encode(sentence, word_dict=word_bank):
    categories = [_ for _ in word_dict]
    binary_sentence = [0 for _ in range(len(word_dict))]
    words = process(sentence)
    for category in word_dict:
        for word in [ps.stem(x.lower()) for x in word_dict[category]]:
            if process(word) in words and word not in ['']:
                binary_sentence[categories.index(category)] += 1
    return binary_sentence
