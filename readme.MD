Current progress on take home project:


Project currently uses Scrapy to extract metadata from Boston Celtics videos on their NBA page
and produce a csv file of the video info.


Next steps or things I would like to do going forward:

1. Currently, the project is able to scrape the page and get all the metadata in the logs, but the
resulting output CSV has only the same repeated entry.
2. The script currently only scrapes from the Celtics "Video" page instead of their entire "Video/Archive"
this is due to the metadata being easier to extract from this page the purposes of this time limited
assignment. Given more time I would more exhaustively research html of the Celtics videos across the
different pages of the website in order to see if I could extract more than just the basic info from
another source on the website.
3. Again due to the time limited nature of the assignment the project doesn't currently scroll through all
the videos across the entirety of the Celtics archive. Given more time the project would be able to page
through all the available videos and present a complete list of metadata for the teams videos.
4. It would also be beneficial to be able to write tests for the project in order to make sure that
the project is currently working as intended and returning what we want it to be returning.
5. Also, adapting the project to be able to scrape videos for other teams would be a hurdle as well.
Checking out the other teams' websites I found that they are all laid out slightly differently and
that the structure of the html for the other teams is also different. This would prove a challenge going
forward attempting to fit the tool to all the teams with their different sites and would require its own
set of researching and testing to incorporate this addition functionality.
6. Clean up and comment the code, again due to the time limited nature of the assignment the code itself is not as
neat and refined as it should were it to actually be incorporated into a functional project.