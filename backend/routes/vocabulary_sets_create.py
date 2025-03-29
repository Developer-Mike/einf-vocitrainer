from flask import jsonify

# TODO: Implement this route
def vocabulary_sets_create(user_id: int, user_role: str):
  """
  POST /api/vocabulary-sets/create

  **Response Format**
  .. code-block:: json
    {
      "id": 1,
      "label": "Vocabulary Set 1"
    }
  """
  return jsonify({
    "id": 1,
    "label": "Vocabulary Set 1"
  })