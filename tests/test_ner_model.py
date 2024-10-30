import unittest
from models.bert_ner import BertNERModel

class TestNERModel(unittest.TestCase):
    def test_prediction_shape(self):
        model = BertNERModel()
        text = "Patient has diabetes."
        output = model.predict(text)
        self.assertEqual(output.shape[0], len(text.split()))

if __name__ == "__main__":
    unittest.main()
