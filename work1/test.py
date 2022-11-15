from datetime import datetime
import random
import sys

## формирование данных
# data = []
# for _ in range(1000000):
#     data.append([random.randint(1, 10000), random.randint(1, 500), random.randint(16680863160, 16684463160)/10])
#
# columns = ['customer_id', 'product_id', 'timestamp']
#
# df = pd.DataFrame(data, columns=columns)
# df.to_csv('test.csv', index=False)


# решение
import pandas as pd

def add_session(df, len_session):
    
    def get_sessions(data):
        first = 1

        def get_one_session(data):
            nonlocal first
            if data:
                first += 1
            return first

        return data.apply(get_one_session)

    df = df.sort_values(['customer_id', 'timestamp'])
    df['session_diff'] = df['timestamp'].diff() > len_session
    index_first_session = df[['customer_id', 'timestamp']].groupby('customer_id').agg({'timestamp': 'idxmin'})[
        'timestamp']
    df.loc[index_first_session.values, 'session_diff'] = False
    session = df.groupby('customer_id')['session_diff'].transform(get_sessions)
    df['session_id'] = 1
    df['session_id'] = session
    df.drop('session_diff', axis=1, inplace=True)

    return df



if __name__ == "__main__":
    if len(sys.argv) == 4:
        df = pd.read_csv(sys.argv[1])
        df = add_session(df, int(sys.argv[3]))
        df.to_csv(sys.argv[2], index=False)