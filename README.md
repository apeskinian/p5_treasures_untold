# [P5 TREASURES UNTOLD](https://apeskinian-treasures-untold-568a3e176ede.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/apeskinian/p5_treasures_untold)](https://www.github.com/apeskinian/p5_treasures_untold/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/apeskinian/p5_treasures_untold)](https://www.github.com/apeskinian/p5_treasures_untold/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/apeskinian/p5_treasures_untold)](https://www.github.com/apeskinian/p5_treasures_untold)

**An online store for all your magical Disney items!**

Look at your stuff..<br>
Isn't it neat?<br>
Wouldn't you think your collection's complete?

**No!** You can always find something more to add to your magical collection at Treasures Untold!

Treasures Untold is an e-commerce solution to selling the rare and difficult to acquire items from some of the most famous realms featured in Disney. From a frying pan to glass slipper, there's a whole trove of products to browse. Items can be filtered, sorted, and searched using the site's easily accessible features. Each product can then be viewed in more detail and added to a shopping basket ready for secure checkout processing using Stripe. For security, users do need to register an account to be able to purchase items but can freely browse as a guest. There are also opportunities to unlock rewards that grant certain perks...

A well featured list of support pages also offers help for users including:
  - **FAQs** page for the common questions that users have.
  - **Contact Us** where users can submit a question directly.
  - **Newsletter** page where users can learn about the newsletter and sign up. Confirmation is required via a link sent via email after initially signing up. Users signed up to the newsletter can also unsubscribe at any time by using the unsubscribe link in each newsletter they receive.
  - **Returns Policy** for information and terms about product returns.
  - **Privacy Policy** for how information about users is stored and used.
  - **Terms and Conditions** for general site terms.

A staff dashboard reserved for users with staff and admin privileges allows management of products, FAQs, contact messages, and newsletter admin:
  - New products and realms can be created, and existing ones can be modified and deleted.
  - FAQs that appear in the support pages of the site can also be managed with full CRUD functionality.
  - The contact messages section allows staff to read the messages sent via the contact us page and send an initial reply straight from the dashboard.
  - The newsletter section allows management of both newsletters and subscribers. Newsletters can be created and sent to the current list of subscribers. The list of subscribers is also found here, and staff can see the status of the email addresses that have been submitted. Each address can be removed individually, and if there are email addresses that have expired, they can all be cleared in one easy action.

![screenshot](documentation/tu-mockup.png)

source: [Techsini Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/?url=https://apeskinian-treasures-untold-568a3e176ede.herokuapp.com/)


## UX

### Strategy

**Purpose**
- Provide a seamless and intuitive e-commerce experience for customers to browse, filter, and purchase magical items found in the Disney realms.
- Empower site owners to manage the store's inventory and support content efficiently.

**Primary User Needs**
- Guest users need to be able to browse products and use support features with ease.
- Registered customers need a streamlined shopping experience with account and order history features.
- Site owners need robust tools for inventory and support content management.

**Business Goals**
- Drive sales by providing a user-friendly shopping experience.
- Build customer loyalty through personalized and efficient account features.
- Maintain an organized and up-to-date store inventory.

### Scope

**Features**

A full list of [Features](#features) can be viewed in detail below but essentially I wanted to include:
 - Browsing and support avaible for guests.
 - Account requirement for purchases.
 - Full sort, filter, and search functionality for browsing products.
 - Smooth checkout experience with redundancy built it.
 - Stock recovery for abandoned/lost baskets.
 - Intuitive feature rich staff dashboard.
 - Some Easter eggs to unlock special discounts.


**Content Requirements**
- Product details, including name, price, description, stock level, category, and images.
- Clear prompts and instructions for browsing, filtering, and purchasing.
- Order details, confirmation pages, and email notifications.
- Secure payment processing using Stripe.
- Payment success emails sent to users.
- 404 page for lost users.
- 500 page for any server errors.

### Structure

The homepage of the site is where the user is welcomed. This page features products available in the store in two sections, one for recently added items and one for a featured realm, which is cycled every time the page loads to create more exposure for the products. A scrolling banner divides these to advertise where the site has been featured.

At the bottom of most pages there is an information and support panel that gives all users quick access to newsletter sign up, social media links and common site links.

Navigation for the site is provided via a menu that slides out upon activation by the well recognised burger menu icon on the top left. This menu gives the user full navigation and search functionality.

The account and basket menus are situated to the top right of the screen. The account menu drops down to give the user options relevant to their access privileges. The basket menu acts in a similar way to the navigation menu sliding out from the side to show the user their basket contents and then links to checkout or manage their basket.

The navigation, account and basket access for mobile users is all done from a menu at the bottom of the screen for easier access on smaller devices.

When viewing products user will be able to filter and sort further using options either to the side of the products for desktop devices or via another filter menu option in the mobile navigation bar. Items can be added to a registered users basket from the product detail page.

The users next step will either be to navigate to the basket view where they can adjust quantities and remove items or go straight to the checkout page to complete their purchase.

Once completed they will be shown a confirmation of the order.

Users can also access their profile page via the account menu to see past order details and update their details.

Staff members can access the dashboard via the account menu and from there select which area they wish to manage via a tabbed layout.

All logged in users will have confirmation of their login displayed along with a button to log out in the account menu.

**Information Architecture**

- **Navigation Menu**:
  - Home
  - New
  - All Products
  - Products by Realm
  - FAQ
  - Contact Us
  - Newsletter
  - Returns Policy
  - Privacy Statement
  - Terms and Conditions
- **Account and Basket Menu**:
  - Account options (including dashboard for staff and admin panel for admin)
  - Basket (leading to checkout or basket management)
- **Hierarchy**:
  - Prominent product categories and filters for easy navigation.
  - Basket and checkout options displayed prominently for convenience.


### Skeleton

In the wireframing process, I decided the navigation should be simple and remain constant throughout the site where possible. Having navigation on the bottom for mobile devices makes it easier for the user to interact with while keeping the screen visible. The navigation would move to the top for larger screens for a more traditional layout.

A full list of [Wireframes](#wireframes) can be viewed in detail below.

### Surface

**Visual Design Elements**

- **[Colours](#colour-scheme)**: see below.
- **[Typography](#typography)**: see below.

### Colour Scheme

The colour scheme for the site was based around colours used in the main hero image. This image was created using [Canva Dream Lab](https://www.canva.com/dream-lab) and the prompt *"A hero image for an online shop selling magical items without text"*

![Original Canva Image](documentation/ux/canva_dream_lab_image.png)

I used Affinity Photo 2 to remove the text, clean it up and use the colour picker to select complimentary colours for the site listed below. The image was then plugged back into Canva to expand the width. The edges were given a fade to transparent for the final edit in Affinity Photo 2.

![Final Hero Banner](documentation/ux/final_hero_banner.png)

For the colours I decided to use :root in the css to define them. This made referencing them easier when styling.

The action buttons are grouped by colour for specific types of action. This should lead the user naturally to each button when presented, depending on what they want to do.

| :root Reference | Colour Reference | Site Elements |
| --- | --- | --- |
| --tu-green: | #839680 | Sign In / Sign Up / Add / Confirm / Constructive Actions |
| --tu-green-hover: | #5f6e5d | Used when --tu-green items are hovered over |
| --tu-green-shadow: | #5f6e5d80 | Used for the border when --tu-green items are focused |
| --tu-red: | #934B59 | Sign Out / Delete Buttons / Destructive Actions |
| --tu-red-hover: | #713945 | Used when --tu-red items are hovered over |
| --tu-red-shadow: | #71394580 | Used for the border when tu-red-items are focused  |
| --tu-yellow: | #E6B86E | Edit Buttons / Alteration Actions |
| --tu-yellow-hover: | #C78D4B | Used when --tu-yellow items are hovered over |
| --tu-yellow-shadow: | #c78d4b80 | Used for the border when --tu-yellow items are focused |
| --tu-blue: | #5190a5 | Used for main navigational links / Progressive Actions |
| --tu-blue-hover: | #3F7586 | Used when --tu-blue items are hovered over |
| --tu-blue-shadow: | #3f758680 | Used for the border when --tu-blue items are focused |
| --tu-teal: | #405254 | Used for a contrasting alternative for --tu-green for similar actions but giving an aesthetic variance |
| --tu-teal-hover: | #28383a | Used when --tu-teal items are hovered over |
| --tu-teal-shadow: | #28383abd | Used for the border when --tu-teal items are focused |
| --tu-dark-teal: | #1B2429 | Mobile navigation menu background |
| --tu-purple: | #885b92 | Unloacked rewards message border |
| --tu-white: | #FFF | All contrasting text and icons that are on a dark background |
| --tu-off-white: | #f0f0f0 | Page content containers |
| --tu-light-grey: | #dcdcdc | Nav pills / Table headers / Message reply content background |
| --tu-mid-grey: | #b4b4b4 | Page backgrounds / Mobile menu highlighted background |
| --tu-dark-grey: | #555555 | Focused and Active nav pills / Menu link text |
| --tu-dark-grey-shadow: | #55555580 | Nav pill shadow |

### Typography

**Fonts**

- [Pirata One](https://fonts.google.com/specimen/Pirata+One) was used for the main logo and h1 elements.

- [Cantora One](https://fonts.google.com/specimen/Cantora+One) was used for all h2-h6 elements.

- [Roboto](https://fonts.google.com/specimen/Roboto) was used for all other text.

**Icons**

- The favicon for the site is from [Flaticon](https://www.flaticon.com/):

    | Icon | Name |
    | --- | --- |
    | ![Favicon](documentation/ux/lamp_favicon.png) | [Lamp](https://www.flaticon.com/free-icon/lamp_867845?term=magic&page=1&position=59&origin=tag&related_id=867845) |

- [Font Awesome](https://fontawesome.com) icons were used across the site for various uses:

    | Icon | Name | Use |
    | --- | --- | --- |
    | ![Bars](documentation/ux/bars-solid.svg) | [bars](https://fontawesome.com/icons/bars?f=classic&s=solid "font awesome link") | Navigation menu toggle |
    | ![Wizard Hat](documentation/ux/hat-wizard-solid.svg) | [hat-wizard](https://fontawesome.com/icons/hat-wizard?f=classic&s=solid "font awesome link") | Account menu toggle |
    | ![Shopping Basket](documentation/ux/basket-shopping-solid.svg) | [basket-shopping](https://fontawesome.com/icons/basket-shopping?f=classic&s=solid "font awesome link") | Shopping basket |
    | ![Filter](documentation/ux/filter-solid.svg) | [filter](https://fontawesome.com/icons/filter?f=classic&s=solid "font awesome link") | Mobile sort and filter menu toggle |
    | ![Magnifying Glass](documentation/ux/magnifying-glass-solid.svg) | [magnifying-glass](https://fontawesome.com/icons/magnifying-glass?f=classic&s=solid "font awesome link") | Search bar submit button |
    | ![Angle Down](documentation/ux/angle-down-solid.svg) | [angle-down](https://fontawesome.com/icons/angle-down?f=classic&s=solid "font awesome link") | By realm product view dropdown menu |
    | ![Angle Up](documentation/ux/angle-up-solid.svg) | [angle-up](https://fontawesome.com/icons/angle-up?f=classic&s=solid "font awesome link") | Scroll to top button |
    | ![Plus Sign](documentation/ux/plus-solid.svg) | [plus](https://fontawesome.com/icons/plus?f=classic&s=solid "font awesome link") | Quantity adjustment in basket view |
    | ![Minus Sign](documentation/ux/minus-solid.svg) | [minus](https://fontawesome.com/icons/minus?f=classic&s=solid "font awesome link") | Quantity adjustment in basket view |
    | ![Rotate](documentation/ux/rotate-solid.svg) | [rotate](https://fontawesome.com/icons/rotate?f=classic&s=solid "font awesome link") | Basket refresh button |
    | ![Trash Can](documentation/ux/trash-can-solid.svg) | [trash-can](https://fontawesome.com/icons/trash-can?f=classic&s=solid "font awesome link") | Delete/Remove buttons |
    | ![Envelope](documentation/ux/envelope-solid.svg) | [envelope](https://fontawesome.com/icons/envelope?f=classic&s=solid "font awesome link") | Email address icon in profile page |
    | ![Phone](documentation/ux/phone-solid.svg) | [phone](https://fontawesome.com/icons/phone?f=classic&s=solid "font awesome link") | Phone number icon in profile page |
    | ![Sparkling Magic Wand](documentation/ux/wand-magic-sparkles-solid.svg) | [wand-magic-sparkles](https://fontawesome.com/icons/wand-magic-sparkles?f=classic&s=solid "font awesome link") | Used in overlay when processing transactions |
    | ![Clock Rotating Left](documentation/ux/clock-rotate-left-solid.svg) | [clock-rotate-left](https://fontawesome.com/icons/clock-rotate-left?f=classic&s=solid "font awesome link") | Delivery window timer in product views |
    | ![Pen to Square](documentation/ux/pen-to-square-solid.svg) | [pen-to-square](https://fontawesome.com/icons/pen-to-square?f=classic&s=solid "font awesome link") | Edit buttons |
    | ![Paper Plane](documentation/ux/paper-plane-solid.svg) | [paper-plane](https://fontawesome.com/icons/paper-plane?f=classic&s=solid "font awesome link") | Newsletter sign up submit button |
    | ![Reply](documentation/ux/reply-solid.svg) | [paper-plane](https://fontawesome.com/icons/reply?f=classic&s=solid "font awesome link") | Reply to message submit button |


## User Stories

**Database Setup**
| User | Capability | Benefit |
| --- | --- | --- |
| As a developer | I can create a JSON fixtures file for the product model | so that I can quickly and easily load products into the database. |
| As a developer | I can create a JSON fixtures file for the realm model | so that I can quickly and easily load realms into the database. |
| As a developer | I need images for the products | so that site users can see the product. |

**Viewing and Navigating Products**
| User | Capability | Benefit |
| --- | --- | --- |
| As a site user | I can see a homepage full of useful information | so that I can see what the site is and why I should spend my time here. |
| As a user | I can view the available items | so that I can decide if I'd like to buy one or some of them. |
| As a user | I can click on a product | so that I can see more detailed info on the product. |
| As a user | I can access my shopping basket from anywhere | so that I can keep track of my current total and avoid spending too much. |
| As a user | I can easily see if items are out of stock | so that I know I cannot buy them. |
| As a user | I can see a custom 404 error page | so that I know the page I’m looking for doesn’t exist and can easily navigate back to the rest of the site. |
| As a user | I can see a custom 500 error page | so that I understand something went wrong on the server and can find a way to navigate back to the site. |
| As a user | I can sign up to be notified if an item that is sold or out of stock becomes available | so that I can purchase it. |
| As a user | I can share products directly to social media platforms | so that I can share items with my friends easily. |

**User Accounts**
| User | Capability | Benefit |
| --- | --- | --- |
| As a user | I can create an account | so that I can purchase items and view/edit my own profile. |
| As a user | I can easily log in and out of my account | so that my details remain private and secure. |
| As a user | I can easily recover my account and change password | so that I can continue to log in and out if I forget my password. |
| As a user | I should receive a confirmation email when my account is created | so that I know it was created successfully. |
| As a user | I can view a user profile page | so that I can see my purchase history and update my details. |
| As a developer | I can implement a social media login | so that users can create accounts quickly and easily. |

**Sorting and searching for items**
| User | Capability | Benefit |
| --- | --- | --- |
| As a user | I can search manually for an item from an input field | so that I can find and view specific items quickly. |
| As a user | I can sort products | so that view the list of products sorted based on a selected property. |
| As a user | I can filter products | so that only products that match the filter property are shown. |
| As a user | I can order any of the sort or filter results by ascending or descending order | so that I can view the list in the order that I want to. |

**Purchasing and checkout**
| User | Capability | Benefit |
| --- | --- | --- |
| As a user | I can select how many of a product I wish to buy | so that I can add the amount I need in one process to the basket. |
| As a user | I can view the basket | so that see the total cost and all the items I have added to it. |
| As a user | I can adjust the quantity of product from the basket | so that I can easily edit how many I want. |
| As a user | I can remove an item directly from the basket | so that I can quickly adjust what I'm buying. |
| As a user | I can easily enter my payment details | so that checkout quickly and hassle free. |
| As a user | I can see an order confirmation after completing a purchase | so that I know the transaction was successful. |
| As a user | I receive an email confirming my order confirmation and details | so that I know the transaction was successful. |
| As a developer | I can expand the application to support multiple currencies | so that users can view and complete transactions in their preferred currency, improving accessibility and user experience. |

**Help and support page**
| User | Capability | Benefit |
| --- | --- | --- |
| As a user | I can send a message to the shop owner | so that if I have a question or message I can send it directly with my details so that they can get back to me. |
| As a user | I can view the FAQ on the help and support page | so that I may find the answer to a question I have before sending a message to ask. |
| As a user | I can sign up to a newsletter | so that I can be informed when new magical items have been found and added to the store for sale. |
| As a user | I can view the sites privacy policy | so that I can see how my data is stored and used. |
| As a user | I can view the sites returns policy | so that I can see how the returns process works should I not be happy with a purchase. |
| As a user | I can view the sites general terms and conditions | so that I can I can understand the rules, policies, and my rights when using the website. |

**Admin and store management**
| User | Capability | Benefit |
| --- | --- | --- |
| As a shop owner | I can access a shop admin page | so that they add edit and delete products so that they can keep the catalogue up to date. |
| As a shop owner | I can add a new product | so that the shop can be updated with new items. |
| As a shop owner | I can edit products | so that I can update prices, stock levels and keep the catalogue up to date. |
| As a shop owner | I can delete products from the catalogue | so that I can make sure the catalogue is up to date. |
| As a shop owner | I can add new questions and answers to the FAQ section of the help and support page | so that site users have the most up to date FAQ. |
| As a shop owner | I can edit any FAQ entries | so that amend any that I need to. |
| As a shop owner | I can delete FAQ entries | so that I can keep the list up to date by removing any redundant entries. |
| As a shop owner | I can view the messages sent from the contact us form | so that I can send an initial reply. |
| As a shop owner | I can manage newsletters including viewing previous newsletters and creating and sending newsletters | so that subscribers can be updated on any offers and news from the site. |
| As a shop owner | I can see a list of the current subscribers including active, pending and expired memberships. I can also remove any individual subscriber and clear all expired subscribers from the list | so that I can I can keep the subscriber list accurate, organised, and up to date. |

**Easter Eggs**
| User | Capability | Benefit |
| --- | --- | --- |
| As a curious user | I can enter a classic phrase in the search bar | so that a special reward is unlocked! |
| As a curious user | I might notice that upon hovering over a certain item the cursor changes, | should I perform a certain action a special reward is unlocked! |
| As a curious user | I might know about the Cave of Wonders in Agrabah and know what I need to gain access | to unlock a special reward... |
| As a greedy user | I might not be able to stop myself from wanting a particular product when a certain reward is activated | and I will see the consequences... |

**SEO and Marketing**
| User | Capability | Benefit |
| --- | --- | --- |
| As a developer | I need to implement good marketing strategies | so that the site gains exposure and attracts customers. |
| As a developer | I can make sure that SEO methods are used in the site | so that it ranks higher in search engine results, attracts more organic traffic, and provides a better user experience. |

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Mobile Wireframes
| Homepage | Account Menu | Navigation | Basket Preview | Products Full Title | Products Floating Title | Product Detail | Basket | Checkout | Checkout Success | Profile | FAQs | Contact Us | Newsletter | Privacy | Staff Dashboard |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![wireframe](documentation/wireframes/mobile/mobile_homepage.png "Homepage") | ![wireframe](documentation/wireframes/mobile/mobile_homepage_account_menu.png "Account Menu") | ![wireframe](documentation/wireframes/mobile/mobile_homepage_navigation_expanded.png "Navigation Menu") | ![wireframe](documentation/wireframes/mobile/mobile_homepage_basket_expanded.png "Basket Preview") | ![wireframe](documentation/wireframes/mobile/mobile_products_full_title.png "Products Full Title") | ![wireframe](documentation/wireframes/mobile/mobile_products_dynamic_title.png "Products Dynamic Title") | ![wireframe](documentation/wireframes/mobile/mobile_product_detail.png "Product Detail") | ![wireframe](documentation/wireframes/mobile/mobile_basket_view.png "Basket") | ![wireframe](documentation/wireframes/mobile/mobile_checkout.png "Checkout") | ![wireframe](documentation/wireframes/mobile/mobile_checkout_success.png "Checkout Success") | ![wireframe](documentation/wireframes/mobile/mobile_profile.png "Profile") | ![wireframe](documentation/wireframes/mobile/mobile_faq.png "FAQs") | ![wireframe](documentation/wireframes/mobile/mobile_contact_us.png "Contact Us") | ![wireframe](documentation/wireframes/mobile/mobile_newsletter.png "Newsletter") | ![wireframe](documentation/wireframes/mobile/mobile_privacy.png "Privacy") | ![wireframe](documentation/wireframes/mobile/mobile_shop_management.png "Staff Dashboard") |

### Tablet Wireframes
| Homepage | Account Menu | Navigation | Basket Preview | Products Full Title | Products Floating Title | Product Detail | Basket | Checkout | Checkout Success | Profile | FAQs | Contact Us | Newsletter | Privacy | Staff Dashboard |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![wireframe](documentation/wireframes/tablet/tablet_homepage.png "Homepage") | ![wireframe](documentation/wireframes/tablet/tablet_homepage_account_menu.png "Account Menu") | ![wireframe](documentation/wireframes/tablet/tablet_homepage_navigation_expanded.png "Navigation Menu") | ![wireframe](documentation/wireframes/tablet/tablet_homepage_basket_expanded.png "Basket Preview") | ![wireframe](documentation/wireframes/tablet/tablet_products_full_title.png "Products Full Title") | ![wireframe](documentation/wireframes/tablet/tablet_products_dynamic_title.png "Products Dynamic Title") | ![wireframe](documentation/wireframes/tablet/tablet_product_detail.png "Product Detail") | ![wireframe](documentation/wireframes/tablet/tablet_basket_view.png "Basket") | ![wireframe](documentation/wireframes/tablet/tablet_checkout.png "Checkout") | ![wireframe](documentation/wireframes/tablet/tablet_checkout_success.png "Checkout Success") | ![wireframe](documentation/wireframes/tablet/tablet_profile.png "Profile") | ![wireframe](documentation/wireframes/tablet/tablet_faq.png "FAQs") | ![wireframe](documentation/wireframes/tablet/tablet_contact_us.png "Contact Us") | ![wireframe](documentation/wireframes/tablet/tablet_newsletter.png "Newsletter") | ![wireframe](documentation/wireframes/tablet/tablet_privacy.png "Privacy") | ![wireframe](documentation/wireframes/tablet/tablet_shop_management.png "Staff Dashboard") |

### Desktop Wireframes
| Homepage | Account Menu | Navigation | Basket Preview | Products Full Title | Products Floating Title | Product Detail | Basket | Checkout | Checkout Success | Profile | FAQs | Contact Us | Newsletter | Privacy | Staff Dashboard |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![wireframe](documentation/wireframes/desktop/desktop_homepage.png "Homepage") | ![wireframe](documentation/wireframes/desktop/desktop_homepage_account_menu.png "Account Menu") | ![wireframe](documentation/wireframes/desktop/desktop_homepage_navigation_expanded.png "Navigation Menu") | ![wireframe](documentation/wireframes/desktop/desktop_homepage_basket_expanded.png "Basket Preview") | ![wireframe](documentation/wireframes/desktop/desktop_products_full_title.png "Products Full Title") | ![wireframe](documentation/wireframes/desktop/desktop_products_dynamic_title.png "Products Dynamic Title") | ![wireframe](documentation/wireframes/desktop/desktop_product_detail.png "Product Detail") | ![wireframe](documentation/wireframes/desktop/desktop_basket_view.png "Basket") | ![wireframe](documentation/wireframes/desktop/desktop_checkout.png "Checkout") | ![wireframe](documentation/wireframes/desktop/desktop_checkout_success.png "Checkout Success") | ![wireframe](documentation/wireframes/desktop/desktop_profile.png "Profile") | ![wireframe](documentation/wireframes/desktop/desktop_faq.png "FAQs") | ![wireframe](documentation/wireframes/desktop/desktop_contact_us.png "Contact Us") | ![wireframe](documentation/wireframes/desktop/desktop_newsletter.png "Newsletter") | ![wireframe](documentation/wireframes/desktop/desktop_privacy.png "Privacy") | ![wireframe](documentation/wireframes/desktop/desktop_shop_management.png "Staff Dashboard") |

## Features

### Existing Features

- ### User Accounts

    #### Individual Accounts
    Users can browse the shop as a guest but must create an account in order to purchase items. Account management is handled by Allauth.

    | Register Mobile | Register Desktop | Login Mobile | Login Desktop | Logout Mobile | Logout Desktop | Recover Mobile | Recover Desktop |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | ![Register Mobile](documentation/features/user_accounts/mobile_register.png "Register Mobile") | ![Register Desktop](documentation/features/user_accounts/desktop_register.png "Register Desktop") | ![Login Mobile](documentation/features/user_accounts/mobile_login.png "Login Mobile") |![Login Desktop](documentation/features/user_accounts/desktop_login.png "Login Desktop") | ![Logout Mobile](documentation/features/user_accounts/mobile_logout.png "Logout Mobile") | ![Logout Desktop](documentation/features/user_accounts/desktop_logout.png "Logout Desktop") | ![Recover Mobile](documentation/features/user_accounts/mobile_reset.png "Recover Mobile") | ![Recover Desktop](documentation/features/user_accounts/desktop_reset.png "Recover Desktop") |

    When logged in, your username is displayed so that you know you are logged in to the correct account. Every page also has access the log-out button.

    | Logged in Mobile | Logged in Desktop |
    | --- | --- |
    | ![Logged in Mobile](documentation/features/user_accounts/mobile_logged_in.png "Logged in Mobile") | ![Logged in Desktop](documentation/features/user_accounts/desktop_logged_in.png "Logged in Desktop") |

    #### Different Account Levels
    - There are three levels of user, each with different levels of access:
        - **User**: this is the default level with the following privileges:

            - Access their account.
            - Make purchases from the site.
            - View their purchase history with previous order details.
            - Update their personal details used for orders.

        - **Staff Member**: this is the standard level that would be given to a client user. They have all the same privileges as User with the additions:

            - Access to the staff dashboard page.
            - Create, update or delete Products
            - Create, update or delete Realms
            - Create, update or delete FAQs
            - Create, update or delete FAQ Topics
            - View and reply to messages received from the Contact Us page
            - Create and send newsletters
            - View and delete previous newletters
            - View subscriber list and current status for each
            - Remove individual subscribers
            - Clear all expired subscribers

        - **Super User**: this is the highest level and only for site administrators. In addition to User and Staff Member privileges, they can:

            - Access the Django Admin Panel.
            - Create, update and delete any type of user.
            - Create, update and delete orders.
            - Access custom session management commands (clear rewards, empty baskets, recover abandoned baskets)
    
    If you are a staff member or super user (admin), you will be presented with extra buttons to access the appropriate settings given to you.

    |  | Super | Staff | User |
    | --- | --- | --- | --- |
    | Mobile | ![Mobile Super](documentation/features/user_accounts/mobile_super.png "Super User Menu Mobile") | ![Mobile Staff](documentation/features/user_accounts/mobile_staff.png "Staff User Menu Mobile") | ![Mobile User](documentation/features/user_accounts/mobile_user.png "User Menu Mobile") |
    | Desktop | ![Desktop Super](documentation/features/user_accounts/desktop_super.png "Super User Menu Desktop") | ![Desktop Staff](documentation/features/user_accounts/desktop_staff.png "Staff User Menu Desktop") | ![Desktop User](documentation/features/user_accounts/desktop_user.png "User Menu Desktop") |

- ### Navigation

    **Note:** Tapping/clicking on the main title will bring you back to the home page on both mobile and desktop versions.

    ### Mobile
    Navigation on mobile devices is found at the bottom of the view for easy access without compromising what the user can see. The standard navigation bar as the following options:
    - Account Menu
    - Site Navigation
    - Basket Preview

    ![Standard Mobile Navbar](documentation/features/navigation/mobile_standard_nav.png "Standard Mobile Navbar")

    With an additional option when on the products page:
    - Sort, Filter, and Search
    
    ![Products Mobile Navbar](documentation/features/navigation/mobile_products_nav.png "Products Mobile Navbar")
    
    Each is accessed by tapping the appropriate icon.

    | Account Menu | Site Navigation | Sort, Filter and Search | Basket Preview |
    | --- | --- | --- | --- |
    | ![Mobile Account Menu](documentation/features/navigation/mobile_account_menu.png "Mobile Account Menu") | ![Mobile Site Navigation](documentation/features/navigation/mobile_navigation_menu.png "Mobile Site Navigation") |  ![Mobile Sort, Filter, Search](documentation/features/navigation/mobile_sort_filter.png "Mobile Sort, Filter, and Search") | ![Mobile Basker Preview](documentation/features/navigation/mobile_basket_preview.png "Mobile Basket Preview") |

    ### Desktop
    Navigation on desktop devices is found at the top of the screen in the hero image and title banner. Site navigation is located at the top left which is expanded by clicking on the burger menu icon. The account menu is opened by clicking on the wizard hat and the basket icon will open the basket preview panel.

    ![Desktop Navbar](documentation/features/navigation/desktop_navigation_icons.png "Desktop Navbar")

    | Account Menu | Site Navigation | Basket Preview |
    | --- | --- | --- |
    | ![Desktop Account Menu](documentation/features/navigation/desktop_account_menu.png "Desktop Account Menu") | ![Desktop Site Navigation](documentation/features/navigation/desktop_navigation_menu.png "Desktop Site Navigation") | ![Desktop Basket Preview](documentation/features/navigation/desktop_basket_preview.png "Desktop Basket Preview") |

    To ensure easy navigation for desktop users on pages that may require a lot of scrolling, a floating menu becomes active once the page is scrolled past the hero banner. It appears when the user scrolls up slightly and remains visible until the page is scrolled back to the top, where it seamlessly fades into the main menu.

    ![Dynamic Floating Menu](documentation/features/navigation/dynamic_navbar.gif "Dynamic Desktop Navbar")

    **Note:** Both mobile and desktop site navigation menus also feature a dropdown so that the user can select a specific realm to browse.

- ### Hero Image and Title
    The hero image and title remain in the same place throughout the site. It is responsive and the title is dynamic so changes depending on what page is being viewed. For desktop views the navigation, account, and basket menus are also part of the title banner.

    | Mobile | Desktop |
    | --- | --- |
    | ![Mobile Hero](documentation/features/hero/mobile_hero.png "Mobile Hero") | ![Desktop Hero](documentation/features/hero/desktop_hero.png "Desktop Hero") |

    |  | FAQs | Contact Us | Newsletter | Returns Policy | Privacy Policy | T&Cs | Dashboard |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | Mobile | ![Mobile FAQs](documentation/features/hero/mobile_faqs.png "Mobile FAQs") | ![Mobile Contact](documentation/features/hero/mobile_contact.png "Mobile Contact") | ![Mobile Newsletter](documentation/features/hero/mobile_newsletter.png "Mobile Newsletter") | ![Mobile Returns](documentation/features/hero/mobile_returns.png "Mobile Returns") | ![Mobile Privacy](documentation/features/hero/mobile_privacy.png "Mobile Privacy") | ![Mobile Terms](documentation/features/hero/mobile_terms.png "Mobile Terms") | ![Mobile Dashboard](documentation/features/hero/mobile_dashboard.png "Mobile Dashboard") |
    | Desktop | ![Desktop FAQs](documentation/features/hero/desktop_faqs.png "Desktop FAQs") | ![Desktop Contact](documentation/features/hero/desktop_contact.png "Desktop Contact") | ![Desktop Newsletter](documentation/features/hero/desktop_newsletter.png "Desktop Newsletter") | ![Desktop Returns](documentation/features/hero/desktop_returns.png "Desktop Returns") | ![Desktop Privacy](documentation/features/hero/desktop_privacy.png "Desktop Privacy") | ![Desktop Terms](documentation/features/hero/desktop_terms.png "Desktop Terms") | ![Desktop Dashboard](documentation/features/hero/desktop_dashboard.png "Desktop Dashboard") |

- ### Info Section & Footer
    The footer is found on every page with a simple copyright. The info section can be found accompanying the footer on all pages except for staff dashboard pages
    
    | Mobile | Tablet | Desktop |
    | --- | --- | --- |
    | ![Mobile Info Bar](documentation/features/footer_and_info/mobile_info.png "Mobile Info Bar") | ![Tablet Info Bar](documentation/features/footer_and_info/tablet_info.png "Tablet Info Bar") | ![Desktop Info Bar](documentation/features/footer_and_info/desktop_info.png "Desktop Info Bar") |
    
    The info section consists of three separate responsive sections:
    - **Newsletter quick sign up:** provides users a quick and simple way to sign up to the newsletter.
    - **Social media links:** provides links to the sites social media account pages.
    - **Helpful site links:** provides the user easy access to the main site pages.
    <br>
    <br>
    > [!NOTE]  
    > The links for Instagram and X just point to the social media platforms homepage as there is not account for Treasures Untold on these platforms at this time. The facebook link should take the user to the Facebook business page if it is still active.

- ### Scroll Button
    For pages that require a lot of scrolling there is a scroll button that will appear after the page has scrolled past the main hero banner. Tapping or clicking on this button will gracefully take the user back to the top of the page.

    | The Scroll Button |
    | :---: |
    | ![Scroll Button](documentation/features/scroll_button/scroll_button.png "Scroll Button") |

    | Mobile | Desktop |
    | --- | --- |
    | ![Mobile Scrolling](documentation/features/scroll_button/mobile_scroll.gif "Mobile Scrolling") | ![Desktop Scrolling](documentation/features/scroll_button/desktop_scroll.gif "Desktop Scrolling") |

- ### Homepage
    The homepage has four main elements:
    - Welcome Message
    - New products slideshow
    - As seen in banner
    - Featured Realm slideshow

    **Welcome Message**
    
    A short welcome messages to the site with a link to view all products. If the user is logged in it will address them by their username instead of 'Traveler'.

    ![Welcome Message](documentation/features/homepage/homepage_welcome.png "Welcome message")

    **New Products**

    This section showcases the latest products added to the store's inventory. If there is more then one item, the image will transition in a slideshow looping through all of the new items. The user can either tap/click on the image or link to take them to the products view filtered to show new products.

    ![New Products](documentation/features/homepage/homepage_new.png "New items showcase")

    **As Seen In**

    This scrolling banner showcases where Treasures Untold has been featured in.

    ![As seen in banner](documentation/features/homepage/homepage_marquee.gif "As seen in")

    **Featured Realm**

    This section highlights a particular realm and shows the items from that realm in the slideshow. Tapping/clicking on the image or link will take the user to view the products from that realm. This feature is refreshed every time the page loads to show a different realm.

    ![Featured Realm](documentation/features/homepage/homepage_featured.png "Featured Realm")

- ### Viewing Products
    Products are displayed in a responsive layout, allowing users to easily search for specific products or keywords. They can also sort and filter the results to refine their search. Filtering can be applied to show items by realm, stock level and new products. The user is notified of what products are being shown at the top. Search, sort and filter actions can be combined together, for example you can search for 'hook' and then filter and sort those results further. Searches also look for matches in the product description.

    The filter, sort and search functions for mobile can be found in the extra filter menu on the navigation bar at the bottom of the view. For desktop users, the sort and filter controls are to the left of the displayed products and the search bar can be found in the navigation panel accessed via the burger menu icon.

    To clear all searches, sort orders or filters the user can tap/click on the clear button to show all products again.

    Any items that are out of stock or sold are shown at the bottom of the page, their image is desaturated and the price is replaced with the text 'SOLD' if the item is unique or 'OUT OF STOCK' if not.

    To view a product in more detail the user can tap/click on the product image. Products that are sold or out of stock can still be viewed in more detail.

    | Mobile | Desktop |
    | --- | --- |
    | ![Mobile Products View](documentation/features/viewing_products/mobile_all_products.png "Mobile products view") | ![Desktop Products View](documentation/features/viewing_products/desktop_all_products.png "Desktop all products") |

    |  | Mobile | Desktop |
    | --- | --- | --- |
    | Search Results | ![Mobile search products](documentation/features/viewing_products/mobile_search_results.png "Mobile search products") | ![Desktop search products](documentation/features/viewing_products/desktop_search_results.png "Desktop search products") |
    | Sort Results | ![Mobile sort products](documentation/features/viewing_products/mobile_sort_results.png "Mobile sort products") | ![Desktop sort products](documentation/features/viewing_products/desktop_sort_results.png "Desktop sort products") |
    | Filter Results | ![Mobile filter products](documentation/features/viewing_products/mobile_filter_results.png "Mobile filter products") | ![Desktop filter products](documentation/features/viewing_products/desktop_filter_results.png "Desktop filter products") |
    | Combined Results | ![Mobile combined products](documentation/features/viewing_products/mobile_combined.png "Mobile combined products") | ![Desktop combined products](documentation/features/viewing_products/desktop_combined.png "Desktop combined products") |
    | No Results | ![Mobile no products](documentation/features/viewing_products/mobile_no_results.png "Mobile no products") | ![Desktop no products](documentation/features/viewing_products/desktop_no_results.png "Desktop no products") |
    | Sold Items | ![Mobile sold products](documentation/features/viewing_products/mobile_sold.png "Mobile sold products") | ![Desktop sold products](documentation/features/viewing_products/desktop_sold.png "Desktop sold products") |

- ### Viewing Product Details
    By tapping/clicking on a products image the user is show the product in more detail including:
    - Larger image
    - Name
    - Realm (also a link to show all products from that realm)
    - Product Description
    - Cost
    - Availablity
    - A quantity input if the item is not unique
    - If the user is logged in an 'Add to Basket' button is shown otherwise 'Log In' and 'Sign Up' buttons are shown. With a message to say you need to log in to add items to the basket.
    - A live timer counting down to 5pm local time for same day dispatch. If the time is past 5pm, the timer then counts to 5pm the following day and the message changes appropriately.
    - A button to return to the previous product page, this includes any search, sort or filters that were active at the time.

    |  | Product Detail Guest View | Product Detail User View - Unique Product | Product Detail User View - Non Unique Product |
    | --- | --- | --- | --- |
    | Mobile | ![Mobile guest details](documentation/features/product_details/mobile_detail_logged_off.png "Mobile guest view") | ![Mobile unique view](documentation/features/product_details/mobile_detail_unique.png "Mobile unique view") |![Mobile stocked view](documentation/features/product_details/mobile_detail_stocked.png "Mobile stocked view") |
    | Desktop | ![Desktop guest details](documentation/features/product_details/desktop_detail_logged_off.png "Desktop guest view") | ![Desktop unique view](documentation/features/product_details/desktop_detail_unique.png "Desktop unique view") |![Desktop stocked view](documentation/features/product_details/desktop_detail_stocked.png "Desktop stocked view") |

- ### Adding Products to the Basket
    To add an item to the basket a user simply taps/clicks on the 'Add to Basket' button on the product detail page. If the product is not unique the user can specify the quantity required in the input field by either typing or using the plus/minus buttons. When the user adds the product to their basket, the page is updated to reflect any stock changes and availability.

    | Unique Product Availability Adjusting | Product Quantity Adjusting | Product Quantity Zero Adjusting |
    | --- | --- | --- |
    | ![Product Adjusting Availability](documentation/features/product_details/unique_product_updating.gif "Product updating availability") | ![Product Adjusting Quantity](documentation/features/product_details/stocked_product_updating.gif "Product updating quantity") | ![Product Adjusting Quantity to Zero](documentation/features/product_details/stocked_product_zero.gif "Product updating quantity to zero") |

- ### Viewing and Editing the Basket
    Users can view their baskets in two ways. Via the basket preview or the basket page.
    
    **Basket Preview**
    The basket preview is easily accessible from any page via the basket icon on both mobile and desktop navigation. When expanded it provides a summary of the basket contents including:
    - Products with image, name, sku and quantity with total cost for that product
    - Current subtotal
    - Delivery cost
    - Current Grand total

    It also shows any current rewards or discounts that have been activated and updated totals/costs.
    There is also a button to open the basket page and another to proceed straight to the secure checkout.

    | Mobile Basket Preview | Desktop Basket Preview |
    | --- | --- |
    | ![Mobile Basket Preview](documentation/features/basket_view/mobile_basket_preview.png "Mobile basket preview") | ![Desktop Basket Preview](documentation/features/basket_view/desktop_basket_preview.png "Desktop basket preview") |

    **Basket Page**
    The basket page shows everything that the preview does with the additions of:
    - Product cost each
    This page is also where a user can also edit the contents of their basket before proceeding to the secure checkout. For each line item the user can:
    - Remove the product from the basket using the bin icon
    - If the product is not unique, the quantity required can also be adjusted. To confirm the adjustment the refresh icon must be tapped/clicked which is situated next to the quantity adjuster. Adjusting the quantity to 0 will remove the product from the basket.

    This page shows two buttons at the bottom, one to contine shopping which navigates to the products page, the other is to proceed to secure checkout.

    | Mobile Basket Page | Desktop Basket Page |
    | --- | --- |
    | ![Mobile Basket Page](documentation/features/basket_view/mobile_basket_page.png "Mobile basket page") | ![Desktop Basket Page](documentation/features/basket_view/desktop_basket_page.png "Desktop basket page") |

- ### Secure Checkout
    When users are ready to checkout, they are directed to the checkout page. Here they are presented with a from to complete for delivery and payment details along with a summary of the items they are buying.
    
    The order summary is in the same format as the basket preview described above.

    The Payment and Delivery section is split into three sub sections:
    - Contact Details
    - Delivery
    - Payment

    The contact and delivery sections will be prefilled with any details currently saved in the user's profile page with a checkbox option to save any details added or amended during the checkout process (any email change will not be saved, this will always default to the users email defined for their account).

    When the user has completed the form they can then click on the 'Complete Order' button to complete payment via Stripe. On a successul payment they will be taken to the order confirmation page. If any errors occur the user will be notified and any corrections can be made before attempting payment again.

    The user also has the option to go back to the edit basket page directly from the checkout page should they see something they need to change before proceeding.

    | Mobile Checkout | Desktop Checkout |
    | --- | --- |
    | ![Mobile Checkout](documentation/features/checkout_view/mobile_checkout.png "Mobile Checkout") | ![Desktop Checkout](documentation/features/checkout_view/desktop_checkout.png "Desktop Checkout") |

- ### Order Processing
    When a user submits their order for payment, a processing overlay is displayed before either going back to the checkout page if there was an error, or continuing to the confirmation page. This encourages the user to be patient while the transaction is processed as it gives them a visual indication of something happening. 

    ![Processinf Overlay](documentation/features/checkout_view/processing_overlay.gif "Processing overlay")

- ### Order Confirmation
    Upon completing a successful order, the user is directed to a confirmation page. This page informs them that a confirmation email will be sent to the provided address and includes a link to the contact page in case they need to report any issues. Additionally, it displays the following details of their purchase:
    - Order Number
    - Date
    - Contact and Delivery details provided during checkout
    - Order summary including any activated rewards and relevant price adjustments

    There are two buttons at the bottom of the page, one to go straight to the users profile page, the other to continue shopping which goes to the products page.

    | Checkout Success Mobile | Checkout Success Desktop |
    | --- | --- |
    | ![Mobile Checkout Success](documentation/features/checkout_view/mobile_checkout_success.png "Mobile checkout success") | ![Desktop Checkout Success](documentation/features/checkout_view/desktop_checkout_success.png "Desktop checkout success") |

    | Example Confirmation Email |
    | --- |
    | ![Confirmation Email](documentation/features/checkout_view/checkout_success_email.png "Example confirmation email") |
    
- ### User Profile Page
    Registered users can access a profile page where they can view their order history and also update their details that are used for orders during checkout.

    To update their details, users can enter new details into the form and tap/click on the submit button.

    | Mobile Profile Page | Desktop Profile Page |
    | --- | --- |
    | ![Mobile Profile Page](documentation/features/profile_page/mobile_profile_page.png "Mobile profile page") | ![Desktop Profile Page](documentation/features/profile_page/desktop_profile_page.png "Desktop profile page") |

    To view details of previous orders, users can tap/click on the relevant order number shown in the table to bring up details of that order.

    | Mobile Order History View | Desktop Order History View |
    | --- | --- |
    | ![Mobile Order History](documentation/features/profile_page/mobile_order_history.png "Mobile Order History") | ![Desktop Order History](documentation/features/profile_page/desktop_order_history.png "Desktop order history") |

- ### Support and Help Pages
    Tresures Untold has the following support pages for users which can be accessed via the navigation menus or the links at the bottom of each page:
    - FAQs
    - Contact Us
    - Newsletter
    - Returns Policy
    - Privacy Statement
    - Terms and Conditions

    ### FAQs
    This page offers a comprehensive FAQ section, covering a variety of topics to help users find the information they need.

    | Mobile FAQ | Mobile FAQ Expanded | Desktop FAQ | Desktop FAQ Expanded |
    | --- | --- | --- | --- |
    | ![Mobile FAQ](documentation/features/support_pages/mobile_faq_collapsed.png "Mobile FAQ") | ![Mobile FAQ Expanded](documentation/features/support_pages/mobile_faq_expanded.png "Mobile FAQ expanded") | ![Desktop FAQ](documentation/features/support_pages/desktop_faq_collapsed.png "Desktop FAQ") | ![Desktop FAQ Expanded](documentation/features/support_pages/desktop_faq_expanded.png "Desktop FAQ expanded") |

    ### Contact Us
    This page allows users to easily contact the staff/admin of Treasures Untold by submitting a message. To do so, users simply fill out a form with their name, email address, and message. Once submitted, a unique ticket number is generated, and an acknowledgment email is sent to the provided address. Users are then redirected to a thank you page outlining the next steps. The submitted message is accessible to staff members via the dashboard, where they can review and respond accordingly.

    | Mobile Contact Us | Desktop Contact Us |
    | --- | --- |
    | ![Mobile Contact Us](documentation/features/support_pages/mobile_contact_us.png "Mobile contact us") | ![Desktop Contact Us](documentation/features/support_pages/desktop_contact_us.png "Desktop contact us") |

    | Mobile Contact Us Thank You | Desktop Contact Us Thank You |
    | --- | --- |
    | ![Mobile Contact Us Thank You](documentation/features/support_pages/mobile_contact_thanks.png "Mobile contact us thanks") | ![Desktop Contact Us Thank You](documentation/features/support_pages/desktop_contact_thanks.png "Desktop contact us thanks") |

    | Example Acknowledgement Email |
    | --- |
    | ![Example Acknowledgement Email](documentation/features/support_pages/contact_example_acknowledgement_email.png "Example acknowledgement email") |

    ### Newsletter
    Users can sign up to receive the Treasures Untold newsletter by entering their email into the newsletter form at the bottom of most pages or from the dedicated newsletter page which is accessed via the navigation menus or the links at the bottom of each page.

    | Newsletter Form | Mobile Newsletter Page | Desktop Newsletter Page |
    | --- | --- | --- |
    | ![Newsletter Form](documentation/features/support_pages/newsletter_form_section.png "Newsletter Form") | ![Mobile Newsletter Page](documentation/features/support_pages/mobile_newsletter_page.png "Mobile newsletter page") | ![Desktop Newsletter Page](documentation/features/support_pages/desktop_newsletter_page.png "Desktop newsletter page") |

    Upon submitting the form the user is given a message informing them that they will receive an email for them to confirm their subsription.

    | Acknowledgement Message |
    | --- |
    | ![Acknowledgement Message](documentation/features/support_pages/newsletter_message.png "Newsletter message") |

    A unique token is generated to create a confirmation link, which is then sent to the user. They are informed that the link is valid for 24 hours, after which it will expire if not used to confirm the subscription.

    | Confirmation Email |
    | --- |
    | ![Confirmation Email](documentation/features/support_pages/newsletter_email.png "Confirmation email") |

    If the user clicks the link within 24 hours, they are redirected to a success page, and their status is set to active, allowing them to receive newsletter emails. If the token has expired, they are shown an expiration message and directed to the newsletter page to re-subscribe.

    | Mobile Newsletter Success | Desktop Newsletter Success | Expired Token Message |
    | --- | --- | --- |
    | ![Mobile Newsletter Success](documentation/features/support_pages/mobile_newsletter_success.png "Mobile newsletter success") | ![Desktop Newsletter Success](documentation/features/support_pages/desktop_newsletter_success.png "Desktop newsletter success") | ![Expired Token](documentation/features/support_pages/newsletter_expired_message.png "Expired token message") |

    Newsletters can be sent to all active email subscribers through the staff dashboard. Users can unsubscribe at any time by:
    - Clicking the unique unsubscribe link at the bottom of each newsletter.
    - Requesting removal via the contact form, which staff can process through the dashboard.

    If a user unsubscribes via the email link, they are redirected to the homepage with a confirmation message.

    | Example Newsletter | Unsubscribe Message |
    | --- | --- |
    | ![Example Newsletter](documentation/features/support_pages/example_newsletter.png "Example Newsletter") | ![Unsubscription Message](documentation/features/support_pages/unsubscribe_message.png "Unsubscription Message") |

    ### Returns Policy
    This page displays the return policy for Treasures Untold.

    | Mobile Returns Policy | Desktop Returns Policy |
    | --- | --- |
    | ![Mobile Returns Policy](documentation/features/support_pages/mobile_returns_policy.png "Mobile Returns Policy") | ![Desktop Returns Policy](documentation/features/support_pages/desktop_returns_policy.png "Desktop Returns Policy") |

    ### Privacy Statement
    This page displays the privacy statement for Treasures Untold.

    | Mobile Privacy Statement | Desktop Privacy Statement |
    | --- | --- |
    | ![Mobile Privacy Statement](documentation/features/support_pages/mobile_privacy.png "Mobile Privacy Statement") | ![Desktop Privacy Statement](documentation/features/support_pages/desktop_privacy.png "Desktop Privacy Statement") |

    ### Terms and Conditions
    This page displays the terms and conditions for Treasures Untold.

    | Mobile Terms and Conditions | Desktop Terms and Conditions |
    | --- | --- |
    | ![Mobile Terms and Conditions](documentation/features/support_pages/mobile_terms.png "Mobile Terms and Conditions") | ![Desktop Terms and Conditions](documentation/features/support_pages/desktop_terms.png "Desktop Terms and Conditions") |

- ### Error Pages
    The 404 error page in Treasures Untold features a themed message, gently informing users that the page they seek is lost in the magical realms. It provides navigation options to help them find their way back.

    | Mobile 404 | Desktop 404 |
    | --- | --- |
    | ![Mobile 404](documentation/features/error_pages/mobile_404.png "Mobile 404 Page") | ![Desktop 404](documentation/features/error_pages/desktop_404.png "Desktop 404 Page") |

    The 500 error page maintains the enchanted theme while reassuring users that something has gone wrong on our end. It offers guidance on what to do next and encourages them to try again later.

    | Mobile 500 | Desktop 500 |
    | --- | --- |
    | ![Mobile 500](documentation/features/error_pages/mobile_500.png "Mobile 500 Page") | ![Desktop 500](documentation/features/error_pages/desktop_500.png "Desktop 500 Page") |

- ### Staff Dashboard
    The staff dashboard is an area of the site with access reserved for users with a level of **staff** or **super user**. This is where shop owners can manage the day to day admin of the site, the page is split into four sections:
    - [Product Admin](#product-admin): This is where products can be created, updated and deleted. Product realms can also be managed here too.
    - [FAQ Admin](#faq-admin): FAQs can be created, updated and deleted here, including FAQ topics.
    - [Message Admin](#message-admin): This is where messages sent via the contact us page can be viewed, replied to and deleted.
    - [Newsletter Admin](#newsletter-admin): Staff can create and send newsletters here, they can also read and delete previously sent newsletters. The current list of subscribers and their status is also manageable here.<br><br>

    |  | Product Admin | FAQ Admin | Message Admin | Newsletter Admin |
    | --- | --- | --- | --- | --- |
    | Mobile | ![Mobile Product Admin](documentation/features/dashboard/mobile_product_admin.png "Mobile Product Admin") | ![Mobile FAQ Admin](documentation/features/dashboard/mobile_faq_admin.png "Mobile faq admin") | ![Mobile Message Admin](documentation/features/dashboard/mobile_message_admin.png "Mobile message admin") | ![Mobile Newsletter Admin](documentation/features/dashboard/mobile_newsletter_admin.png "Mobile newsletter admin") |
    | Desktop | ![Desktop Product Admin](documentation/features/dashboard/desktop_product_admin.png "Dektop product admin") | ![Desktop FAQ Admin](documentation/features/dashboard/desktop_faq_admin.png "Desktop faq admin") | ![Desktop Message Admin](documentation/features/dashboard/desktop_message_admin.png "Desktop message admin") | ![Desktop Newsletter Admin](documentation/features/dashboard/desktop_newsletter_admin.png "Desktop newsletter admin") | 

    ### Product Admin
    The products and realms are displayed in table format that is responsive showing details relevant to display size. Both products and realms can be managed separately here.

    - ### Products
    | Products |
    | :---: |
    | ![Products](documentation/features/dashboard/product_admin/products.png "Products") |

    When the green plus icon is clicked, a prompt is displayed with the input form to create a new product with the following fields:
    - Name
    - Realm
    - Description
    - Price
    - Stock

    All the above criteria are required to create a new product, additionally the product can be set as unique via the checkbox and an image can be uploaded using the 'Select New Image' button.
    
    Any selected image will then be shown and if no image is selected, a placeholder is used.

    If adding a new product requires the creation of a new realm, you can easily do so through the same form. Simply select ‘Add New Realm’ in the realm selector. This will reveal an input field for entering the new realm’s name. Additionally, there is a checkbox to indicate whether the realm name should include a prefix of ‘The’ in specific grammatical contexts (e.g., ‘The Enchanted Forest’ — where the realm is named Enchanted Forest, but the article ‘The’ is used in certain instances).

    The user can then save the new product by tapping/clicking on the 'Add' button or cancel and return to the dashboard with the 'Cancel' or modal close button.

    | Mobile Product Creation | Desktop Product Creation |
    | :---: | :---: |
    | ![Mobile Product Creation](documentation/features/dashboard/product_admin/mobile_product_add.png "Mobile product creation") | ![Desktop Product Creation](documentation/features/dashboard/product_admin/desktop_product_add.png "Desktop product creation") |

    When the yellow edit icon is tapped/clicked, a prompt is displayed prefilled with the selected products details. These can be edited in the same manner as the creation of a new product. If a new image is selected, a preview of the chosen file will show next to the current image.

    The user can then save the product by tapping/clicking on the 'Update' button or cancel and return to the dashboard with the 'Cancel' or modal close button.

    | Mobile Product Update | Desktop Product Update |
    | :---: | :---: |
    | ![Mobile Product Update](documentation/features/dashboard/product_admin/mobile_product_update.png "Mobile product update") | ![Desktop Product Update](documentation/features/dashboard/product_admin/desktop_product_update.png "Desktop product update") |

    When the red bin icon is tapped/clicked, a prompt is displayed asking the user to confirm the deletion of the selected product.

    The user can the confirm the deletion by tapping/clicking the 'Delete' button or cancel and return to the dashboard with the 'Cancel' or modal close button.

    | Mobile Product Delete | Desktop Product Delete |
    | :---: | :---: |
    | ![Mobile Product Delete](documentation/features/dashboard/product_admin/mobile_product_delete.png "Mobile product delete") | ![Desktop Product Delete](documentation/features/dashboard/product_admin/desktop_product_delete.png "Desktop product delete") |

    - ### Realms
    | Realms |
    | :---: |
    | ![Realms](documentation/features/dashboard/product_admin/realms.png "Realms") |

    Tapping/clicking on the green plus icon in the realm table displays the new realm prompt. The user can enter the name of the new realm here. Additionally, there is a checkbox to indicate whether the realm name should include a prefix of ‘The’ in specific grammatical contexts (e.g., ‘The Enchanted Forest’ — where the realm is named Enchanted Forest, but the article ‘The’ is used in certain instances).

    The user can then save the new realm by tapping/clicking on the 'Add' button or cancel and return to the dashboard with the 'Cancel' or modal close button.

    | Mobile Realm Creation | Desktop Realm Creation |
    | :---: | :---: |
    | ![Mobile Realm Creation](documentation/features/dashboard/product_admin/mobile_realm_add.png "Mobile realm creation") | ![Desktop Realm Creation](documentation/features/dashboard/product_admin/desktop_realm_add.png "Desktop realm creation") |
    
    When the yellow edit icon is tapped/clicked, a prompt is displayed prefilled with the selected realms details. These can be edited in the same manner as the creation of a new realm. The user will also be informed of how many products will be affected by this change.

    The user can then save the realm by tapping/clicking on the 'Update' button or cancel and return to the dashboard with the 'Cancel' or modal close button.

    | Mobile Realm Update | Desktop Realm Update |
    | :---: | :---: |
    | ![Mobile Realm Update](documentation/features/dashboard/product_admin/mobile_realm_update.png "Mobile realm update") | ![Desktop Realm Update](documentation/features/dashboard/product_admin/desktop_realm_update.png "Desktop realm update") |

    When the red bin icon is tapped/clicked, a prompt is displayed asking the user to confirm the deletion of the selected realm. The user will also be informed of how many products will be affected by this deletion.

    The user can the confirm the deletion by tapping/clicking the 'Delete' button or cancel and return to the dashboard with the 'Cancel' or modal close button.

    | Mobile Realm Delete | Desktop Realm Delete |
    | :---: | :---: |
    | ![Mobile Realm Delete](documentation/features/dashboard/product_admin/mobile_realm_delete.png "Mobile realm delete") | ![Desktop Realm Delete](documentation/features/dashboard/product_admin/desktop_realm_delete.png "Desktop realm delete") |

    ### FAQ Admin
    The FAQs and topics are displayed in table format that is responsive showing details relevant to display size. Both FAQs and topics can be managed separately here.

    - ### FAQs
    | FAQs |
    | :---: |
    | ![FAQs](documentation/features/dashboard/faq_admin/faqs.png "FAQs") |

    To create a a FAQ the green plus icon is tapped/clicked, a prompt is displayed with the input form to create a new FAQ with the following fields:
    - Topic
    - Question
    - Answer

    All the above criteria are required to create a new FAQ
    
    If adding a new FAQ requires the creation of a new topic, you can easily do so through the same form. Simply select ‘Add New Topic' in the topic selector. This will reveal an input field for entering the new topic.

    The user can then save the new FAQ by tapping/clicking on the 'Add' button or cancel and return to the dashboard with the 'Cancel' or modal close button.

    | Mobile FAQ Creation | Desktop FAQ Creation |
    | :---: | :---: |
    | ![Mobile FAQ Creation](documentation/features/dashboard/faq_admin/mobile_faq_add.png "Mobile faq creation") | ![Desktop FAQ Creation](documentation/features/dashboard/faq_admin/desktop_faq_add.png "Desktop faq creation") |
    
    To update a FAQ the yellow edit icon is tapped/clicked. A prompt is displayed prefilled with the selected FAQ details. These can be edited in the same manner as the creation of a new FAQ.

    The user can then save the FAQ by tapping/clicking on the 'Update' button or cancel and return to the dashboard with the 'Cancel' or modal close button.

    | Mobile FAQ Update | Desktop FAQ Update |
    | :---: | :---: |
    | ![Mobile FAQ Update](documentation/features/dashboard/faq_admin/mobile_faq_update.png "Mobile faq update") | ![Desktop FAQ Update](documentation/features/dashboard/faq_admin/desktop_faq_update.png "Desktop faq update") |

    To delete a FAQ the red bin icon is tapped/clicked. A prompt is displayed asking the user to confirm the deletion of the selected FAQ.

    The user can the confirm the deletion by tapping/clicking the 'Delete' button or cancel and return to the dashboard with the 'Cancel' or modal close button.

    | Mobile FAQ Delete | Desktop FAQ Delete |
    | :---: | :---: |
    | ![Mobile FAQ Delete](documentation/features/dashboard/faq_admin/mobile_faq_delete.png "Mobile faq delete") | ![Desktop FAQ Delete](documentation/features/dashboard/faq_admin/desktop_faq_delete.png "Desktop faq delete") |

    - ### FAQ Topics
    | FAQ Topics |
    | :---: |
    | ![FAQ Topics](documentation/features/dashboard/faq_admin/topics.png "FAQ Topics") |

    Tapping/clicking on the green plus icon in the FAQ Topics table displays the new topic prompt. The user can enter the name of the new topic here.

    The user can then save the new topic by tapping/clicking on the 'Add' button or cancel and return to the dashboard with the 'Cancel' or modal close button.

    | Mobile Topic Creation | Desktop Topic Creation |
    | :---: | :---: |
    | ![Mobile Topic Creation](documentation/features/dashboard/faq_admin/mobile_topic_add.png "Mobile topic creation") | ![Desktop Topic Creation](documentation/features/dashboard/faq_admin/desktop_topic_add.png "Desktop topic creation") |

    To update a topic the user taps/clicks on the yellow edit icon. A prompt is displayed prefilled with the selected topic details. These can be edited in the same manner as the creation of a new topic. The user will also be informed of how many FAQs will be affected by this change.

    The user can then save the topic by tapping/clicking on the 'Update' button or cancel and return to the dashboard with the 'Cancel' or modal close button.

    | Mobile Topic Update | Desktop Topic Update |
    | :---: | :---: |
    | ![Mobile Topic Update](documentation/features/dashboard/faq_admin/mobile_topic_update.png "Mobile topic update") | ![Desktop Topic Update](documentation/features/dashboard/faq_admin/desktop_topic_update.png "Desktop topic update") |

    When the red bin icon is tapped/clicked, a prompt is displayed asking the user to confirm the deletion of the selected topic. The user will also be informed of how many FAQs will be affected by this deletion.

    The user can the confirm the deletion by tapping/clicking the 'Delete' button or cancel and return to the dashboard with the 'Cancel' or modal close button.

    | Mobile Topic Delete | Desktop Topic Delete |
    | :---: | :---: |
    | ![Mobile Topic Delete](documentation/features/dashboard/faq_admin/mobile_topic_delete.png "Mobile topic delete") | ![Desktop Topic Delete](documentation/features/dashboard/faq_admin/desktop_topic_delete.png "Desktop topic delete") |

    ### Message Admin
    Messages are grouped into two sections:
    - Unreplied
    - Replied

    The unreplied messages are shown at the top and are also ordered chronologically with the oldest messages at the top. This gives the staff a clear indication of which messages need replying to.

    Each message pane show the following information:
    - Unique ticket number
    - Name of sender
    - Email address of sender
    - Date the message was received
    - Message content

    If the message has been replied to the additional information is visible:
    - Date the reply was sent
    - Reply content<br><br>

    | Messages |
    | :---: |
    | ![Messages](documentation/features/dashboard/message_admin/messages.png "Messages") |

    To reply to a message the yellow reply icon is tapped/clicked. This will display a message prompt for the staff member to type in. They can then send this by tapping/clicking on the 'Reply' button or cancel and return to the dashboard by tapping/clicking on the 'Cancel' or modal close buttons.

    | Mobile Message Reply | Desktop Message Reply |
    | :---: | :---: |
    | ![Mobile Message Reply](documentation/features/dashboard/message_admin/mobile_message_reply.png "Mobile message reply") | ![Desktop Message Reply](documentation/features/dashboard/message_admin/desktop_message_reply.png "Desktop messsage reply") |

    Once a message reply has been created, an email will be sent to the original user who created the message and the message will be updated in the dashboard to reflect the replied status.

    | Example Reply Email |
    | :---: |
    | ![Example Reply Email](documentation/features/dashboard/message_admin/message_reply_email.png "Example reply email") |

    To delete a message the red bin icon can be tapped/clicked. A prompt asking the user to confirm will be displayed. The can then either tap/click on 'Delete' to confirm or return to the dashboard with the 'Cancel' or model close button.

    | Mobile Message Delete | Desktop Message Delete |
    | :---: | :---: |
    | ![Mobile Message Delete](documentation/features/dashboard/message_admin/mobile_message_delete.png "Mobile message delete") | ![Desktop Message Delete](documentation/features/dashboard/message_admin/desktop_message_delete.png "Desktop message delete") |

    ### Newsletter Admin
    The newsletter admin page is split into two sections:

    - ### Newsletters
    Staff can see a list of previously sent newsletters which they can view and delete. They can also create and send a newsletter.

    | Newsletters |
    | :---: |
    | ![Newsletters](documentation/features/dashboard/newsletter_admin/newsletters.png "Newsletters") |

    To create a newsletter the green plus icon is clicked. A prompt is then displayed with the input form to create a newsletter with the following fields:
    - Subject
    - ... (for content)

    To send the newsletter the user taps/clicks on the 'Send' button. An email is then sent to every active subscriber in the list. Newsletter creation can also be cancelled using the 'Cancel' or modal close button to return to the dashboard.

    | Mobile Newsletter Creation | Desktop Newsletter Creation |
    | :---: | :---: |
    | ![Mobile Newsletter Creation](documentation/features/dashboard/newsletter_admin/mobile_newsletter_send.png "Mobile newsletter send") | ![Desktop Newsletter Send](documentation/features/dashboard/newsletter_admin/desktop_newsletter_send.png "Desktop Newsletter Send") |

    | Example Newsletter |
    | :---: |
    | ![Example Newsletter](documentation/features/support_pages/example_newsletter.png "Example Newsletter") |

    Previously sent newsletters can also be viewed by tapping/clicking on the blue open icon next to each newsletter. This will open the newsletter in a prompt. This can be closed with the 'Close' or modal close button to return to the dashboard.

    | Mobile Newsletter View | Desktop Newsletter View |
    | :---: | :---: |
    | ![Mobile Newsletter View](documentation/features/dashboard/newsletter_admin/mobile_newsletter_view.png "Mobile newsletter view") | ![Desktop Newsletter View](documentation/features/dashboard/newsletter_admin/desktop_newsletter_view.png "Desktop newsletter view") |

    Newsletters can also be deleted by tapping/clicking on the red bin icon. A prompt will be displayed to confirm the deletion. To confirm deletion the user must tap/click on the 'Delete' button. This can be cancelled with the 'Cancel' or modal close buttons to return to the dashboard.

    | Mobile Newsletter Delete | Desktop Newsletter Delete |
    | :---: | :---: |
    | ![Mobile Newsletter Delete](documentation/features/dashboard/newsletter_admin/mobile_newsletter_delete.png "Mobile newsletter delete") | ![Desktop Newsletter Delete](documentation/features/dashboard/newsletter_admin/desktop_newsletter_delete.png "Desktop newsletter delete") |

    - ### Subscribers
    Staff can see the list of subscribers and their current status. This will be one of the following:

    - **ACTIVE**: The user has confirmed their subscription by clicking on the link in the email sent to them when signing up. They will receive newsletters.
    - **PENDING**: The user has not yet confirmed their subscription by clicking on the link. The token to activate their subscription is still valid. They will not recieve newsletters until they confirm their subscription.
    - **EXPIRED**: The user has not yet confirmed their subscription and the token has expired.<br><br>

    | Subscribers |
    | :---: |
    | ![Subscribers](documentation/features/dashboard/newsletter_admin/subscribers.png "Subscribers") |

    Staff members can remove individual subscribers by tapping/clicking the red bin icon next to their email address. A confirmation prompt will appear, displaying their current status. To proceed with removal, select ‘Remove.’ To cancel and return to the dashboard, simply click ‘Cancel’ or close the modal.

    |  | Remove Active Subscriber | Remove Pending Subscriber | Remove Expired Subscriber |
    | :---: | :---: | :---: | :---: |
    | Mobile | ![Mobile Remove Active Subscriber](documentation/features/dashboard/newsletter_admin/mobile_remove_active.png "Mobile remove active subscriber") | ![Mobile Remove Pending Subscriber](documentation/features/dashboard/newsletter_admin/mobile_remove_pending.png "Mobile remove pending subscriber") | ![Mobile Remove Expired Subscriber](documentation/features/dashboard/newsletter_admin/mobile_remove_expired.png "Mobile remove expired subscriber") |
    | Desktop | ![Desktop Remove Active Subscriber](documentation/features/dashboard/newsletter_admin/desktop_remove_active.png "Desktop remove active subscriber") | ![Desktop Remove Pending Subscriber](documentation/features/dashboard/newsletter_admin/desktop_remove_pending.png "Desktop remove pending subscriber") | ![Desktop Remove Expired Subscriber](documentation/features/dashboard/newsletter_admin/desktop_remove_expired.png "Desktop remove expired subscriber") |

    Staff members can also clear all current expired subscribers by tapping/clicking on the 'Clear Expired Subscribers' button. This will display a prompt listing all emails that are expired. To confirm removal the 'Clear' button can be tapped/clicked. To cancel and return to the dashboard, simply click ‘Cancel’ or close the modal.

    | Mobile Clear Expired | Desktop Clear Expired |
    | :---: | :---: |
    | ![Mobile Clear Expires Subscribers](documentation/features/dashboard/newsletter_admin/mobile_clear_expired.png "Mobile clear expired subscribers") | ![Desktop Clear Expired Subscribers](documentation/features/dashboard/newsletter_admin/desktop_clear_expired.png "Desktop clear expired subscribers") |

- ### Super User Privileges

- ### Communication to the User

- ### Easter Eggs

- ### Backend Features

- ### SEO & Marketing Features
    A full explanation of the [SEO & Marketing](#seo--marketing) features can be viewed in detail below.

- ### Heroku Deployment
    The site is deployed to Heroku, making it accessible online for users. More inforation on [deployment](#deployment) can be found below.

### Future Features

⚠️ INSTRUCTIONS ⚠️

Do you have additional ideas that you'd like to include on your project in the future? Fantastic, list them here! It's always great to have plans for future improvements. Consider adding any helpful links or notes to help remind you in the future, if you revisit the project in a couple years.

A few examples are listed below to align with possible ways to improve on the sample walkthrough project, to give you some inspiration.

⚠️ --- END ---⚠️

- **Product Reviews & Ratings**: Allow customers to leave reviews and rate products, with admin moderation. Display average ratings and review counts on product pages.
- **Wishlist Functionality**: Enable users to save products to a personal wishlist for future purchases. Notify users if wishlist items go on sale or are back in stock.
- **Product Recommendations**: Implement a "Customers who bought this also bought" or "You might also like" feature to suggest related products.
- **Live Chat Support**: Provide real-time customer support through an integrated live chat or chatbot.
- **Abandoned Cart Recovery**: Automatically send emails to users who add items to their cart but don't complete the purchase, offering discounts or reminders.
- **Discount Codes and Vouchers**: Allow the admin to create discount codes or vouchers for promotions and marketing campaigns.
- **Loyalty Program**: Introduce a points-based loyalty system where customers earn points for purchases, which can be redeemed for discounts.
- **Product Inventory Alerts**: Notify customers when out-of-stock items are back in stock, or when low inventory is approaching.
- **Multi-Currency and Multi-Language Support**: Expand the application to support multiple currencies and languages to reach a global audience.
- **Product Bundles**: Offer discounted product bundles (e.g., buy 3 for the price of 2) or custom product kits.
- **Social Media Integration**: Enable users to share products directly to social media platforms or implement a social login for quick account creation.
- **Shipping Tracking Integration**: Provide real-time shipping updates and tracking information directly within the user’s order history.
- **Advanced Analytics Dashboard for Admin**: Offer an in-depth dashboard that displays sales trends, popular products, customer behavior, and more.
- **Subscription-Based Products**: Allow users to subscribe to certain products (e.g., monthly deliveries of consumables like coffee or skincare products).
- **Product Video Demos**: Support product videos to better showcase features, especially for high-tech or complex items.
- **Mobile App**: Develop a mobile app for iOS and Android, providing users with a more optimized shopping experience on mobile devices.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) | Online secure payments of e-commerce products/services. |
| [![badge](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) | Sending emails in my application. |
| [![badge](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Canva-grey?logo=canva&logoColor=00C4CC)](https://www.canva.com/p/canvawireframes) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |

⚠️ NOTE ⚠️

Want to add more?

- Tutorial: https://shields.io/badges/static-badge
- Icons/Logos: https://simpleicons.org
  - FYI: not all logos are available to use

🛑 --- END --- 🛑

## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

![screenshot](documentation/erd.png)

⚠️ INSTRUCTIONS ⚠️

Using your defined models, create an ERD with the relationships identified. A couple of recommendations for building your own free ERDs:
- [Lucidchart](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning)
- [Draw.io](https://draw.io)

Looking for an interactive version of your ERD? Consider using a [`Mermaid flowchart`](https://mermaid.live). To simplify the process, you can ask ChatGPT (or similar) the following prompt:

> ChatGPT Prompt:
> "Generate a Markdown syntax Mermaid ERD using my Django models"
> [paste-your-django-models-into-ChatGPT]

The "Boutique Ado" sample ERD in Markdown syntax using Mermaid can be seen below as an example.

**NOTE**: A Markdown Preview tool doesn't show the interactive ERD; you must first commit/push the code to your GitHub repository in order to see it live in action.

⚠️ --- END --- ⚠️

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    User {
        int id PK
        varchar username
        varchar email
        varchar password
    }

    UserProfile {
        int id PK
        varchar default_phone_number
        varchar default_street_address1
        varchar default_street_address2
        varchar default_town_or_city
        varchar default_county
        varchar default_postcode
        varchar default_country
    }

    User ||--|| UserProfile : has_one

    Category {
        int id PK
        varchar name
        varchar friendly_name
    }

    Product {
        int id PK
        varchar sku
        varchar name
        text description
        bool has_sizes
        decimal price
        decimal rating
        varchar image_url
        image image
    }

    Product ||--o| Category : belongs_to

    Order {
        int id PK
        varchar order_number
        varchar full_name
        varchar email
        varchar phone_number
        varchar country
        varchar postcode
        varchar town_or_city
        varchar street_address1
        varchar street_address2
        varchar county
        datetime date
        decimal delivery_cost
        decimal order_total
        decimal grand_total
        text original_bag
        varchar stripe_pid
    }

    OrderLineItem {
        int id PK
        int quantity
        decimal lineitem_total
        varchar product_size
    }

    Order ||--o| OrderLineItem : has_many
    OrderLineItem ||--o| Product : belongs_to

    Order ||--o| UserProfile : belongs_to

    Newsletter {
        int id PK
        varchar email
    }

    Contact {
        int id PK
        varchar name
        varchar email
        text message
    }

    FAQ {
        int id PK
        varchar question
        text answer
    }
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqVVcFu2zAM_RVD57RIHLdpfRs6DBg2bB2GXYYAhmIxjlBZcimqqdvk3yfbSVPHceP5kBh8TyRFPtKvLDUCWMwAP0ueIc_nOvDPHwsYvDbv1SM1BVIE998OpieO6Ypj4DxV8xy6CORcqq654NauDYoG2c71IeQ9mqVUMDCygCV3ipJiZTQk2uULwH6WJQSghAuBYO1kKDHsJ5JZ68Rgkkoq-1mpcfojvDCWqiac8YDliXoFm83FxWbTql0crLhNfEX2xDtOkBksB1b1dC-XKEELVSYH-C0TH1m4lAb6tw_uXFCCZ_K3tynKgqTRB2RhjKrvZ-UL2INdQCpzroICZQpdM3KSOuuG9WAGicN3Kq1NzW_PNauam82hrHGwAGV0Zr0g9tyfKAYPkKm4vfJdOqWS_5uvD8ehJabWsV4dfqzzs3N1dp6OJ0T4ypLMoX7pNlOAkk-ApZ8LS124KScZ4qoL-g2nxTFYy82gzKTmKlnw7OQdZAFJIY-3Vt3o71LDV4L8TMMr06Pjmlp13KemvBPpnRxn99afRn618k8lsddlO6NmG-Rcl6fy3R3ZK7tfyTtie890yT9gbRUQDdb-Owm_3ebOaOKD18mg0ag7nHv1daf6y6dfAyM9OrDtbVS75dqu94O2ZSOWA_rgwn9Ta7dzRivwKbLYvwqOD3M21xWPOzK_S52ymNDBiLmikvvuK8ziJVfWWwuuWfzKnlk8jSaXN9ez8HoyHc_C8TiajVjJ4ovp5XUUTqMovLqdXd2Et-FsO2Ivxngfk8vxZBpGkT_m_zxW-_tbY01QNC5b7YJt_wE0ZoQj)

⚠️ RECOMMENDED ⚠️

Alternatively, or in addition to, a more comprehensive ERD can be auto-generated once you're at the end of your development stages, just before you submit. Follow the steps below to obtain a thorough ERD that you can include. Feel free to leave the steps below in the README for future use to yourself.

⚠️ --- END --- ⚠️

I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- drag the new `erd.png` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![screenshot](documentation/advanced-erd.png)

source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

## Agile Development Process

### GitHub Projects

⚠️ TIP ⚠️

Consider adding screenshots of your Projects Board(s), Issues (open and closed), and Milestone tasks.

⚠️ --- END ---⚠️

[GitHub Projects](https://www.github.com/apeskinian/p5_treasures_untold/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/apeskinian/p5_treasures_untold/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/apeskinian/p5_treasures_untold)](https://www.github.com/apeskinian/p5_treasures_untold/issues) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/apeskinian/p5_treasures_untold)](https://www.github.com/apeskinian/p5_treasures_untold/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCow" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Ecommerce Business Model

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss the business model for your e-commerce project. An example is provided below that aligns closely with **Boutique Ado's B2C** strategy. Be sure to align to your own project requirements.

⚠️ --- END --- ⚠️

This site sells goods to individual customers, and therefore follows a **Business to Customer** model. It is of the simplest **B2C** forms, as it focuses on individual transactions, and doesn't need anything such as monthly/annual subscriptions.

It is still in its early development stages, although it already has a newsletter, and links for social media marketing.

Social media can potentially build a community of users around the business, and boost site visitor numbers, especially when using larger platforms such a Facebook.

A newsletter list can be used by the business to send regular messages to site users. For example, what items are on special offer, new items in stock, updates to business hours, notifications of events, and much more!

## SEO & Marketing

### Keywords

I've identified some appropriate keywords to align with my site, that should help users when searching online to find my page easily from a search engine. This included a series of the following keyword types:

- Short-tail (head terms) keywords
- Long-tail keywords

I've also played around with [Word Tracker](https://www.wordtracker.com) a bit to check the frequency of some of my site's primary keywords (only until the free trial expired).

### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file. This was generated using my deployed site URL: https://apeskinian-treasures-untold-568a3e176ede.herokuapp.com

After it finished crawling the entire site, it created a [sitemap.xml](sitemap.xml), which I've downloaded and included in the repository.

### Robots

I've created the [robots.txt](robots.txt) file at the root-level. Inside, I've included the default settings:

```txt
User-agent: *
Disallow:
Sitemap: https://apeskinian-treasures-untold-568a3e176ede.herokuapp.com/sitemap.xml
```

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales. Using more popular providers with a wider user base, such as Facebook, typically maximizes site views.

I've created a mockup Facebook business account using the [Balsamiq template](https://code-institute-org.github.io/5P-Assessments-Handbook/files/Facebook_Mockups.zip) provided by Code Institute.

![screenshot](documentation/mockup-facebook.png)

### Newsletter Marketing

I have incorporated a newsletter sign-up form on my application, to allow users to supply their email address if they are interested in learning more. 

⚠️ OPTION 1: RECOMMENDED ⚠️

**Custom Django Model Newsletter**

- Create a custom `newsletter` app in your project, with a custom model/class called `Newsletter`.
- This method satisfies two assessment criteria:
    1. include a newsletter
    2. one of your 3 required custom models
- It doesn't need anything except the `email` field on the model, but feel free to add more if you need.
- Example: (keep this in your README if you've done this method, attach your `Newsletter` model in a code block like the following example)
    ```python
    class Newsletter(models.Model):
        email = models.EmailField(null=False, blank=False)

        def __str__(self):
            return self.email
    ```
- Consider using the same `send_mail()` functionality used on the `webhook_handler.py` file.
    - You can trigger an email to be sent out to subscribed users when new products are added to the site!

⚠️ --- END --- ⚠️

🛑 OPTION 2 🛑

**MailChimp Newsletter**

- Sign up for a Mailchimp account
- This allows up to 2,500 subscription email sends per month
- Incorporate the code and scripts into your project like in the Code Institute lessons.

🛑 --- END --- 🛑

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://apeskinian-treasures-untold-568a3e176ede.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

🛑 !!! ATTENTION apeskinian !!! 🛑

⚠️ DO NOT update the environment variables to your own! These should never be public; only use the demo values below! ⚠️

🛑 --- END --- 🛑

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user-inserts-own-aws-access-key-id |
| `AWS_SECRET_ACCESS_KEY` | user-inserts-own-aws-secret-access-key |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user-inserts-own-gmail-api-key |
| `EMAIL_HOST_USER` | user-inserts-own-gmail-email-address |
| `SECRET_KEY` | any-random-secret-key |
| `STRIPE_PUBLIC_KEY` | user-inserts-own-stripe-public-key |
| `STRIPE_SECRET_KEY` | user-inserts-own-stripe-secret-key |
| `STRIPE_WH_SECRET` | user-inserts-own-stripe-webhook-secret |
| `USE_AWS` | True |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://apeskinian-treasures-untold-568a3e176ede.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (*verify your password and account*)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords** (*search for it at the top, if not*).
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
    - Any custom name, such as "Django" or `p5_treasures_untold`
- You'll be provided with a 16-character password (API key).
    - Save this somewhere locally, as you cannot access this key again later!
    - If your 16-character password contains *spaces*, make sure to remove them entirely.
    - `EMAIL_HOST_PASS` = user's 16-character API key
    - `EMAIL_HOST_USER` = user's own personal Gmail email address

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

🛑 !!! ATTENTION apeskinian !!! 🛑

⚠️ DO NOT update the environment variables to your own! These should never be public; only use the demo values below! ⚠️

🛑 --- END --- 🛑

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user-inserts-own-aws-access-key-id")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user-inserts-own-aws-secret-access-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("EMAIL_HOST_PASS", "user-inserts-own-gmail-host-api-key")
os.environ.setdefault("EMAIL_HOST_USER", "user-inserts-own-gmail-email-address")
os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user-inserts-own-stripe-public-key")
os.environ.setdefault("STRIPE_SECRET_KEY", "user-inserts-own-stripe-secret-key")
os.environ.setdefault("STRIPE_WH_SECRET", "user-inserts-own-stripe-webhook-secret")  # only if using Stripe Webhooks

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/apeskinian/p5_treasures_untold).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/apeskinian/p5_treasures_untold.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/apeskinian/p5_treasures_untold)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/apeskinian/p5_treasures_untold).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss any differences between the local version you've developed, and the live deployment site. Generally, there shouldn't be [m]any major differences, so if you honestly cannot find any differences, feel free to use the following example:

⚠️ --- END --- ⚠️

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

⚠️ INSTRUCTIONS ⚠️

In the following sections, you need to reference where you got your content, media, and any extra help. It is common practice to use code from other repositories and tutorials (which is totally acceptable), however, it is important to be very specific about these sources to avoid potential plagiarism.

⚠️ --- END ---⚠️

### Content

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution links for any borrowed code snippets, elements, and resources. Ideally, you should provide an actual link to every resource used, not just a generic link to the main site. If you've used multiple components from the same source (such as Bootstrap), then you only need to list it once, but if it's multiple Codepen samples, then you should list each example individually. If you've used AI for some assistance (such as ChatGPT or Perplexity), be sure to mention that as well. A few examples have been provided below to give you some ideas.

⚠️ --- END ---⚠️

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [Boutique Ado](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [AWS S3](https://aws.amazon.com/s3) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Stripe](https://docs.stripe.com/payments/elements) | Online payment services |
| [Gmail API](https://developers.google.com/gmail/api/guides) | Sending payment confirmation emails |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution links to any media files borrowed from elsewhere (images, videos, audio, etc.). If you're the owner (or a close acquaintance) of some/all media files, then make sure to specify this information. Let the assessors know that you have explicit rights to use the media files within your project. Ideally, you should provide an actual link to every media file used, not just a generic link to the main site, unless it's AI-generated artwork.

Looking for some media files? Here are some popular sites to use. The list of examples below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links by sending yourself (or Slackbot) the following command: `!freemedia`.

- Images
    - [Pexels](https://www.pexels.com)
    - [Unsplash](https://unsplash.com)
    - [Pixabay](https://pixabay.com)
    - [Lorem Picsum](https://picsum.photos) (placeholder images)
    - [Wallhere](https://wallhere.com) (wallpaper / backgrounds)
    - [This Person Does Not Exist](https://thispersondoesnotexist.com) (reload to get a new person)
- Audio
    - [Audio Micro](https://www.audiomicro.com/free-sound-effects)
- Video
    - [Videvo](https://www.videvo.net)
- Image Compression
    - [TinyPNG](https://tinypng.com) (for images <5MB)
    - [CompressPNG](https://compresspng.com) (for images >5MB)

A few examples have been provided below to give you some ideas on how to do your own Media credits.

⚠️ --- END ---⚠️

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [Boutique Ado](https://codeinstitute.net) | Sample images provided from the walkthrough projects |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Pexels](https://images.pexels.com/photos/416160/pexels-photo-416160.jpeg) | Hero image |
| [Wallhere](https://c.wallhere.com/images/9c/c8/da4b4009f070c8e1dfee43d25f99-2318808.jpg!d) | Background wallpaper |
| [Pixabay](https://cdn.pixabay.com/photo/2017/09/04/16/58/passport-2714675_1280.jpg) | Background wallpaper |
| [DALL-E 3](https://openai.com/index/dall-e-3) | AI generated artwork |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [CompressPNG](https://compresspng.com) | Compressing images > 5MB |
| [CloudConvert](https://cloudconvert.com/webp-converter) | Converting images to `.webp` |

### Acknowledgements

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution and acknowledgement to any supports that helped, encouraged, or supported you throughout the development stages of this project. It's always lovely to appreciate those that help us grow and improve our developer skills. A few examples have been provided below to give you some ideas.

⚠️ --- END ---⚠️

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my partner, for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.

