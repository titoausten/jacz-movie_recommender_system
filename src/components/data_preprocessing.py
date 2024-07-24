from src import logger
from src.utils.common import load_data
from src.entity.config_entity import DataPreprocessingConfig
import contractions
import re
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords


class DataPreprocessing:
    def __init__(self, config: DataPreprocessingConfig):
        self.config = config
        self.file = self.config.source_data_path
        self.df = load_data(self.file)


    def create_new_dataframe(self):
        # Create new dataframe with relevant data
        self.df = self.df[[
            self.config.important_feature,
            self.config.important_feature1,
            self.config.important_feature2,
            self.config.important_feature3
            ]]
        
        # self.df[self.config.important_feature2].fillna('', inplace=True)
        self.df[self.config.important_feature2] = self.df[self.config.important_feature2].fillna('')
        #  Drop rows with NaN values
        self.df.dropna(inplace=True)
        return self.df
        

    def create_feature(self):      
        # Create a new feature
        print(f"Creating feature ({self.config.new_feature}) from ({self.config.important_feature2}) and ({self.config.important_feature3})")
        self.df[self.config.new_feature] = self.df[self.config.important_feature2].map(str) + ' ' + self.df[self.config.important_feature3]
        logger.info(f"Feature ({self.config.new_feature}) created")
        return self.df
        

    def preprocess_data(self, document):
        # Remove non-alphanumeric characters, strip whitespace, and convert to lowercase
        document = re.sub(r'[^a-zA-Z0-9\s]', '', document)
        document = document.lower()
        document = document.strip()
        # Fixing contractions e.g don't, won't etc.
        document = contractions.fix(document)
        # tokenize document
        tokens = word_tokenize(document)
        # filter stopwords out of document
        stop_words = stopwords.words('english')
        filtered_tokens = [token for token in tokens if token not in stop_words]
        # re-create document from filtered tokens
        document = ' '.join(filtered_tokens)
        return document
