def compute_pareto_optimal(df):
    optimal = set()
    potentialy_pareto_optimal = set(df.index)


    while potentialy_pareto_optimal:

        potential = potentialy_pareto_optimal.pop()

        temp = (df.loc[potentialy_pareto_optimal.union(optimal)] > df.loc[potential])

        dominates = temp.all(axis=1)
        
        if not (~temp).all(axis=1).any():
            optimal.add(potential)

        potentialy_pareto_optimal -= set(dominates[dominates].index)
    
    return df.index.isin(optimal)
