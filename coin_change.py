import math

COINS = [1, 10, 25, 21, 33]
AMOUNT = 257669

def min_coins(coins, amount = 0):
    if len(coins) < 1:
        return 'Need an input list of coins'
    # Get max coins value
    max_coin = max(coins)
    # Get product of all coins:
    worst_lcm = math.prod(coins)
    lcm = worst_lcm

    # Find lowest common multiple: LCM (to know after which amount we should always use highest coin)
    for cm in range(max_coin, worst_lcm + 1, max_coin):
        lcm_found = True
        for coin in coins:
            if cm % coin != 0:
                lcm_found = False
                break
        if lcm_found:
            lcm = cm
            break

    # If amount is larger (or equal) to lcm, use max_coin until it is lower.
    # This is to reduce the need for calculating every number up to amount
    add_coins = 0
    while amount >= lcm:
        add_coins += 1
        amount -= max_coin

    # Initiate min_coins_arr to high value
    min_coins_arr = [amount + 1] * (amount + 1)
    # Set amount of coins needed for '0' to be zero coins
    min_coins_arr[0] = 0

    # Loop over all amounts and calculate nr of coins needed to reach the amount
    for sought_amount in range(1, amount + 1):
        # Loop over all available coins
        for coin in coins:
            # If, when subtracting coin, remaining amount is less than zero then coin is not valid to use
            if sought_amount - coin < 0:
                continue
            # For given coin check if current nr of coins needed to reach amount can be reduce by checking current value against 1 + coins needed for: amount - coin
            min_coins_arr[sought_amount] = min(1 + min_coins_arr[sought_amount - coin], min_coins_arr[sought_amount])

    result = min_coins_arr[-1]

    # If result > amount then no combination works so return '-1'.
    if result > amount: return 'Not possible to provide requested amount'
    return result + add_coins

print(min_coins(COINS, AMOUNT))
