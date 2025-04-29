def min_coins(coin_values, k):

    dp = [float('inf') for _ in range(k + 1)]
    dp[0] = 0
    
    for amount in range(1, k + 1):
        for coin in coin_values:
            if coin <= amount and dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    if dp[k] != float('inf'):
        return dp[k]
    else:
        return -1

# Example usage
if __name__ == "__main__":
    # Example: Coins with values [1, 5, 10, 25] (like US cents)
    coins = [1, 5, 10, 25]
    amount = 46
    
    result = min_coins(coins, amount)
    print(f"Minimum coins needed for {amount} dollars: {result}")
    # Output: Minimum coins needed for 42 dollars: 6 (1 quarter, 1 dime, 1 nickel, 2 pennies)`