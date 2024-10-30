from transformers import BertTokenizerFast, BertForTokenClassification
import torch

class BertNERModel:
    def __init__(self, model_name='bert-base-uncased', num_labels=5):
        self.tokenizer = BertTokenizerFast.from_pretrained(model_name)
        self.model = BertForTokenClassification.from_pretrained(model_name, num_labels=num_labels)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs)
        return torch.argmax(outputs.logits, dim=2)
