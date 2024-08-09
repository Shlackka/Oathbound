# Oathbound

A link to the deployed app is **[here](https://oathbound-53135a23d9e9.herokuapp.com/)**.

Guess the God is an engaging and educational quiz where players are presented with images of gods from various mythologies. The objective is to correctly identify which pantheon each god belongs to Greek, Norse, Egyptian, or Aztec. This fun and interactive game helps players familiarize themselves with the distinctive visual characteristics and attributes of deities from different cultures. Perfect for mythology enthusiasts and curious learners alike, this quiz offers a visual and entertaining way to deepen your knowledge of ancient pantheons.

## Responsive Mockup

  - This mockup image was made using **[Techsini Multi Device Mockup Generator](https://techsini.com/multi-mockup/)**

![Responsive Mockup](assets/images/readme/guess-the-god-mockup.png)

**Table of contents:**

- [Title](#guess-the-god)
- [User Experience](#user-experience-ux)
  - [Expectation](#expectation)
  - [User Journey](#user-journey)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)
- [Features](#features)
  - [Languages Used](#languages-used)
  - [Existing Features](#existing-features)
  - [Features Not Yet Implemented](#features-not-yet-implemented)
- [Testing](#testing)
  - [Validator Testing](#validator-testing)
  - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Tools and Libraries](#tools-and-libraries)
  - [Acknowledgements](#acknowledgements)

## User Experience (UX)

  - ### Expectation
    - **Clear Instructions**: Users look for clear and concise instructions on how to play the game.

    - **Simple Navigation**: Navigation of the game is simple and intuitive.

    - **Feedback**: Users expect and receive immediate feedback from each and every action performed whilst playing the game.

    - **Educational**: Users receive new and interesting pieces of information upon playing the game.

    - **Responsive Design**: Whether playing on mobile or desktop the game works well and as expected on both.

  - ### User Journey
    - **Landing Page**: Users are welcomed with a nicely styled door which upon clicking the button in the centre of the screen will open to the main menu.  
    This experience is slightly different on mobile as the first screen will be the main menu.

    - **Main Menu**: A clear choice of either start game or how to play is shown to the user.

    - **Question Screens**: Each question displays an 
    image of a god with multiple-choice options to select the correct pantheon with the option to also get a hint.

    - **Feedback**: After selecting an answer, users 
    receive immediate feedback on whether they were correct, with additional information about the god.

    - **Completion**: At the end of the quiz, users are offered an encouraging message on their performance  
    and offered a choice to play again or to end the game and be returned to the main menu/closed door depending on platform.

## Design

  - ### Colour Scheme
    - I chose these colours to create a visually striking and immersive experience that reflects the grandeur and mystique of mythology, with the dark red conveying a sense of ancient power, while the black and white provide clear, readable text and elements that stand out against the light, neutral background.

    - The colour palette below was created using **[EightShapes Contrast Grid](https://contrast-grid.eightshapes.com)**

      ![Colour Palette](assets/images/readme/colour-palette.png)

  - ### Typography
    - The primary font is 'Lato', sans-serif for general text, providing a clean and modern look. 
    
    - 'Vollkorn', serif is used for headings to add a touch of elegance and distinction.
    
    - All fonts were acquired through **[Google Fonts](https://fonts.google.com/)**.

  - ### Imagery
    - High-quality images of gods from different mythologies are used to create a visually engaging and educational experience.  
    The images are central to the quiz, helping users associate visual characteristics with each god.
    
    - All god images were created with the help of **[ChatGPT](https://chatgpt.com/?oai-dm=1)**.

  - ### Languages Used
    - **HTML5**: Used for structuring the content of the web pages. HTML5 provides the semantic elements and structure necessary for a well-organized and accessible web application.
    
    - **CSS3**: Used for styling the web pages. CSS3 ensures that the application has a visually appealing and consistent design. It includes the use of Flexbox and Grid for layout, and media queries for responsiveness.
    
    - **JavaScript**: Used for adding interactivity to the web application. JavaScript powers the game's logic, user interactions, dynamic content updates, and animations.  
    As well as the use of modules to improve readability and scalability in the future.
    
    - **Markdown**: Used to write the README.

  - ### Wireframes

Please see below the original wireframes of the site made using Balsamiq Wireframes.

- #### Main Menu (Desktop)

![Main Menu Desktop Wireframe](assets/images/readme/main-menu-desktop-wireframe.png)

- #### Main Menu (Mobile)

![Main Menu Mobile Wireframe](assets/images/readme/main-menu-mobile-wireframe.png)

- #### Game Zone

![Game Zone Wireframe](assets/images/readme/game-zone-wireframe.png)

## Features

Below I will go into a brief explanation of the features I have encorporated into the game.

### Existing Features

- __Landing Page (Desktop)__

    - Shown upon loading the site on desktop, an attractive image used to introduce the site with minimal wording. 
    - A central button offering an intriguing message of "Enter the Pantheon" inviting users to click and continue onto the main title screen.
    - The sliding effect of the main image on the desktop landing page offers a feeling of grandeur as the main title page is unveiled.

![Landing Page Desktop](assets/images/readme/landing-page-desktop.png)

- __Main Menu (Desktop)__

    - An intuitive and simple to use main menu with 2 buttons, "Start Game" and "How to Play".
    - Attractive imagery that supports getting the player into the right mindset for the game.

![Main Menu Desktop](assets/images/readme/main-menu-desktop.png)

- __Landing Page/Title Page (Mobile)__

    - The mobile landing page, although missing the sliding feature image of the desktop version still offers the same asthetic with a identical title page.
    - A simple to use title page main menu offering the options of "Start Game" and "How to Play" with an attractive hero image to give a distinct feel to the game.

![Landing Page/Title Page Mobile](assets/images/readme/landing-page-mobile.png)

- __Instructions__

    - When the "How to Play" button is clicked a message window will open to give all the relevant instrutions the player will need.
    - The instructions window includes it's own "Start Game" button to avoid needing to return to the main menu.

![Instructions](assets/images/readme/instructions.png)

- __Game Zone__

    - A stylised image of a god will appear central to the game zone.
    - A question will display below the god image "To which mythology does this god/goddess belong?".
    - The answer buttons are displayed clearly below the question each in the same style as the main site.
    - A hint button is displayed below the answer buttons, clearly stating the repercussion for using a hint.

![Game Zone](assets/images/readme/game-zone.png)

- __Score__

    - A score keeping area is displayed below the buttons.

![Score](assets/images/readme/score.png)

- __Alert Box (Answer)__

    - For each action the player performs a message box will appear central to the screen.
    - Uses an "x" in the top right corner as a close button.
    - Will give the player feedback on their chosen answer whether it was right or wrong.

![Alert Box Answer](assets/images/readme/alert-box-answer.png)

- __Alert Box (Hint)__

    - Will give the player a hint dependant on the current god/goddess displayed.
    - The hint can be displayed as many times as the player would like for each god/goddess.

![Alert Box Hint](assets/images/readme/alert-box-hint.png)

- __Alert Box (End Game)__

    - The message box will contain 2 buttons upon reaching an end game state "End Game" and "Play Again".
    - The "x" in the top right will not appear for this message so as not to present an unwanted loop in game.

![Alert Box End Game](assets/images/readme/alert-box-end.png)

### Features Not Yet Implemented

- __Difficulty__

    - If I was to continue adding features at this stage then next would be a difficulty selector  
    giving the player a limited amount of time or guesses to reach the required score to win.

- __More Pantheons__

    - Another feature I may implement is further Pantheons to guess from such as Roman or Hinduism.

## Testing

Each feature of the game has been tested upon integration and also tested again upon completion of development, these tests will be outlined below.

- **Sliding Images**: The sliding images on the landing page were tested to ensure they animate correctly  
and reveal the main menu upon clicking the "Enter The Pantheon" button. The transition and timing were checked for smoothness and alignment.

- **Navigation Buttons**: All buttons present within the site have been tested to confirm they perform the correct actions:
    - The "Start Game" button begins the game.

    - The "How to Play" button displays the instructions.

    - The "Play Again" and "End Game" buttons appear at the end of the game, and they respectively restart the game or return the user to the main menu.

- **Answer Buttons**:  Each answer button was tested to ensure it registers the correct mythology when clicked. The correct feedback message is displayed based on the user's choice.
 
- **Hint Button**:  The hint button was tested to ensure it displays the correct hint and deducts points only the first time it is used for each god.  
The score is adjusted accordingly, and hintsUsed array functions properly to prevent repeated point deduction for the same hint.

- **Score Calculation**:  The scoring system was tested to ensure points are correctly awarded for correct answers and deducted for hints.  
The score properly resets when the game is restarted.

- **Alert Box**:  The custom alert box was tested to ensure it displays the correct messages for user feedback, and the close button functions as expected.  
Additionally, the answer buttons are temporarily disabled when the alert box is shown and re-enabled upon closing.

- **Responsive Design**: The layout and functionality was tested across different screen sizes and devices to ensure the game maintains its structural integrity and usability.

- **Accessibility**: All images were tested for appropriate alt text to ensure accessibility. Colour contrast was checked to meet accessibility guidelines.

### Lighthouse Testing

Along with feature testing I have also run lighthouse tests, these have come back very positive as seen below with the screen captures.

- #### Lighthouse report for desktop

![Lighthouse Report Desktop](assets/images/readme/lighthouse-report-desktop.png)

- #### Lighthouse report for mobile

![Lighthouse Report Mobile](assets/images/readme/lighthouse-report-mobile.png)

### Validator Testing

- __HTML__
    - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fshlackka.github.io%2Fguess-the-god%2F)
- __CSS__
    - No errors were returned when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fshlackka.github.io%2Fguess-the-god%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- __JavaScript__
    - No errors were returned when passing through **[JSHint](https://jshint.com/)** as shown in the images below.

    ![script.js Testing](assets/images/readme/script-testing.png)
    ![data.js Testing](assets/images/readme/data-testing.png)

### Unfixed Bugs

To the best of my knowledge after testing all aspects of the site I have been unable to find any unfixed bugs.

## Deployment

The site has been deployed to GitHub pages, in order to do this the following steps were completed.

- From within the guess-the-god repo I navigated to the settings tab

- In settings navigate to the Pages section under "Code and automation"

- Once in Pages, I chose to deploy from a branch as the source and then chose the Main branch before clicking save

- The deployed site can be found at **https://shlackka.github.io/guess-the-god/**

If you wish to fork the repo this can be achieved by using the "Fork" button at the top of the repo and following the onscreen prompts to set up the forked repo as you wish.

If you wish to clone the repo this can be achieved by using the drop down on the green "code" button and copying the URL into a workspace of your choosing such as **[Gitpod](https://www.gitpod.io/)** or **[CodeAnywhere](https://codeanywhere.com/)**.

## Credits 

In the below section I will go over all of the external sources where I either drew inspiration or used their tools to assist in the development of Guess the God.

### Content

- All text included within Guess the God has been typed out by myself with hint and god facts first being found with the use of **[ChatGPT](https://chatgpt.com/?oai-dm=1)** before being reworded into the game.

- **[ChatGPT](https://chatgpt.com/?oai-dm=1)** has been used to help explain certain JavaScript concepts I was struggling with, specifically when I changed the nested if statements into a switch case and exporting and importing the god data from the data file.

- All inspiration for this project was taken from my personal interest into ancient civilizations and their respective mythologies and religions.

- Fonts for the site were found using **[Google Fonts](https://fonts.google.com/)**.

### Media

- All images including those used as backgrounds have been created using the DALL-E AI image creator through **[ChatGPT](https://chatgpt.com/?oai-dm=1)** by OpenAI.

- Favicon was created using **[Red Ketchup](https://redketchup.io/favicon-generator)**.
 
### Tools and Libraries

- **[Gitpod](https://www.gitpod.io/)** was used as the development environment.

- **[Visual Studio Code](https://code.visualstudio.com/)** was the code editor used for writing and editing the project's code within Gitpod.

- **[GitHub](https://github.com/)** was used for version control and hosting the project repository.

### Acknowledgements

- I would like to thank my family, specifically my sister Robyn for helping to playtest Guess the God  
and highlight any areas of gameplay I may have overlooked during development.

- I would also like to thank my Mentor Harry Dhillon who has been an invaluable source of encouragement.  
Always helping to guide me in the right direction during development.