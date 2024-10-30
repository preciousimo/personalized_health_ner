from models.personalized_ner import PersonalizedNER
from data import feedback

def retrain_model():
    # Incorporate feedback into retraining
    model = PersonalizedNER()
    model.train()
