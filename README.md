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

**User Accounts**
| User | Capability | Benefit |
| --- | --- | --- |
| As a user | I can create an account | so that I can purchase items and view/edit my own profile. |
| As a user | I can easily log in and out of my account | so that my details remain private and secure. |
| As a user | I can easily recover my account and change password | so that I can continue to log in and out if I forget my password. |
| As a user | I should receive a confirmation email when my account is created | so that I know it was created successfully. |
| As a user | I can view a user profile page | so that I can see my purchase history and update my details. |

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
| Homepage | Homepage / Account Menu | Homepage / Navigation Expanded | Homepage / Basket Expanded | Products Full Title | Products Floating Title | Product Detail | Basket | Checkout | Checkout Success | Profile | FAQs | Contact Us | Newsletter | Privacy | Staff Dashboard |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![wireframe](documentation/wireframes/mobile/mobile_homepage.png "Homepage") | ![wireframe](documentation/wireframes/mobile/mobile_homepage_account_menu.png "Account Menu") | ![wireframe](documentation/wireframes/mobile/mobile_homepage_navigation_expanded.png "Navigation Menu") | ![wireframe](documentation/wireframes/mobile/mobile_homepage_basket_expanded.png "Basket Preview") | ![wireframe](documentation/wireframes/mobile/mobile_products_full_title.png "Products Full Title") | ![wireframe](documentation/wireframes/mobile/mobile_products_dynamic_title.png "Products Dynamic Title") | ![wireframe](documentation/wireframes/mobile/mobile_product_detail.png "Product Detail") | ![wireframe](documentation/wireframes/mobile/mobile_basket_view.png "Basket") | ![wireframe](documentation/wireframes/mobile/mobile_checkout.png "Checkout") | ![wireframe](documentation/wireframes/mobile/mobile_checkout_success.png "Checkout Success") | ![wireframe](documentation/wireframes/mobile/mobile_profile.png "Profile") | ![wireframe](documentation/wireframes/mobile/mobile_faq.png "FAQs") | ![wireframe](documentation/wireframes/mobile/mobile_contact_us.png "Contact Us") | ![wireframe](documentation/wireframes/mobile/mobile_newsletter.png "Newsletter") | ![wireframe](documentation/wireframes/mobile/mobile_privacy.png "Privacy") | ![wireframe](documentation/wireframes/mobile/mobile_shop_management.png "Staff Dashboard") |

### Tablet Wireframes
| Homepage | Homepage / Account Menu | Homepage / Navigation Expanded | Homepage / Basket Expanded | Products Full Title | Products Floating Title | Product Detail | Basket | Checkout | Checkout Success | Profile | FAQs | Contact Us | Newsletter | Privacy | Staff Dashboard |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![wireframe](documentation/wireframes/tablet/tablet_homepage.png "Homepage") | ![wireframe](documentation/wireframes/tablet/tablet_homepage_account_menu.png "Account Menu") | ![wireframe](documentation/wireframes/tablet/tablet_homepage_navigation_expanded.png "Navigation Menu") | ![wireframe](documentation/wireframes/tablet/tablet_homepage_basket_expanded.png "Basket Preview") | ![wireframe](documentation/wireframes/tablet/tablet_products_full_title.png "Products Full Title") | ![wireframe](documentation/wireframes/tablet/tablet_products_dynamic_title.png "Products Dynamic Title") | ![wireframe](documentation/wireframes/tablet/tablet_product_detail.png "Product Detail") | ![wireframe](documentation/wireframes/tablet/tablet_basket_view.png "Basket") | ![wireframe](documentation/wireframes/tablet/tablet_checkout.png "Checkout") | ![wireframe](documentation/wireframes/tablet/tablet_checkout_success.png "Checkout Success") | ![wireframe](documentation/wireframes/tablet/tablet_profile.png "Profile") | ![wireframe](documentation/wireframes/tablet/tablet_faq.png "FAQs") | ![wireframe](documentation/wireframes/tablet/tablet_contact_us.png "Contact Us") | ![wireframe](documentation/wireframes/tablet/tablet_newsletter.png "Newsletter") | ![wireframe](documentation/wireframes/tablet/tablet_privacy.png "Privacy") | ![wireframe](documentation/wireframes/tablet/tablet_shop_management.png "Staff Dashboard") |

### Desktop Wireframes
| Homepage | Homepage / Account Menu | Homepage / Navigation Expanded | Homepage / Basket Expanded | Products Full Title | Products Floating Title | Product Detail | Basket | Checkout | Checkout Success | Profile | FAQs | Contact Us | Newsletter | Privacy | Staff Dashboard |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![wireframe](documentation/wireframes/desktop/desktop_homepage.png "Homepage") | ![wireframe](documentation/wireframes/desktop/desktop_homepage_account_menu.png "Account Menu") | ![wireframe](documentation/wireframes/desktop/desktop_homepage_navigation_expanded.png "Navigation Menu") | ![wireframe](documentation/wireframes/desktop/desktop_homepage_basket_expanded.png "Basket Preview") | ![wireframe](documentation/wireframes/desktop/desktop_products_full_title.png "Products Full Title") | ![wireframe](documentation/wireframes/desktop/desktop_products_dynamic_title.png "Products Dynamic Title") | ![wireframe](documentation/wireframes/desktop/desktop_product_detail.png "Product Detail") | ![wireframe](documentation/wireframes/desktop/desktop_basket_view.png "Basket") | ![wireframe](documentation/wireframes/desktop/desktop_checkout.png "Checkout") | ![wireframe](documentation/wireframes/desktop/desktop_checkout_success.png "Checkout Success") | ![wireframe](documentation/wireframes/desktop/desktop_profile.png "Profile") | ![wireframe](documentation/wireframes/desktop/desktop_faq.png "FAQs") | ![wireframe](documentation/wireframes/desktop/desktop_contact_us.png "Contact Us") | ![wireframe](documentation/wireframes/desktop/desktop_newsletter.png "Newsletter") | ![wireframe](documentation/wireframes/desktop/desktop_privacy.png "Privacy") | ![wireframe](documentation/wireframes/desktop/desktop_shop_management.png "Staff Dashboard") |

## Features

⚠️ INSTRUCTIONS ⚠️

In this section, you should go over the different parts of your project, and describe each feature. You should explain what value each of the features provides for the user, focusing on your target audience, what they want to achieve, and how your project can help them achieve these things.

**IMPORTANT**: Remember to always include a screenshot of each individual feature!

⚠️ --- END --- ⚠️

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Product List | Users can browse all available products with sorting, filtering by categories, and search functionality. | ![screenshot](documentation/features/product-list.png) |
| Product Details | Displays detailed information about a selected product, including its name, description, price, an image, and available sizes. | ![screenshot](documentation/features/product-details.png) |
| Add to Bag | Users can add items to their shopping bag, with support for selecting different sizes if applicable. | ![screenshot](documentation/features/add-to-bag.png) |
| View Bag | Users can view the contents of their shopping bag, adjust quantities, or remove items. | ![screenshot](documentation/features/view-bag.png) |
| Checkout | Users can proceed to checkout, where they provide their delivery details and payment information using Stripe integration. | ![screenshot](documentation/features/checkout.png) |
| Order Confirmation | Users receive an on-screen and email confirmation with details of their purchase. | ![screenshot](documentation/features/order-confirmation.png) |
| Profile Management | Users can manage their profile information, including their default delivery address and order history. | ![screenshot](documentation/features/profile-management.png) |
| Order History | Users can view their past orders and access details of each order, including products purchased and the delivery status. | ![screenshot](documentation/features/order-history.png) |
| Product Management | Superusers can add, edit, and delete products from the site via a CRUD interface. | ![screenshot](documentation/features/product-management.png) |
| Newsletter | Users can register their email address to receive newsletters from the site. Currently, this only stores the email in the database. | ![screenshot](documentation/features/newsletter.png) |
| Contact | Users can submit a message via the contact form, which stores their name, email, and message in the database. | ![screenshot](documentation/features/contact.png) |
| FAQs | Admins can manage frequently asked questions, which are displayed on the site for users. | ![screenshot](documentation/features/faqs.png) |
| User Feedback | Clear and concise Django messages are used to provide feedback to users when interacting with various features (e.g., adding products to the bag, checking out, etc.). | ![screenshot](documentation/features/user-feedback.png) |
| Heroku Deployment | The site is deployed to Heroku, making it accessible online for users. | ![screenshot](documentation/features/heroku.png) |
| SEO | SEO optimization with a sitemap.xml, robots.txt, and appropriate meta tags to improve search engine visibility. | ![screenshot](documentation/features/seo.png) |
| Marketing | Social media presence is available in the footer using external links, as well as a Facebook Marketplace wireframe in the README for future integrations. | ![screenshot](documentation/features/marketing.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |

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

