
def knapsack(parcels, capacity):

    n = len(parcels)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):

        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["value"]

        for w in range(capacity + 1):

            # If parcel weight is greater than capacity
            if weight > w:
                dp[i][w] = dp[i - 1][w]

            else:
                # Maximum of including or excluding parcel
                include = value + dp[i - 1][w - weight]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

    # Find selected parcels
    selected_parcels = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            parcel = parcels[i - 1]
            selected_parcels.append(parcel)

            w -= parcel["weight"]

    selected_parcels.reverse()

    total_weight = sum(p["weight"] for p in selected_parcels)
    total_value = sum(p["value"] for p in selected_parcels)

    return selected_parcels, total_weight, total_value, dp
