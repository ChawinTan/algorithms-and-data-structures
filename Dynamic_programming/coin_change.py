'''
find the number of solutions to the coin change
'''

coins = [1,2,3]
coin_pos = len(coins)

'''
solution set includes a set with nth coin (change-coins[coin_pos])
and a set without nth coind (coin_pos - 1)
Recursive solution
'''
def coin_change(coins, coin_pos, change):

    if change == 0:
        return 1
    if change < 0:
        return 0
    if coin_pos <= 0 and n >= 1: #not enough coins to make change
        return 0
    return coin_change(coins, coin_pos-1, change) + coin_change(coins, coin_pos, change-coins[coin_pos-1])

''' Dynamic programming '''
coins = [1,2,3]
coin_pos = len(coins)

def coin_change(coins, coin_pos, change):

    table = [[0 for _ in range(coin_pos)] for _ in range(change+1)]

    for i in range(coin_pos):      #''' base case, when change = 0 '''
        table[0][i] = 1

    for curr_change in range(1, change+1):
        for coin in range(coin_pos):

            ''' solution including curr_coin '''
            have_Jth_coin = table[curr_change - coins[coin]][coin] if curr_change-coins[coin] >= 0 else 0

            ''' solution excluding curr_coin '''
            no_Jth_coin = table[curr_change][coin - 1] if coin >= 1 else 0

            ''' total count '''
            table[curr_change][coin] = have_Jth_coin + no_Jth_coin
    for i in range(len(table)):
        print(table[i])
    return table[change][coin_pos-1]

''' with one array '''
def coin_change(coins, coin_pos, change):

    value = [0 for _ in range(change+1)]

    value[0] = 1

    ''' at every value, we already found the number of possible combination with
        jth coin, hence we simply add the current combination to the lookback
        combination of value - coins

        Remeber!!! It's combinations!!!
    '''
    for coin in range(coin_pos):
        for curr_value in range(change+1):
            if curr_value >= coins[coin]:
                value[curr_value] += value[curr_value - coins[coin]]
    print(value)

coins = [1,2,5]
coin_pos = len(coins)
coin_change(coins, coin_pos, 12)
