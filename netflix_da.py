import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def preset_pandas():
    # This helps pandas display all rows/columns in terminal
    # Otherwise, only 10 rows and several columns would display by default

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

def retrieve_database():
    # Convert csv file into a panda dataframe

    return pd.read_csv("netflix_country.csv")

def display_all(netflix_df):
    # Display all the data in the dataframe
    #.head(None) allows the data to display without withholding and data (shouldn't be necessary because of our presents)

    print(netflix_df.head(None))

def display_columns(netflix_df):
    # Displays all of the columns in a tuple

    print(netflix_df.columns)

def country_display(netflix_df):
    # Only displays a country which the user chooses along with it's data

    print("What country do you want to view? (\"Q\" To Exit)")
    while True:
        country_name = (input("> "))
        # Check to see if the user designated column name is a real column in the dataframe
        if (netflix_df["Country"] == country_name).any():
            # This is essentially a SQL query saying "Where country_name is found in netflix_df["Country"], return that row."   
            print(netflix_df[netflix_df["Country"] == country_name])
        elif country_name.upper() == "Q":
            break
        else:
            # Error handling
            print("That country isn't included in the database...")

def filtered_column(netflix_df):
    # Perform an inequality filter on any column and return those results

    while True:
        print("Choose a column to filter. (\"Q\" for Exit)")
        column_name = input("> ")
        if column_name.upper() == "Q":
            break
        else:
            # This is error handling to make sure a real column is chosen
            if column_name in netflix_df.columns:
                print("Choose operator: ")
                print("1. >")
                print("2. >=")
                print("3. <")
                print("4. <=")
                print("5. Quit")
                operator_choice = int(input("> "))
                # This seems a bit repetitive and could probably be simplified better
                if operator_choice == 1:
                    print("Choose an amount to filter by.")
                    filter_num = int(input("> "))
                    # This is basically a SQL query saying "Return the rows where netflix_df[column_name] is greater than filtered num".
                    print(netflix_df[netflix_df[column_name] > filter_num])
                elif operator_choice == 2:
                    print("Choose an amount to filter by.")
                    filter_num = int(input("> "))
                    print(netflix_df[netflix_df[column_name] >= filter_num])
                elif operator_choice == 3:
                    print("Choose an amount to filter by.")
                    filter_num = int(input("> "))
                    print(netflix_df[netflix_df[column_name] < filter_num])
                elif operator_choice == 4:
                    print("Choose an amount to filter by.")
                    filter_num = int(input("> "))
                    print(netflix_df[netflix_df[column_name] <= filter_num])
                elif operator_choice == 5:
                    break
                else:
                    print("Invalid command!")
            else:
                print("That column name isn't in the database...")

def top_ten(netflix_df):
    # This method will sort the data into descending order and display only the top ten results for the desired column

    print("What column do you want to see the top ten for? (\"Q\" for Exit)")
    while True:
        column_name = input("> ")
        if column_name.upper() == "Q":
            break
        else:
            # Error handling for column name
            if column_name in netflix_df.columns:
                # Retrieve the country names and the desired columns and save into separate data set
                data_set = netflix_df[["Country", column_name]]
                # Use the .sort_values() function to sort by a certain column in the data set. Set .head() to display only 10 rows
                print(data_set.sort_values(by=[column_name], ascending=False).head(10))
            else:
                print("That column name doesn't exist...")

def bottom_ten(netflix_df):
    # This method will sort the data into ascending order and display only the top ten results for the desired column

    print("What column do you want to see the bottom ten for? (\"Q\" for Exit)")
    while True:
        column_name = input("> ")
        if column_name.upper() == "Q":
            break
        else:
            # Error handling for column name
            if column_name in netflix_df.columns:
                data_set = netflix_df[["Country", column_name]]
                # Default settings are for sort_value to sort into ascending order
                print(data_set.sort_values(by=[column_name]).head(10))
            else:
                print("That column name doesn't exist...")

def display_prices(netflix_df):
    # This method will display all of the prices alongside their countries. 
    # Optionally can sort into ascending order by basic, standard, and premium prices (in that order)

    print("Do you want it sorted by price or not? (Y/N)")
    preference = input("> ")
    if preference.upper() == "Y":
        # Double bracket notation [[]] creates a subset of the dataframe which contains only the desired data. 
        print(netflix_df[["Country", "Cost Per Month - Basic ($)", "Cost Per Month - Standard ($)", "Cost Per Month - Premium ($)"]].sort_values(by=["Cost Per Month - Basic ($)", "Cost Per Month - Standard ($)", "Cost Per Month - Premium ($)"]))
    else:
        print(netflix_df[["Country", "Cost Per Month - Basic ($)", "Cost Per Month - Standard ($)", "Cost Per Month - Premium ($)"]])

def find_mean(netflix_df):
    # This method will return the mean/average of any column which has numeric data.
    # NOTE: This breaks if Country is chosen as column name

    print("Choose which column you'd like to find the mean (average) of. (\"Q\" for Exit)")
    while True:
        column_name = input("> ")
        if column_name.upper() == "Q":
            break
        else:
            # Error checking column name
            if column_name in netflix_df.columns:
                # Extract the desired column name from the dataframe
                column_series = netflix_df[column_name]
                # Use the .mean() function to get the mean of all of the rows in the extracted data
                print(column_series.mean())
            else:
                print("That column name doesn't exist...")

def access_scatter(netflix_df):
    # This method allows the user to create a scatter plot of any two columns they desire
    # The intended x-axis is "Country" while the y-axis can be any of the other columns

    while True:
        print("Please choose a column to represent the x-axis. (\"Q\" for Exit)")
        x_axis = input("> ")
        if x_axis.upper() == "Q":
            break
        # Error checking column name
        elif x_axis not in netflix_df.columns:
            print("That column doesn't exist...")
        else:
            print("Please choose a column to represent the y-axis. (\"Q\" for Exit)")
            y_axis = input("> ")
            if y_axis.upper() == "Q":
                break
            # Error checking column name
            elif y_axis not in netflix_df.columns:
                print("That column doesn't exist...")
            else:
                # Set the size of the figure
                plt.figure(figsize=(15,10))
                # Set the x-axis and y-axis and tell the plot to look at the netflix_df for the data
                plt.scatter(x_axis, y_axis , data=netflix_df)
                # Set the x-axis data's orientation
                plt.xticks(rotation=90)
                # Set labels
                plt.xlabel(x_axis)
                plt.ylabel(y_axis)
                # Cause graph to display
                plt.show()

def access_area_plot(netflix_df):
    # This method will allow the user to use the pandas built in area plot graph maker.
    # User has the option to have up to 3 columns compared against the Countries simultaneously.

    while True:
        print("How many columns do you want to compare against the \"Country\" x-axis?")
        print("1, 2, or 3? (Type 4 to quit)")
        column_num = int(input("> "))
        # Create if statements here to allow for one or more variable names to enter the plot.area()
        if column_num == 1:
            print("Input the name of the column you want to compare.")
            column_name_one = input("> ")
            # Error checking for column name
            if column_name_one in netflix_df.columns:
                # Create and save the plot.area() into a variable to plot.
                # Need to show how many columns in the y=, stacked makes the columns overlap, figsize is size of graph, rot makes the country names stand vertically,
                # and xticks lets all the countries show on the graph using the dataframe.index()
                area_graph = netflix_df.plot.area(x="Country", y=[column_name_one], stacked=False, figsize=(12,8), rot=90, xticks=netflix_df.index)
                # Plot the graph we just created
                area_graph.plot()
                # Use matplotlib to display the plotted graph
                plt.show()
            else:
                print("That's not a valid column name...")
        elif column_num == 2:
            print("Input the name of the first column you want to compare.")
            column_name_one = input("> ")
            print("Input the name of the second column you want to compare.")
            column_name_two = input("> ")
            if column_name_one in netflix_df.columns and column_name_two in netflix_df.columns:
                # Insert extra columns into the y=
                area_graph = netflix_df.plot.area(x="Country", y=[column_name_one, column_name_two], stacked=False, figsize=(12,8), rot=90, xticks=netflix_df.index)
                area_graph.plot()
                plt.show()
            else:
                print("One of those are not a valid column name...")
        elif column_num == 3:
            print("Input the name of the first column you want to compare.")
            column_name_one = input("> ")
            print("Input the name of the second column you want to compare.")
            column_name_two = input("> ")
            print("Input the name of the third column you want to compare.")
            column_name_three = input("> ")
            if column_name_one in netflix_df.columns and column_name_two in netflix_df.columns and column_name_three in netflix_df.columns:
                # Insert extra columns into the y=
                area_graph = netflix_df.plot.area(x="Country", y=[column_name_one, column_name_two, column_name_three], stacked=False, figsize=(12,8), rot=90, xticks=netflix_df.index)
                area_graph.plot()
                plt.show()
            else:
                print("One of those are not a valid column name...")
        elif column_num == 4:
            break
        else:
            print("That isn't a valid number...")

def main():
    # Main runs the whole program

    # Call the pandas presets to allow all the columns/rows to display
    preset_pandas()
    # For a better program, this would pass in a csv file name and withdraw any file
    # But that would also require generalizing the rest of the functions below so...ascii(obj)
    netflix_df = retrieve_database()
    print("Welcome to the Netflix Subscription Fee database explorer (2021)")
    # Loop here to allow the user to keep using the program until exited
    while True:
        print("\nPlease select one of the following commands: ")
        print("1. Display all database data.")
        print("2. Display all columns.")
        print("3. Display a specific country's data.")
        print("4. Filter certain column by certain amount.")
        print("5. Display top 10 per certain column.")
        print("6. Display bottom 10 per certain column.")
        print("7. Display each country and all three prices.")
        print("8. Find mean values of certain column.")
        print("9. Display data in scatter plot.")
        print("10. Display data in area plot (compare up to 3 columns together).")
        print("66. Exit program.")

        command = int(input("> "))
        if command == 1:
            display_all(netflix_df)
        elif command == 2:
            display_columns(netflix_df)
        elif command == 3:
            country_display(netflix_df)
        elif command == 4:
            filtered_column(netflix_df)
        elif command == 5:
            top_ten(netflix_df)
        elif command == 6:
            bottom_ten(netflix_df)
        elif command == 7:
            display_prices(netflix_df)
        elif command == 8:
            find_mean(netflix_df)
        elif command == 9:
            access_scatter(netflix_df)
        elif command == 10:
            access_area_plot(netflix_df)
        elif command == 66:
            break
        else:
            print("Invalid command...")
    print("Until Next Time...")
    print("Bye-bye!")

if __name__ == '__main__':
    # This allows the main() function to run when this file address is called

    main()