def latest(scores):
    return scores[-1]
    pass

def personal_best(scores):
    return max(scores)
    pass

def personal_top_three(scores):
    return sorted((scores), reverse=True)[:3]
    pass
