from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
# Sample dataset with question-answer pairs
with open('qa_d.json', 'r',encoding='UTF-8') as f:
    data = json.load(f)
dataset = data
# Extract the questions and answers
questions = [entry['Question'] for entry in dataset]
answers = [entry['Answer'] for entry in dataset]

# Initialize the TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Fit the model on the dataset questions
vectorizer.fit(questions)

# Function to get the most similar question from the dataset
def get_answer(user_question):
    # Vectorize the user's question
    user_question_vec = vectorizer.transform([user_question])
    
    # Calculate cosine similarity between the user's question and dataset questions
    similarities = cosine_similarity(user_question_vec, vectorizer.transform(questions))
    
    # Get the index of the most similar question
    most_similar_idx = similarities.argmax()
    
    # Return the answer corresponding to the most similar question
    return answers[most_similar_idx]

# # Chatbot loop
# while True:
#     question = input("Ask me something: ")
#     if question.lower() == 'exit':
#         print("Goodbye!")
#         break
#     answer = get_answer(question)
#     print(f"Answer: {answer}")
