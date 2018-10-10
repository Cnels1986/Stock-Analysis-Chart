1. Discovery/Requirements:
  I am collecting information on 5 different stocks for an investor to create some sort of
  chart or graph to help them determine which stock to invest in. Based on the results I'm
  suppose to choose the best stock for the investor.

2. Collection:
  Using the alphavantage.co API, I am going to collect stock information on 5 different
  car companies over the last couple years.

3. Data prep/Cleaning:
  Data retrieved using the API, only need the date and the closing amount for that month

4. Exploration/Planning:
  With the data retrieved, the plan is to create a line chart, where each point will
  be the closing amount for each month. Will not be using the last 20 years though, maybe 3-5

5. Modeling/Algorithms:
  https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html#sphx-glr-gallery-lines-bars-and-markers-simple-plot-py
  This is the example that will be recreated for each of the 5 stock prices I will be
  comparing

6. Automation/Computation:
  After parsing the data to get the date as well as the high for that month, the points
  were plotted using matplotlib and a .png file was saved for each.

7. Findings/Review/Repeat:
  The results for Mazda seemed to be incorrect, switched to GM instead which provided a
  better chart
