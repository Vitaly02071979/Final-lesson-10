import random 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# 1 
data.loc[data['whoAmI'] == 'human', 'human'] = '1'
data.loc[data['whoAmI'] == 'robot', 'robot'] = '1'
data.head()

# 2
lst = ['robot'] * 10
lst += ['human'] * 10
lst += ['kiborg'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

# 3 
data.loc[data['whoAmI'] == 'human', 'human'] = '1'
data.loc[data['whoAmI'] == 'human', 'human'] = '0'
data.loc[data['whoAmI'] == 'robot', 'robot'] = '1'
data.loc[data['whoAmI'] == 'human', 'robot'] = '0'
data.head()
