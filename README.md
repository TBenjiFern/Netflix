# Overview

This is a simple data analysis program made to help me investigate the data provided to me by the following kaggle page.

[Netflix Subscription Fee Per Country](https://www.kaggle.com/datasets/prasertk/netflix-subscription-price-in-different-countries)

This page provides a dataset which contains a list of 65 countries around the world which have a netflix subscription. Along with each country name comes a total library size, the number of movies and series available, and the cost of each type of subscription (Basic, Standard, and Premium) available in each country. This is a fairly small set of data which I thought would be perfect for a beginner trying to get into data analysis using pandas.

As I mentioned above, I wrote this software to practice using data analysis libraries and tools such as pandas and matplotlib. I didn't want a very big database because working with large amount of data can be very overwhelming. In fact, prior to working on this project I didn't even want to consider working with data analysis because the thought of trying transform raw data to answer a specific question seemed too hard to attempt. To specifically combat this fear, I created this program to not only display the answers to my questions concerning the data set, but I made the program user friendly so that anybody could explore this data set and feel what data analysis really is. When this program is run, you will notice 10 options to run the data, most of which require the user to decide what columns he wants to investigate. I believe this approached helped me understand pandas and data analysis much better!

[Software Demo Video](https://youtu.be/SKnglQvMK18)

# Data Analysis Results

1. Does Netflix overcharge some countries compared to others?
* The answer is, Yes! Some countries are charged a LOT more than surrounding countries per subscription. In fact, an interesting anomaly I noticed was that the subscription upgrade price from Basic to Standard to Premium wasn't consistent either. Some countries started off with very fair to cheap Basic subscription fees but then were hit with a huge upgrade fee which other countries didn't have. In all, most countries in the same vicinity were charged the same rates, but there are extreme examples of overpaying and underpaying in this data set.

2. Do some countries have access to more media than others?
* Yes, some countries have access to WAY more media than other countries! It makes sense with trying to get rights to movies and all that some countries might not have access, or may have restricted access, to certain media from Netflix. Japan, for example, has free access to Japanese shows and movies which the United States can't access. Some other countries might have less restrictions on the type of media can be shown on public streaming platforms and can have more media than most other countries as well.

3. If so, does the price in subscription change to reflect this?
* Once again, the answer is yes! The interesting part about this, however, is that the subscription fee doesn't always change to reflect a difference in the amount of media available. In fact, the most overpriced country has a below-average amount of media that it can access. Turkey, on the other hand, is being charged the least per subscription (only $4 for a premium account and about $2 for a basic account) and they have an above-average amount of available media. My guess is that Netflix chooses to charge their users on another critera besides how many shows they might have access too. Perhaps location plays a role into how much Netflix charges or the type of licenses they have to obtain per country to stream certain shows.

Using this data set alone can't supply an answer as to why some countries are being treated differently compared to others, but we can clearly see that there are more than a few abnormalities between how Netflix charges one country compared to another. 


# Development Environment

* Visual Studio Code
* Python v. 3.9.5
* Pandas v. 1.4.1
* Matplotlib v. 3.5.1
* Pip v. 22.0.4
* Numpy v. 1.22.3


# Useful Websites

* [Pandas in 10 Minutes - Jump Start Guide](https://pandas.pydata.org/docs/user_guide/10min.html#min)
* [Pandas in Depth Tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
* [Pandas API Reference Sheets - DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
* [Matplotlib Main Website](https://matplotlib.org/)
* [Netflix Subscription Fee Per Country](https://www.kaggle.com/datasets/prasertk/netflix-subscription-price-in-different-countries)
* [Keggle for Free Data Sets](https://www.kaggle.com/)


# Future Work

* Change this project so that it's generalized for any data set and not hardcoded for the Netflix Subscription Fee csv
* Add more analysis options such as a pie chart, bar graphs, and other forms of scatter plots
* Rename all of the csv column names so that they are easier to type. Or, greate a gui for this program.