# Little Explorers – Fieldtrip Locator
###### Project 3: Data Centric Development with Python - Code Institute
This website aims to help preschool educators add and search for suitable field trip locations for the children. This is so that some of the weight of educators’ responsibilities can be reduced and they can focus more on the children themselves rather than planning.

This website aims to create a community of preschool educators who collaborate and share their resources and experiences on field trips with each other. This includes contact details and activity ideas for the location.

## The website
A website can be found [here.]( https://fieldtrip-database.herokuapp.com/)

## UX
This website can be used by preschool educators who would like share their field trip locations and those looking for field trip ideas.

Below are several user stories for the website:
- As a new preschool educator planning a field trip for the first time, I want to be able to search for ideas that can help me to start planning.
- As a preschool educator, I want to be able to share new locations and some ideas of field trips to help other educators.
- As a preschool educator, I want to be able to add on to the information to help the other communities of early childhood educators.
- As a principal, I want to be able to have the authority to remove entries that I deem inappropriate for children based on my years of experience.

Below is the detailed UX planning of the website from the Strategy to the Surface.

#### Strategy:
In Singapore, preschool educators are often overwhelmed with the responsibilities that they have.
This not only includes nurturing the children but also loaded with paperwork, curriculum planning and administrative responsibilities.

One of the things that educators have to plan are field trips that build on what children are learning at moment.
Hence, to lighten some load for the educators in one aspect of planning, this site aims to create a database where teachers can share field trip locations and activities.
Therefore, teachers will have more time on their hands for their other responsibilities.

#### Scope:
On the site educators will be able to:

- CREATE new entries of locations and its details.
- READ[search] through entries that have been put up by:
	- Name
	- Theme
	- Age Group
	- Price
- UPDATE[edit] entries should they have more things to add on that could help other teachers.
- DELETE entries that they deem unsuitable for children or if locations have closed down.

The site will include:
- A database of field trip locations that will have
	- A name
	- An image
	- An address
	- A contact email for the location [if needed]
	- A description of the location
	- Themes selected from a given set
	- List of activities
	- Age group selected from a given list
	- Price [free, paid or both]

#### Structure:
The site will use a flask template with multiple html files to display different pages.

A navigation link will be found at the top of the page for easy and intuitive navigation.

Navigation will include:
	- View all locations
	- Search for location
	- Add location

To view the ER diagram for the database click [here.](https://github.com/diyanah08/project-3-fieldtrip-database/blob/master/static/images/er-diagram.jpg)

#### Skeleton:
On entering the site, the landing page will have a carousel of images and an instruction on how to navigate through the site.

Once entered, the site is easily navigated through using the navigation bar in the header.

To view the original wireframe of the website click [here.](https://github.com/diyanah08/project-3-fieldtrip-database/blob/master/static/images/skeleton.jpg)


#### Surface:
As the site is catered for preschool educators, the colours used will be bright, light and inviting. Fonts will also be more casual and cursive. As a good practice for preschool educators, the fonts chosen will also try to be preschool/dyslexic friendly.

## Features

### Existing Features
###### 1) Landing Page:
- On the landing page in a carousel of some images. A text is in front of the images. This text has the introduction/instruction for the site.

###### 2) Navigation Bar [Bootstrap], Back to top button [JavaScript], Back button {JavaScript]:
- A navigation bar is located the top of the page to allow users quick navigation.
- The user will not have to scroll all the way back up as there is a button that will seamlessly scroll the page back to the top when pressed.
- Some pages also have a back button where users can easily click to go back a page.

###### 3) Home Page/ View All:
- When the ‘BEGIN!’ button on the landing page is clicked, the site is directed to the home page which is also the view all page.
- This page has all the entries that have been added in.
- It shows a snapshot of the information and when a user clicks on the name of the location, they will be directed to a page where they will be able to view the full details of the selected location.
- If an image is unable to load, an alternative image – the site’s logo – will be displayed instead.

###### 4) View a location
On the page when users press to view a specific location, they can
- View all the details including, name, address, email, description, activities, themes, age-group and price.
- Click to edit contact details
- Click to edit descriptions
- Click to delete entry

    a)	Edit contact – when the button is clicked, the page will display a form where users will be able to edit the location name, address and email.
    
    b)	Edit Information – when the button is clicked the page will display a form where users will be able to edit the description, activities age group and theme of the location.
    
    c)	Delete Entry – when clicked, a modal will appear, prompting the user to enter a key to confirm the delete. If the key is valid, the delete will be successful. If the key is not valid, the delete will be unsuccessful.


###### 5) Search
On the search page users can by

- Name
- Age-group
- Themes
- Price

When a search is done, the results will be shown at the bottom of the search form. It will also display a snapshot of the information and there is a button to view the full information.

###### 6) Add
This page consists of a form where users can add a new entry for location. Some of the fields in the form is required hence users will not be able to add if the fields are missing.

If an entry is successfully added, an alert will appear hence users will be able to know.


### Features Left to Implement
1) Ability to change the image uploaded and upload multiple images.
2) Ability for user to upload files to share their lesson plans and other user to download them.
3) Addition of mapbox to the address/auto complete of addresses.

## Technologies Used
- HTML
    - [BOOTSTRAP](https://getbootstrap.com/docs/4.3/getting-started/introduction/) was used for several components in the site.
- CSS
    - [GOOGLE FONTS](https://fonts.google.com/) was used to provide a variety of fonts through out the site.
    - [FONT AWESOME ICONS](https://fontawesome.com/icons) was used for the back-to-top botton.
- JavaScript
- Python
- Flask
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
	- Used as the database for the site
- GitHub
	- Used for version control 
- Heroku
	- Used for deployment

## Testing
For this project, no automated testing was used.
Instead, manual testing was conducted.

The steps were:
##### 1) Loading the site
- Upon loading of the site’s landing page, the carousel appears and images are loaded.
- ‘Begin’ button is clickable and leads to the home page

##### 2) Home page / View all
- Page is loaded with locations. A snapshot of each location along with an image can be seen.
- Each entry should have a image. If an uploaded image is unable to load, the site’s logo will be displayed instead.
- When clicked on the ‘View’ button, the page will load up the full details of the location.
- On the view page there will be edit contact, edit description and delete entry buttons.

###### Edit Contact
- When click, the edit contact form will load with the existing information. Information in editable.
- After editing, the page will display the edited version of the contact and an alert to saying that the alert is successful

###### Edit Description
- Similar to the edit contact, a form will load with the existing information.
- After editing, the page will also display the edited description and an alert saying the edit was successful.

###### Delete Entry
- When clicked, a model will appear with the prompt to key in a SECRET KEY.
- If the key is entered incorrectly, the delete is unsuccessful and a danger alert will appear.
- If the key is entered correctly, the delete is successful and the success alert will appear.

##### 3) Search
- When clicked, a search form is loaded.
- Search can be done by name, age-group, themes or price.
- When a search is executed, the results will appear at the bottom of the search form.
- Each result will be shown in a bootstrap card and will displsy a snapshot of the information.
- Again, when clicked on view, the page will load to the full information.

##### 4) Add
- When clicked from the navigation bar, a form will load.
- The form will be filled with information of a new location.
- If the name, image or address field is left empty, the form will prompt to fill it in.
- If the entry is successfully added in, a success alert will appear at the top of the page.

##### 5) Back to top and Back buttons
- Each button is clicked on and checked to see if they are working.



##### The above steps for testing were done on:


| BROWSERS          | DEVICES                                    | TEST OUTCOMES                                                                                                                                                         |
| ----------------- |:------------------------------------------:| -------------------------------------------------------------------------:|
| Windows Edge      | Windows 10                                 | Testing appeared to pass                                                  |
| Google Chrome     | Windows 10, Samsung S9, Samsung Galaxy Tab | Testing appeared to pass                                                  |
| Firefox           | Windows 10                                 | Testing appeared to pass                                                  |
| Safari            | iPhone 6 & 7, iPad Pro, MacBook Pro        | Testing appeared to pass                                                  |
| Samsung Internet  | Samsung S9, Samsung Galaxy Tab             | Testing appeared to pass                                                  |
| Internet Explorer | Windows 10                                 | Images in search results are not able to be the height of the card-image. |

###### Unfortunately the issues reflected above have yet to be resolved at the point of submission.

## Deployment
This project was hosted through GitHub Pages.
- A GitHub repository was created for this project and titled ‘project-3-fieldtrip-database’.
- Throughout the project, regular commits were made when significant additions or edits were made.
- The commits were then pushed to the master branch of the repository.
- Heroku was then used to deploy the project.
- This was done by setting up 
- Files for the project committed to GitHub can be pulled and run locally [here.]( https://github.com/diyanah08/project-3-fieldtrip-database)
- The link to the webpage can be found [here.]( https://fieldtrip-database.herokuapp.com/)

## Credits
#### Media
- The photos used in this site were obtained from pexels.com and google images.

#### Acknowledgements
- The scroll to top codes were gotten from [here.](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)
- The back button javascript codes were gotten from [here.](https://www.w3schools.com/jsref/met_his_back.asp)