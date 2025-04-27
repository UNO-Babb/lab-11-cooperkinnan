def write_summary(totalShoppers, avgWait, avgShoppingTime, avgItems, maxWait, idleTime):
    summary = f"""
Summary of Grocery Store Simulation (SimPy Lab)

In this simulation, shoppers arrived every 2 minutes, selected between 5 and 20 random items,
and completed shopping based on a shopping speed of 2 items per minute. Checkers processed
10 items per minute with a minimum checkout time of 1 minute.

Simulation Results:
- Total shoppers served: {totalShoppers}
- Average wait time: {avgWait:.2f} minutes
- Average shopping time: {avgShoppingTime:.2f} minutes
- Average items purchased: {avgItems:.2f}
- Maximum wait time: {maxWait:.2f} minutes
- Total idle time across all checkers: {idleTime} minutes

Observations:
- More checkers greatly reduced wait times.
- Excess checkers led to more idle time.
- Customer arrival rates and random shopping times caused fluctuations in checkout congestion.

"""

    with open("summary.txt", "w") as file:
        file.write(summary.strip())

    print("\nSummary written to 'summary.txt'.")
