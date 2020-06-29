# Project 0
Web Programming with Python and JavaScript

## Short Writeup
This is a demonstration website to simulate an information page of a residential place knowned as the Penguin Peninsula. It allows users to visit and know about the current situation of the place.

There are four main html files in this project:
- index.html displays the about us and introduction page for the viewers
- signUp.html displays the sign up page for the viewers
- inhabitants.html displays the current residents of the Penguin Peninsula
- gallery.html displays the image gallery of the scene

(S)CSS files used are stored in the CSS folder:
- extra.css (Add ons to Bootstrap 4)
- screen.css (Mainly for media query/responsive)

Images files are sourced from Google Search.

<a href="https://youtu.be/ZVVMm2KHnjM">Link to Youtube</a>

## Requirements
### In README.md, include a short writeup describing your project, what’s contained in each file, and (optionally) any other additional information the staff should know about your project.
1. [x] Short writeup

### Your website must contain at least four different .html pages, and it should be possible to get from any page on your website to any other page by following one or more hyperlinks.
1. [x] At least 4 HTML Pages: 
    - index.html
    - gallery.html
    - inhabitants.html
    - signUp.html

2. [x] Hyperlinks to all websites

### Your website must include at least one list (ordered or unordered), at least one table, and at least one image.
1. [x] At least 1 List (Ordered/Unordered):
    - inhabitants.html [List of Names]

2. [x] At least 1 Table: 
    - index.html [Menu Options]
    - gallery.html [Menu Options and Image Gallery]
    - inhabitants.html [Menu Options]
    - signUp.html [Menu Options]

3. [x] At least 1 Image: 
    - In all sites as a background: https://sb.ecobnb.net/app/uploads/sites/3/2015/10/Igloo.jpeg
    - gallery.html: nightView.jpg, frontView.jpg, seaView.jpg, backView.jpg

### Your website must have at least one stylesheet file. {Done}
1. [x] At least 1 Stylesheet:
    - extra.css
    - bootstrap4
    - screen.css

### Your stylesheet(s) must use at least five different CSS properties, and at least five different types of CSS selectors. You must use the #id selector at least once, and the .class selector at least once. {Done}
1. [x] At least 5 different CSS Properties:
    - background-color
    - border
    - border-collapse
    - bottom
    - color
    - content
    - cursor
    - display
    - font-size
    - font-weight
    - font-style
    - font-family
    - height
    - opacity
    - padding
    - position
    - width
    - text-align
    - z-index

2. [x] At least 5 different types of CSS Selectors:
    - Multiple Elements/Grouping Selector: e.g p, h3
    - Pseudo-Element Selector: e.g h1::before
    - Universal Selector: e.g. *
    - Descendent Selector: e.g. table td a
    - Pseudo-Class Selector: e.g. td:hover, a:hover

3. [x] Use id selector at least once:
    - #title [screen.scss]
    - #coverPage [extra.scss]
    - #fillerText [extra.scss]
    - #tooSmall [screen.scss]
    - #chiefPosition [extra.css]
    - #managerPosition [extra.css]
    - #orderlyPosition [extra.css]

4. [x] Use class selector at least once:
    - .directory [extra.css]
    - .resident [extra.css]
    - .titlePosition [extra.css]

### Your stylesheet(s) must include at least one mobile-responsive @media query, such that something about the styling changes for smaller screens.
1. [x] At least one mobile-responsive @media query:

### You must use Bootstrap 4 on your website, taking advantage of at least one Bootstrap component, and using at least two Bootstrap columns for layout purposes using Bootstrap’s grid model. {Done}
1. [x] Use Bootstrap 4

2. [x] Use at least one Bootstrap Component:
    - img-fluid, img-rounded
    - table-responsive and table-bordered

3. [x] Use at least 2 Bootstrap columns for layout purposes

### Your stylesheets must use at least one SCSS variable, at least one example of SCSS nesting, and at least one use of SCSS inheritance.
1. [x] Use at least one SCSS variable:
    - $words [extra.css]
    - $pageBG [extra.css]
    - $tableBG [extra.css]
    - $hoverFont [extra.css]

2. [x] Use at least one SCSS nesting:
    - table [extra.css]

3. [x] Use at least one SCSS inheritance:
    - td [extra.css]
    - h1::before [extra.css]
    - #chiefPosition::before [extra.css]
    - #managerPosition::before [extra.css]
    - #orderlyPosition::before [extra.css]
    - .resident::before [extra.css]