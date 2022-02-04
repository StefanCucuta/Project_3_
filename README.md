**BATTLESHIP GAME**

***GAME RULES***

Battleship is a strategy type guessing game for two players. It is played on ruled grids (paper or board) on which each player's fleet of ships (including battleships) are marked. The locations of the fleets are concealed from the other player. Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

![](IMAGE OF THE GAME )

**[Live DEMO]( )**


# Table of Contents <a name='contents'></a>

* [User Experience (UX)](#userexperience)
* [Design](#design)
* [Development](#development)
* [Testing](#testing)
* [Deployment](#deployment)
* [Technologies Used](#tech)
* [Credits](#credits)


## User Experience (UX) <a name='userexperience'></a>

- **User Stories**

    *The game works with the assumption that the user is already aware of the classic game: Battleships.*

    + **First Time Visitor Goals**
    
        A. Welcome the User.

        B. Highlight to the user key aspects of the game play layout.

        C. Encouraged them to enter them desire captain name.

    + **Returning Visitor Goals**

        A. Begin testing the limits of the user input during game play.  

        B. Become familiar with the game layout.

        C. Attempt to beat the computer.

    + **Frequent Visitor Goals**

        A. Explore different styles of game play.

        B. Develop individual tactics for game play.

- **Research**

    *My research for the project consisted of browsing other developers battleship game based creations. With the intent of learning the common problems faced and the display choices they made.*

[Return to Table of Contents](#contents)


## Design <a name='design'></a>

- **Colour Scheme**

    *Not required for this project.*

- **Typography**

    *I chose to capitalize all text on the project to create consistency in size throughout.*

- **Imagery**

    *Special attention to the board display during game play was required to ensure for suitable contrast between the different markers. [The Ascii Code](https://theasciicode.com.ar/) website was used to explore my options regarding ASCII characters and boat image for the beagining of the game.*

    ![legend image](IMAGE WITH THE BOAT AT THE BEAGING OF THE GAME) 


[Return to Table of Contents](#contents)

## Development <a name='development'></a>

*Initial development was to create a flow diagram using [LucidChart](https://www.lucidchart.com/pages/) so i could begin exploring how the requirements for my game and their dependencies would work together.

![The flow diagram](/assets/images/pro.jpeg)

*For each valid turn, game end conditions must be checked and if reached, the turn sequence must be broken out of and the game end logic run.


![Wire frame](/assets/images/Wireframe.png)

[Return to Table of Contents](#contents)

## Testing <a name ='testing'></a>  

-  Due to the nature of the project testing has been conducted throughout its entirety, mainly through the use of running the program in the terminal and ensuring i get the output intended. Evidence of this is clear within my commits, with various debugs recorded. 

-  Various sections of code where also developed in isolation and outputs checked before being inserted into the running order as the size of the project grew.  


- **Validator Testing**

    - HTML
        - Not within project scope.

    - CSS
        - Not within project scope.

    - JS
        - Not within project scope.

    - Python
        - No errors were found when passing through the [PEP8 Validator tool](http://pep8online.com/)

- **Lighthouse**

    - Not within project scope.

[Return to Table of Contents](#contents)

## Deployment <a name ='deployment'></a>

- The site is deployed via Heroku. The steps to deploy are as follows:

    *Ensure the requirements for the project are added to the requirements.txt file prior to deployment*

    1: From the dashboard, select New and then Create new app.
    
    2: Enter an individual app name into the text box, select a region from the dropdown and then press Create app.
    
    3: A Heroku app has now been created and the Deploy tab is opened.
    
    4: Select the Settings tab.
    
    5: If required, click on the Reveal Config Vars button and add.
    
    6: In the Buildpacks section of the settings tab, click on Add Buildpack, select Python and then save changes.
    
    7: Click on Add Buildpack again, select node.js and then save changes.

    *When they are on the dashboard, ensure that python is above node.js on the list*
    
    8: Open the Deploy tab.
    
    9: In the deployment method section, select GitHub and confirm the connection.
    
    10: Enter the repo-name into the text box. When the correct repo appears, click Connect.
    
    11: If desired, in the Automatic deploys section, click Enable Automatic Deploys.

    *This then updates the deployment every time GitHub code is pushed.*
    
    12: To complete the process click on the Deploy Brach button in the Manual deploy section. 
        
    *This will take a few seconds to complete while Heroku builds the app.*
    
    13: A message will appear informing you that the app was successfully deployed and a View button will bring you to the live site.

The live link can be found here - [BATTLESHIPS]()

[Return to Table of Contents](#contents)
