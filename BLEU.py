from nltk.translate.bleu_score import sentence_bleu
reference = [["this", "is", "a", "test"]]
candidate = ["this", "is", "a", "trial"]
score = sentence_bleu(reference, candidate) 
print("BLEU Score:", score) 
