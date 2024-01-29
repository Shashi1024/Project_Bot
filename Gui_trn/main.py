import json
from difflib import get_close_matches

def load_K_Base(file_path:str) -> dict:
    with open(file_path,'r') as file:
        data: dict = json.load(file)
    return data

def save_K_Base(file_path: str, data: dict):
    with open(file_path,'w') as file:
        json.dump(data, file, indent = 2)

def find_bM(userQ : str, questions: list[str]) -> str| None:
    matches: list = get_close_matches(userQ, questions, n=1, cutoff = 0.6)
    return matches[0] if matches else None

def get_Ans(question : str, k_Base: dict) -> str | None:
    for q in k_Base["questions"]:
        if q['question'] == question:
            return q["answer"]
    
def C_bot():
    K_Base: dict = load_K_Base("Gui_trn/K_Base.json")

    while True:
        usIn : str = input('You: ')

        if usIn.lower() == quit:
            break

        b_M : str|None = find_bM(usIn,[q['question'] for q in K_Base['questions']])

        if b_M:
            answer : str = get_Ans(b_M, K_Base)
            print(f'Bot: {answer}')
        else:
            print("I dont Know the answer. Can you teach me ?")
            new_ans : str = input('Type the answer or "skip" to skip: ')
            
            if new_ans.lower() != 'skip':
                K_Base["questions"].append({"question": usIn, "answer": new_ans})
                save_K_Base('Gui_trn/K_Base.json',K_Base)
                print('Bot: Thank you i learnt a new response.')



if __name__ == '__main__':
    C_bot()