# BudgetApp
The Category class in budget.py instantiates objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class also has an instance variable called ledger that is a list. 
The class contains the following methods:
- A deposit method that accepts an amount and description. If no description is given, it defaults to an empty string. The method appends an object to the ledger list in the form of {"amount": amount, "description": description}.
- A withdraw method that is similar to the deposit method, but the amount passed is stored in the ledger as a negative number. If there are not enough funds, nothing is added to the ledger. This method returns True if the withdrawal took place, and False otherwise.
- A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
- A transfer method that accepts an amount and another budget category as arguments. The method adds a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method then adds a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing is added to either ledgers. This method returns True if the transfer took place, and False otherwise.
- A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method is used by both the withdraw method and transfer method.

When the budget object is printed it will display:
- A title line of 30 characters where the name of the category is centered in a line of * characters.
- A list of the items in the ledger. Each line shows the description and amount. The first 23 characters of the description is displayed, then the amount. The amount is right aligned, contain two decimal places, and display a maximum of 7 characters.
- A line displaying the category total.

Besides the Category class, the function (outside of the class) called create_spend_chart takes a list of categories as an argument. It returns a string that is a bar chart.

The chart shows the percentage spent in each category passed in to the function. The percentage spent is calculated only with withdrawals and not with deposits. Down the left side of the chart are labels 0 - 100. The "bars" in the bar chart is made out of the "o" character. The height of each bar is rounded down to the nearest 10. The horizontal line below the bars goes two spaces past the final bar. Each category name is written vertically below the bar. There is a title at the top that says "Percentage spent by category".
