from nltk.translate.meteor_score import meteor_score reference = ["this is a test"] 
candidate = "this is a trial" 
score = meteor_score(reference, candidate) 
print("METEOR Score:", score) 
