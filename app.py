# -*- coding: utf-8 -*-

import json

from chalice import Chalice
from chalice import Chalice, Response, BadRequestError

from yake.highlight import TextHighlighter
import yake

app = Chalice(app_name='yake-lambda-api')

@app.route('/')
def index():
    return {'hello': 'Yake!'}

@app.route('/yake/extract_keywords', methods=['POST'])
def extract_keywords():

    try:

        #instantiate Yake
        _yake = yake.KeywordExtractor()
        
        # This is the JSON body the user sent in their POST request.
        _input = app.current_request.json_body
        
        # get attribute 'text' from input json
        text = _input["text"]

        #default
        _max_ngram_size = 3
        
        if hasattr(_input, "max_ngram_size"):
            _max_ngram_size = int(_input["max_ngram_size"])
            _yake.n = _max_ngram_size

        if hasattr(_input, "language"):
            _lan = _input["language"]
            _yake.lan = _lan
        
        # extract keywords using yake
        keywords = _yake.extract_keywords(text)

        _th = TextHighlighter(max_ngram_size = _max_ngram_size)
        highlight_text = _th.highlight(text, keywords)

        response_json = json.dumps({
                                    "keywords":keywords, 
                                    "highlight":highlight_text
                                    })

        return Response(status_code=200, 
                        body=response_json,
                        headers={'Content-Type': 'application/json'})
    except:
        raise BadRequestError('Failed to execute keyword extraction. Please check if input is valid')

