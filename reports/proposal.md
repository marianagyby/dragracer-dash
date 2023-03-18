# Motivation and purpose

The motivation behind designing the dragracer-dash app is to provide a tool that can help fans of RuPaul's Drag Race to easily explore the backgrounds of drag queens on the show, across all seasons and episodes. 

For more context: <br>
**What is RuPaul's Drag Race and What is our purpose for designing this app?** <br>
It is a reality TV show that originated in the US, where drag queens compete to become America's Next Drag Superstar. The show is hosted by drag queen RuPaul, who is a cultural icon and is widely regarded as one of the most influential drag queens in the world. The show has gained a huge following since its debut in 2009 and has since spawned numerous spin-off shows and international versions.

On the show, contestants compete in various challenges, such as acting, singing, and fashion design, with the aim of impressing the judges and avoiding elimination. The contestants are judged based on their performances, runway looks, and overall charisma, uniqueness, nerve, and talent (or "C-U-N-T," as it's known on the show). The contestants also participate in lip-sync battles, where the bottom two performers lip-sync for their lives, with one being eliminated from the competition.

The show has gained a reputation for promoting inclusivity, diversity, and acceptance, with a large and loyal fan base across the world. The show has also helped to raise awareness of the drag community and has provided a platform for drag queens to showcase their talent and artistry to a wider audience. 

**Our Purpose:**<br>
With a large number of drag queens and seasons, it can be difficult for fans to keep track of each queen's performance and progress. The purpose of the app is to provide an interactive and user-friendly platform for fans to answer their research questions and make informed decisions on which drag queens to follow or see in live performances.

# Description of the data

This dashboard will visualize data on about 184 drag queens that have appeared on RuPaul's Drag Race over 14 seasons. We will be using the {dragracer} R package, which provides the following three data sets: `rpdr_contestants`, with contestant-level data, `rpdr_contep`, with contestant and episode level data, and `rpdr_ep` with episode-level data. This package has been developed by web-scraping [the wiki for the show](https://rupaulsdragrace.fandom.com/wiki/RuPaul%27s_Drag_Race_Wiki), and is available on CRAN with installation instructions [here](https://cran.r-project.org/web/packages/dragracer/readme/README.html). We will be joining these three data sets into one dataframe containing the main variables of interest. 

The final dataframe, called `drag`, will include variables that describe general information on the queens (`contestant`, `age`, `dob`), and the season they appeared on (`season`). An additional feature will also be derived from the data that will indicate the queens' astrological sign (`astrology_sign`) based on their date of birth. These features will be used to filter the data and display distributions of age and signs.

*Note: The [data](https://github.com/marianagyby/dragracer-dash/tree/main/data) used in this `dragracer-dash` repository is sourced from the `dragracerviz` repository [data](https://github.com/UBC-MDS/dragracerviz/tree/main/data), which has already been preprocessed as a part of the group project.*

# Research questions and usage scenarios

## Research questions

Possible research questions that can be answered by this visualization are as follows:

1.  What is the most common age of the queens appearing on the show?

2.  What is the most rare astrology sign of the queens appearing in the last season?

## Usage scenario

James is a frequent watcher of RuPaul's Drag Race. He has seen every season of the American franchise, and he's interested in learning more about the backgrounds of the contestants that appear on the show. He's curious about the typical ages and astrological signs of the queens. Are they typically older or younger? Are there more Cancers or Leos? How have these numbers changed over the seasons? James wants to find answers to these pressing questions, but does not have time to do the required research. The visualization app dragracer-dash can help James with his problem. This app allows him to select any number of seasons and an age range that he is interested in. Based on his selections, one plot will show the age distribution of the filtered  queens, allowing him to see the most and least common ages, and a second plot will show the number of queens that fall into each astrological sign category. Now, James can get to know the stars of the show a little better.
