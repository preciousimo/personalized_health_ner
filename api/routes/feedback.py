from flask import Blueprint, request, jsonify
from config.database import get_db

bp = Blueprint('feedback', __name__)

@bp.route('/feedback', methods=['POST'])
def collect_feedback():
    data = request.json
    user_id = data['user_id']
    feedback = data['feedback']
    # Store feedback in database
    return jsonify({'status': 'success'})
