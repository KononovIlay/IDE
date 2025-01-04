import numpy as np

def random_predict(number : int = 1) -> int:
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
        
    return(count)

def score_game(random_predict) -> int:
    """за какое количество попыток в среднем угадывает наш подход 

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество угадыавний
    """
    count_lst = []
    np.random.seed(1)
    random_array = predict_number = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_lst.append(random_predict(number))
        
    score = int(np.mean(count_lst))
    print(f"ваш алгоритм угадывает число в среднем за: {score} попыток")
    return (score)

if __name__ == '__main__':
    score_game(random_predict)    
#print(f"кол-во попыток {random_predict(10)}")   