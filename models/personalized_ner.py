from models.bert_ner import BertNERModel
from config.database import get_db

class PersonalizedNER(BertNERModel):
    def __init__(self, model_name='bert-base-uncased', num_labels=5):
        super().__init__(model_name, num_labels)
        
    def predict_with_profile(self, text, user_profile):
        # Adjust model based on user_profile data
        modified_input = self._adjust_input(text, user_profile)
        return super().predict(modified_input)

    def _adjust_input(self, text, profile):
        # Logic for demographic-based input modification
        return text
