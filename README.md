# dragracer-dash

This dashboard is hosted on `Render`, and can be found [here](https://dragracer-dashboard.onrender.com/).

## Motivation

The dragracer-dash app is designed to help fans of RuPaul's Drag Race explore the backgrounds of drag queens on the show, across all seasons. The dragracer-dash app provides an easy-to-use interface for fans of RuPaul's Drag Race to explore data on the show's contestants and answer research questions such as the most common age and rarest astrological sign of the queens.

To read more, see the [proposal](https://github.com/marianagyby/dragracer-dash/blob/main/reports/proposal.md).

## Usage

To open the app, [click here!](https://dragracer-dashboard.onrender.com/)

When the user opens the app, they will see a short description of the app and the age distribution of all contestants over the history of the show. The user can then select the seasons of interest using a drop-down menu. They can also filter the data by age range using a slider.

Based on these selections, the dashboard will display two updated plots. The first plot will show the age distribution of the queens in the selected seasons and age range. The plot will include a histogram to show the most and least common ages of the queens.

The second plot will show the number of queens in each astrological sign category. This plot will be a bar chart that displays the frequency of each sign in the selected seasons and age range.

The user can explore these visualizations with one or multiple seasons at a time!

## References

The data used in this repository is sourced from [RuPaul's Drag Race wiki](https://rupaulsdragrace.fandom.com/wiki/RuPaul%27s_Drag_Race_Wiki), made available for installation on [CRAN](https://cran.r-project.org/web/packages/dragracer/readme/README.html), and preprocessed in the `dragracerviz` [repository](https://github.com/UBC-MDS/dragracerviz/tree/main/data).
