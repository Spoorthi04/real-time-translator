from sklearn.model_selection import KFold import numpy as np 
kf = KFold(n_splits=5, shuffle=True, random_state=42) bleu_scores = [] 
for train_index, test_index in kf.split(text_data): 
	 train_texts, test_texts = text_data[train_index], text_data[test_index] 
 

 model = train_nmt_model(train_texts)  # Custom function to train NMT 		 bleu_score = evaluate_nmt_model(model, test_texts)  # Custom 	function          to evaluate NMT 
 bleu_scores.append(bleu_score) 
 print("Average BLEU Score:", np.mean(bleu_scores)) 
