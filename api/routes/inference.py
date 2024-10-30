from flask import Blueprint, request, jsonify
from models.personalized_ner import PersonalizedNER

bp = Blueprint('inference', __name__)
model = PersonalizedNER()

@bp.route('/inference', methods=['POST'])
def infer():
    data = request.json
    text = data['text']
    profile = data.get('profile')
    predictions = model.predict_with_profile(text, profile)
    return jsonify({'entities': predictions})
