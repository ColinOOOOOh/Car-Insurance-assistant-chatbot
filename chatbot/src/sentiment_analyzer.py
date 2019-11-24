from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata
import pickle
import nltk
from nltk.classify import NaiveBayesClassifier
import os

import typing
from typing import Any, Optional, Text, Dict

SENTIMENT_MODEL_FILE_NAME = "sentiment_classifier.pkl"

class SentimentAnalyzer(Component):
    """A custom sentiment analysis component"""
    name = "sentiment"
    provides = ["entities"]
    requires = ["tokens", "text_features"]
    defaults = {}
    language_list = ["en"]
    print('initialised the class')

    def __init__(self, component_config=None):
        super(SentimentAnalyzer, self).__init__(component_config)

    def _train_model():
        X_train = [self._sentence_to_features(sent) for sent in df_train]
        y_train = [self._sentence_to_labels(sent) for sent in df_train]
        
    def train(self, training_data, cfg, **kwargs):
        """Load the sentiment polarity labels from the text
           file, retrieve training tokens and after formatting
           data train the classifier."""

        with open('data/sentiment_lables.md', 'r') as f:
            labels = f.read().splitlines()

        training_data = training_data.training_examples #list of Message objects
        tokens = [list(map(lambda x: x.text, t.get('tokens'))) for t in training_data]
        print(tokens)
        ##features = training_data.regex_features
        #print(features)
        word_list = []
        for e in tokens:
            word_list += e
        word_set = set(word_list)
        self.word_set = word_set
        processed_tokens = [self.preprocessing(t, word_set) for t in tokens]
        labeled_data = [[t, x] for t,x in zip(processed_tokens, labels)]
        self.clf_model = NaiveBayesClassifier.train(labeled_data)
        with open('/home/ubuntu/examples/knowledgebasebot/models.clf.pickle','wb')as f:
            pickle.dump(self.clf_model,f)
        #for t in  processed_tokens: 
        #    print(self.clf_model.prob_classify(t).max(), self.clf_model.prob_classify(t).prob(self.clf_model.prob_classify(t).max()))


    def convert_to_rasa(self, value, confidence):
        """Convert model output into the Rasa NLU compatible output format."""

        entity = {"value": value,
                  "confidence": confidence,
                  "entity": "sentiment",
                  "extractor": "sentiment_extractor"}

        return entity
        

    def preprocessing(self, tokens, word_set):
        """Create bag-of-words representation of the training examples."""
        
        return ({word: (word in tokens) for word in word_set})


    def process(self, message, **kwargs):
        """Retrieve the tokens of the new message, pass it to the classifier
            and append prediction results to the message class."""
        with open('/home/ubuntu/examples/knowledgebasebot/models.clf.pickle','rb') as f:
            clf_model = pickle.load(f)#
        entities = message.get("entities")
        print(entities)
        if not self.clf_model:
            # component is either not trained or didn't
            # receive enough training data
            entity = None
        else:
            tokens = [t.text for t in message.get("tokens")]
           # print("process: receive a new massage: ",tokens) 
            tb = self.preprocessing(tokens,self.word_set)
            #print(tb)
            pred = clf_model.prob_classify(tb)
            print("pred.max():", pred.max())
            for e in pred.samples():
                print(e, pred.prob(e))
            sentiment = pred.max()
            confidence = pred.prob(sentiment)
            entity = self.convert_to_rasa(sentiment, confidence)

            message.set("entities", [entity], add_to_output=True)


    def persist(self, file_name, model_dir):
        """Persist this model into the passed directory."""
        classifier_file = os.path.join(model_dir, SENTIMENT_MODEL_FILE_NAME)
        utils.json_pickle(classifier_file, self)
        return {"classifier_file": SENTIMENT_MODEL_FILE_NAME}

    @classmethod
    def load(cls,
             meta: Dict[Text, Any],
             model_dir=None,
             model_metadata=None,
             cached_component=None,
             **kwargs):
        file_name = meta.get("classifier_file")
        classifier_file = os.path.join(model_dir, file_name)
        return utils.json_unpickle(classifier_file)
