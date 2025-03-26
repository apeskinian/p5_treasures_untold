# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

#### Page Templates

> [!NOTE]  
> The main template and also other partial html files listed below were tested as part of the main site files as they include them.
> - base.html
> - toast_error.html
> - toast_info.html
> - toast_rewards.html
> - toast_success.html
> - toast_warning.html
> - info_section.html
> - login_options.html
> - mobile_navbar.html
> - standard_navbar.html
> - sort_and_filter.html

| Directory | Template | Specific Includes File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- | --- |
| templates/account | [login.html](templates/account/login.html) | n/a | [W3 Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapeskinian-treasures-untold-568a3e176ede.herokuapp.com%2Faccounts%2Flogin%2F) | ![HTML Validation](documentation/testing/validation/html/valid_login.png "Valid Login") | No errors or warnings found. |
| templates/account | [logout.html](templates/account/logout.html) | n/a | n/a | ![HTML Validation](documentation/testing/validation/html/valid_logout.png "Valid Logout") | No errors or warnings found. |
| templates/account | [signup.html](templates/account/signup.html) | n/a | [W3 Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapeskinian-treasures-untold-568a3e176ede.herokuapp.com%2Faccounts%2Fsignup%2F) | ![HTML Validation](documentation/testing/validation/html/valid_signup.png "Valid Signup") | No errors or warnings found. |
| templates | [404.html](templates/404.html) | n/a | n/a | ![Html validation](documentation/testing/validation/html/valid_404.png "Valid 404") | No errors or warnings found. |
| templates | [500.html](templates/500.html) | n/a | n/a | ![Html validation](documentation/testing/validation/html/valid_500.png "Valid 500") | No errors or warnings found. |
| home/templates/home | [index.html](home/templates/home/index.html) | n/a | [W3 Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapeskinian-treasures-untold-568a3e176ede.herokuapp.com%2F) | ![HTML Validation](documentation/testing/validation/html/valid_index.png "Valid Index") | No errors or warnings found. |
| products/templates/products | [products.html](products/templates/products/products.html) | n/a | [W3 Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapeskinian-treasures-untold-568a3e176ede.herokuapp.com%2Fproducts%2F) | ![HTML Validation](documentation/testing/validation/html/valid_products.png "Valid Products") | No errors or warnings found. |
| products/templates/products | [product_detail.html](products/templates/products/product_detail.html) | n/a | [W3 Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapeskinian-treasures-untold-568a3e176ede.herokuapp.com%2Fproducts%2F26%2F) | ![HTML Validation](documentation/testing/validation/html/valid_product_detail.png "Valid Product Detail") | No errors or warnings found. Link goes to specific product but same template used for all products. |
| support/templates/support | [support.html](support/templates/support/support.html) | [faqs.html](support/templates/support/includes/faqs.html) | [W3 Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapeskinian-treasures-untold-568a3e176ede.herokuapp.com%2Fsupport%2Ffaq%2F) | ![HTML Validation](documentation/testing/validation/html/valid_faq.png "Valid FAQs") | No errors or warnings found. |
| support/templates/support | [support.html](support/templates/support/support.html) | [contact.html](support/templates/support/includes/contact.html) | [W3 Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapeskinian-treasures-untold-568a3e176ede.herokuapp.com%2Fsupport%2Fcontact%2F) | ![HTML Validation](documentation/testing/validation/html/valid_contact.png "Valid Contact") | No errors or warnings found. |
| support/templates/support | [support.html](support/templates/support/support.html) | [thankyou.html](support/templates/support/includes/thankyou.html) | n/a | ![HTML Validation](documentation/testing/validation/html/valid_thankyou.png "Valid Thankyou") | No errors or warnings found. |
| support/templates/support | [support.html](support/templates/support/support.html) | [newsletter.html](support/templates/support/includes/newsletter.html) | [W3 Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapeskinian-treasures-untold-568a3e176ede.herokuapp.com%2Fsupport%2Fnewsletter%2F) | ![HTML Validation](documentation/testing/validation/html/valid_newsletter.png "Valid newsletter") | No errors or warnings found. |
| support/templates/support | [support.html](support/templates/support/support.html) | [newsletter_success.html](support/templates/support/includes/newsletter_success.html) | n/a | ![HTML Validation](documentation/testing/validation/html/valid_newsletter_success.png "Valid Newsletter Success") | No errors or warnings found. |
| support/templates/support | [support.html](support/templates/support/support.html) | [returns_policy.html](support/templates/support/includes/returns_policy.html) | [W3 Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapeskinian-treasures-untold-568a3e176ede.herokuapp.com%2Fsupport%2Freturns%2F) | ![HTML Validation](documentation/testing/validation/html/valid_returns.png "Valid Returns") | No errors or warnings found. |
| support/templates/support | [support.html](support/templates/support/support.html) | [privacy_policy.html](support/templates/support/includes/privacy_policy.html) | [W3 Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapeskinian-treasures-untold-568a3e176ede.herokuapp.com%2Fsupport%2Fprivacy%2F) | ![HTML Validation](documentation/testing/validation/html/valid_privacy.png "Valid Privacy") | No errors or warnings found. |
| support/templates/support | [support.html](support/templates/support/support.html) | [terms.html](support/templates/support/includes/terms.html) | [W3 Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapeskinian-treasures-untold-568a3e176ede.herokuapp.com%2Fsupport%2Fterms%2F) | ![HTML Validation](documentation/testing/validation/html/valid_terms.png "Valid Terms") | No errors or warnings found. |
| staff/templates/staff | [dashboard.html](staff/templates/staff/dashboard.html) | [product_admin.html](staff/templates/staff/includes/product_admin.html) | n/a | ![HTML Validation](documentation/testing/validation/html/valid_products_admin.png "Valid Dashboard Products") | No errors or warnings found. |
| staff/templates/staff | [dashboard.html](staff/templates/staff/dashboard.html) | [faq_admin.html](staff/templates/staff/includes/faq_admin.html) | n/a | ![HTML Validation](documentation/testing/validation/html/valid_faq_admin.png "Valid Dashboard FAQs") | No errors or warnings found. |
| staff/templates/staff | [dashboard.html](staff/templates/staff/dashboard.html) | [messages_admin.html](staff/templates/staff/includes/messages_admin.html) | n/a | ![HTML Validation](documentation/testing/validation/html/valid_message_admin.png "Valid Dashboard Messages") | No errors or warnings found. |
| staff/templates/staff | [dashboard.html](staff/templates/staff/dashboard.html) | [newsletter_admin.html](staff/templates/staff/includes/newsletter_admin.html) | n/a | ![HTML Validation](documentation/testing/validation/html/valid_newsletter_admin.png "Valid Dashboard Newsletter") | No errors or warnings found. |
| profiles/templates/profiles | [profile.html](profiles/templates/profiles/profile.html) | n/a | n/a | ![HTML Validation](documentation/testing/validation/html/valid_profile.png "Valid Profile") | No errors or warnings found. |
| basket/templates/basket | [basket.html](basket/templates/basket/basket.html) | n/a | n/a | ![HTML Validation](documentation/testing/validation/html/valid_basket.png "Valid Basket") | No errors or warnings found. |
| checkout/templates/checkout | [checkout.html](checkout/templates/checkout/checkout.html) | n/a | n/a | ![HTML Validation](documentation/testing/validation/html/valid_checkout.png "Valid Checkout") |  No errors or warnings found. |
| checkout/templates/checkout | [checkout_success.html](checkout/templates/checkout/checkout_success.html) | n/a | n/a | ![HTML Validation](documentation/testing/validation/html/valid_checkout_success.png "Valid Checkout Success") | No errors or warnings found. |

#### Email Body Templates

HTML was checked by viewing the original message in the email client and then copying the raw html into the W3 validator.

| Directory | Template | Screenshot | Notes |
| --- | --- | --- | --- |
| support/templates/support_emails | [contact_acknowledgment_body.html](support/templates/support/support_emails/contact_acknowledgment_body.html) | ![HTML Validation](documentation/testing/validation/html/valid_contact_message_acknowledgement.png "Valid contact message acknowledgement") | No errors or warnings found. |
| support/templates/support_emails | [subscription_confirmation_body.html](support/templates/support/support_emails/subscription_confirmation_body.html) | ![HTML Validation](documentation/testing/validation/html/valid_subscription_confirmation.png "Valid subscription confirmation") | No errors or warnings found. |
| staff/templates/staff_emails | [contact_reply_body.html](staff/templates/staff/staff_emails/contact_reply_body.html) | ![HTML Validation](documentation/testing/validation/html/valid_message_reply.png "Valid contact message reply") | No errors or warnings found. |
| staff/templates/staff_emails | [newsletter_body.html](staff/templates/staff/staff_emails/newsletter_body.html) | ![HTML Validation](documentation/testing/validation/html/valid_subscription_email.png "Valid subscription email") | No errors or warnings found. |
| staff/checkout/confirmation_emails | [confirmation_email_body.html](checkout/templates/checkout/confirmation_emails/confirmation_email_body.html) | ![HTML Validation](documentation/testing/validation/html/valid_order_confirmation_email.png "Valid order confirmation email") | No errors or warnings found. |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static/css | [base_style.css](static/css/base_style.css) | [CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fapeskinian-treasures-untold-568a3e176ede.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![CSS Validation](documentation/testing/validation/css/valid_base_style.png "Valid base_style.cc") | No errors. Warnings for CSS variables and Bootstrap |
| static/css | [custom_colours.css](static/css/custom_colours.css) | n/a | ![CSS Validaton](documentation/testing/validation/css/valid_custom_colours.png "Valid custom_colours.css") | No errors. Warnings for CSS variables. |
| basket/static/basket/css | [basket_style.css](basket/static/basket/css/basket_style.css) | n/a | ![CSS Validation](documentation/testing/validation/css/valid_basket_style.png "Valid basket_style.css") | No errors. Warnings for CSS variables. |
| checkout/static/checkout/css | [checkout_style.css](checkout/static/checkout/css/checkout_style.css) | n/a | ![CSS Validation](documentation/testing/validation/css/valid_checkout_style.png "Valid checkout_style.css") | No errors or warnings found. |
| home/static/home/css | [home_style.css](home/static/home/css/home_style.css) | n/a | ![CSS Validation](documentation/testing/validation/css/valid_home_style.png "Valid home_style.css") | No errors. Warnings for imported style sheets and CSS variables. |
| home/static/home/css | [marquee_style.css](home/static/home/css/marquee_style.css) | n/a | ![CSS Validation](documentation/testing/validation/css/valid_marquee_style.png "Valid marquee_style.css") | No errors. Warning for CSS variable. |
| home/static/home/css | [slideshow_style.css](home/static/home/css/slideshow_style.css) | n/a | ![CSS Validation](documentation/testing/validation/css/valid_slideshow_style.png "Valid slideshow_style.css") | No errors or warnings found. |
| products/static/products/css | [products_style.css](products/static/products/css/products_style.css) | n/a | ![CSS Validation](documentation/testing/validation/css/valid_products_style.png "Valid product_style.css") | No errors. Warnings for CSS variables. |
| profiles/static/profiles/css | [profiles_style.css](profiles/static/profiles/css/profiles_style.css) | n/a | ![CSS Validation](documentation/testing/validation/css/valid_profiles_style.png "Valid profiles_style.css") | No errors. Warnings for CSS variables. |
| staff/static/staff/css | [staff_style.css](staff/static/staff/css/staff_style.css) | n/a | ![CSS Validation](documentation/testing/validation/css/valid_staff_style.png "Valid staff_style.css") | No errors. Warnings for CSS variables. |
| support/static/support/css | [support_style.css](support/static/support/css/support_style.css) | n/a | ![CSS Validation](documentation/testing/validation/css/valid_support_style.png "Valid support_style.css") | No errors. Warnings for CSS variables. |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static/script | [base_script.js](static/script/base_script.js) | ![JSHint Validation](documentation/testing/validation/script/valid_base_script.png "Valid base_script.js") | No errors, 'bootstrap' shown as undefined variable. |
| static/script | [product_limits.js](static/script/product_limits.js) | ![JSHint Validation](documentation/testing/validation/script/valid_product_limits.png "Valid product_limits.js") | No errors or warnings found. |
| basket/static/basket/script | [basket_script.js](basket/static/basket/script/basket_script.js) | ![JSHint Validation](documentation/testing/validation/script/valid_basket_script.png "Valid basket_script.js") | No errors or warnings found. |
| checkout/static/checkout/script | [stripe_elements.js](checkout/static/checkout/script/stripe_elements.js) | ![JSHint Validation](documentation/testing/validation/script/valid_stripe_elements.png "Valid stripe_elements.js") | No errors, 'stripe' shown as undefined variable. |
| home/static/home/script | [slideshow_script.js](home/static/home/script/slideshow_script.js) | ![JSHint Validation](documentation/testing/validation/script/valid_slideshow_script.png "Valid slideshow_script.js") | No errors or warnings found. |
| products/static/products/script | [countdown_timer.js](products/static/products/script/countdown_timer.js) | ![JSHint Validation](documentation/testing/validation/script/valid_countdown_timer.png "Valid countdown_timer.js") | No errors or warnings found. |
| products/static/products/script | [products_script.js](products/static/products/script/products_script.js) | ![JSHint Validation](documentation/testing/validation/script/valid_products_script.png "Valid products_script.js") | No errors or warnings found. |
| profiles/static/profiles/script | [profiles_script.js](profiles/static/profiles/script/profiles_script.js) | ![JSHint Validation](documentation/testing/validation/script/valid_profiles_script.png "Valid profiles_script.js") | No errors, 'bootstrap' shown as undefined variable. |
| staff/static/staff/script | [staff_script.js](staff/static/staff/script/staff_script.js) | ![JSHint Validation](documentation/testing/validation/script/valid_staff_script.png "Valid staff_script.js") | No errors, 'bootstrap' shown as undefined variable. |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

#### Project Level Files
| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| treasures_untold | [settings.py](treasures_untold/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/treasures_untold/settings.py) | ![Python Validation](documentation/testing/validation/python/project_level/valid_settings.png "Valid settings.py") | All clear, no errors found. |
| treasures_untold | [urls.py](treasures_untold/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/treasures_untold/urls.py) | ![Python Validation](documentation/testing/validation/python/project_level/valid_urls.png "Valid urls.py") | All clear, no errors found. |
|  | [manage.py](/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/manage.py) | ![Python Validation](documentation/testing/validation/python/project_level/valid_manage.png "Valid manage.py") | All clear, no errors found. |

#### Basket App Files
| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| basket | [admin.py](basket/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/basket/admin.py) | ![Python Validation](documentation/testing/validation/python/basket_app/valid_basket_admin.png "Valid admin.py") | All clear, no errors found. |
| basket | [apps.py](basket/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/basket/apps.py) | ![Python Validation](documentation/testing/validation/python/basket_app/valid_basket_apps.png "Valid apps.py") | All clear, no errors found. |
| basket/templatetags | [basket_tools.py](basket/templatetags/basket_tools.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/basket/templatetags/basket_tools.py) | ![Python Validation](documentation/testing/validation/python/basket_app/valid_basket_basket_tools.png "Valid basket_tools.py") | All clear, no errors found. |
| basket | [contexts.py](basket/contexts.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/basket/contexts.py) | ![Python Validation](documentation/testing/validation/python/basket_app/valid_basket_contexts.png "Valid contexts.py") | All clear, no errors found. |
| basket/management | [clear_abandoned_sessions.py](basket/management/commands/clear_abandoned_sessions.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/basket/management/commands/clear_abandoned_sessions.py) | ![Python Validation](documentation/testing/validation/python/basket_app/valid_basket_clear_abandoned_sessions.png "Valid clear_abandoned_sessions.py") | All clear, no errors found. |
| basket | [middleware.py](basket/middleware.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/basket/middleware.py) | ![Python Validation](documentation/testing/validation/python/basket_app/valid_basket_middleware.png "Valid middleware.py") | All clear, no errors found. |
| basket | [models.py](basket/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/basket/models.py) | ![Python Validation](documentation/testing/validation/python/basket_app/valid_basket_models.png "Valid models.py") | All clear, no errors found. |
| basket | [urls.py](basket/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/basket/urls.py) | ![Python Validation](documentation/testing/validation/python/basket_app/valid_basket_urls.png "Valid urls.py") | All clear, no errors found. |
| basket | [views.py](basket/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/basket/views.py) | ![Python Validation](documentation/testing/validation/python/basket_app/valid_basket_views.png "Valid views.py") | All clear, no errors found. |
| basket/tests | [test_admin.py](basket/tests/test_admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/basket/tests/test_admin.py) | ![Python Validation](documentation/testing/validation/python/basket_app/valid_basket_test_admin.png "Valid test_admin.py") | All clear, no errors found. |

#### Checkout App Files
| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout | [admin.py](checkout/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/checkout/admin.py) | ![Python Validation](documentation/testing/validation/python/checkout_app/valid_checkout_admin.png "Valid admin.py") | All clear, no errors found. |
| checkout | [apps.py](checkout/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/checkout/apps.py) | ![Python Validation](documentation/testing/validation/python/checkout_app/valid_checkout_apps.png "Valid apps.py") | All clear, no errors found. |
| checkout/templatetags | [checkout_tools.py](checkout/templatetags/checkout_tools.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/checkout/templatetags/checkout_tools.py) | ![Python Validation](documentation/testing/validation/python/checkout_app/valid_checkout_checkout_tools.png "Valid checkout_tools.py") | All clear, no errors found. |
| checkout | [forms.py](checkout/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/checkout/forms.py) | ![Python Validation](documentation/testing/validation/python/checkout_app/valid_checkout_forms.png "Valid forms.py") | All clear, no errors found. |
| checkout | [models.py](checkout/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/checkout/models.py) | ![Python Validation](documentation/testing/validation/python/checkout_app/valid_checkout_models.png "Valid models.py") | All clear, no errors found. |
| checkout | [signals.py](checkout/signals.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/checkout/signals.py) | ![Python Validation](documentation/testing/validation/python/checkout_app/valid_checkout_signals.png "Valid signals.py") | All clear, no errors found. |
| checkout | [urls.py](checkout/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/checkout/urls.py) | ![Python Validation](documentation/testing/validation/python/checkout_app/valid_checkout_urls.png "Valid urls.py") | All clear, no errors found. |
| checkout | [views.py](checkout/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/checkout/views.py) | ![Python Validation](documentation/testing/validation/python/checkout_app/valid_checkout_views.png "Valid views.py") | All clear, no errors found. |
| checkout | [webhook_handler.py](checkout/webhook_handler.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/checkout/webhook_handler.py) | ![Python Validation](documentation/testing/validation/python/checkout_app/valid_checkout_webhook_handler.png "Valid webhook_handler.py") | All clear, no errors found. |
| checkout | [webhooks.py](checkout/webhooks.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/checkout/webhooks.py) | ![Python Validation](documentation/testing/validation/python/checkout_app/valid_checkout_webhooks.png "Valid webhooks.py") | All clear, no errors found. |

#### Home App Files
| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| home | [admin.py](home/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/home/admin.py) | ![Python Validation](documentation/testing/validation/python/home_app/valid_home_admin.png "Valid admin.py") | All clear, no errors found. |
| home | [apps.py](home/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/home/apps.py) | ![Python Validation](documentation/testing/validation/python/home_app/valid_home_apps.png "Valid apps.py") | All clear, no errors found. |
| home | [models.py](home/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/home/models.py) | ![Python Validation](documentation/testing/validation/python/home_app/valid_home_models.png "Valid models.py") | All clear, no errors found. |
| home | [urls.py](home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/home/urls.py) | ![Python Validation](documentation/testing/validation/python/home_app/valid_home_urls.png "Valid urls.py") | All clear, no errors found. |
| home | [views.py](home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/home/views.py) | ![Python Validation](documentation/testing/validation/python/home_app/valid_home_views.png "Valid views.py") | All clear, no errors found. |

#### Products App Files
| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| products | [admin.py](products/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/products/admin.py) | ![Python Validation](documentation/testing/validation/python/products_app/valid_products_admin.png "Valid admin.py") | All clear, no errors found. |
| products | [apps.py](products/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/products/apps.py) | ![Python Validation](documentation/testing/validation/python/products_app/valid_products_apps.png "Valid apps.py") | All clear, no errors found. |
| products | [contexts.py](products/contexts.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/products/contexts.py) | ![Python Validation](documentation/testing/validation/python/products_app/valid_products_contexts.png "Valid contexts.py") | All clear, no errors found. |
| products | [forms.py](products/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/products/forms.py) | ![Python Validation](documentation/testing/validation/python/products_app/valid_products_forms.png "Valid forms.py") | All clear, no errors found. |
| products | [models.py](products/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/products/models.py) | ![Python Validation](documentation/testing/validation/python/products_app/valid_products_models.png "Valid models.py") | All clear, no errors found. |
| products/templatetags | [product_tags.py](products/templatetags/product_tags.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/products/templatetags/product_tags.py) | ![Python Validation](documentation/testing/validation/python/products_app/valid_products_product_tags.png "Valid product_tags.py") | All clear, no errors found. |
| products | [signals.py](products/signals.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/products/signals.py) | ![Python Validation](documentation/testing/validation/python/products_app/valid_products_signals.png "Valid signals.py") | All clear, no errors found. |
| products | [urls.py](products/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/products/urls.py) | ![Python Validation](documentation/testing/validation/python/products_app/valid_products_urls.png "Valid urls.py") | All clear, no errors found. |
| products | [views.py](products/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/products/views.py) | ![Python Validation](documentation/testing/validation/python/products_app/valid_products_views.png "Valid views.py") | All clear, no errors found. |
| products | [widgets.py](products/widgets.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/products/widgets.py) | ![Python Validation](documentation/testing/validation/python/products_app/valid_products_widgets.png "Valid widgets.py") | All clear, no errors found. |

#### Profiles App Files
| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| profiles | [admin.py](profiles/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/profiles/admin.py) | ![Python Validation](documentation/testing/validation/python/profiles_app/valid_profiles_admin.png "Valid admin.py") | All clear, no errors found. |
| profiles | [apps.py](profiles/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/profiles/apps.py) | ![Python Validation](documentation/testing/validation/python/profiles_app/valid_profiles_apps.png "Valid apps.py") | All clear, no errors found. |
| profiles | [forms.py](profiles/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/profiles/forms.py) | ![Python Validation](documentation/testing/validation/python/profiles_app/valid_profiles_forms.png "Valid forms.py") | All clear, no errors found. |
| profiles | [models.py](profiles/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/profiles/models.py) | ![Python Validation](documentation/testing/validation/python/profiles_app/valid_profiles_models.png "Valid models.py") | All clear, no errors found. |
| profiles | [urls.py](profiles/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/profiles/urls.py) | ![Python Validation](documentation/testing/validation/python/profiles_app/valid_profiles_urls.png "Valid urls.py") | All clear, no errors found. |
| profiles | [views.py](profiles/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/profiles/views.py) | ![Python Validation](documentation/testing/validation/python/profiles_app/valid_profiles_views.png "Valid views.py") | All clear, no errors found. |

#### Staff App Files
| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| staff | [admin.py](staff/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/staff/admin.py) | ![Python Validation](documentation/testing/validation/python/staff_app/valid_staff_admin.png "Valid admin.py") | All clear, no errors found. |
| staff | [apps.py](staff/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/staff/apps.py) | ![Python Validation](documentation/testing/validation/python/staff_app/valid_staff_apps.png "Valid apps.py") | All clear, no errors found. |
| staff | [models.py](staff/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/staff/models.py) | ![Python Validation](documentation/testing/validation/python/staff_app/valid_staff_models.png "Valid models.py") | All clear, no errors found. |
| staff | [urls.py](staff/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/staff/urls.py) | ![Python Validation](documentation/testing/validation/python/staff_app/valid_staff_urls.png "Valid urls.py") | All clear, no errors found. |
| staff | [views.py](staff/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/staff/views.py) | ![Python Validation](documentation/testing/validation/python/staff_app/valid_staff_views.png "Valid views.py") | All clear, no errors found. |

#### Support App Files
| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| support | [admin.py](support/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/support/admin.py) | ![Python Validation](documentation/testing/validation/python/support_app/valid_support_admin.png "Valid admin.py") | All clear, no errors found. |
| support | [apps.py](support/apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/support/apps.py) | ![Python Validation](documentation/testing/validation/python/support_app/valid_support_apps.png "Valid apps.py") | All clear, no errors found. |
| support | [contexts.py](support/contexts.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/support/contexts.py) | ![Python Validation](documentation/testing/validation/python/support_app/valid_support_contexts.png "Valid contexts.py") | All clear, no errors found. |
| support | [forms.py](support/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/support/forms.py) | ![Python Validation](documentation/testing/validation/python/support_app/valid_support_forms.png "Valid forms.py") | All clear, no errors found. |
| support | [models.py](support/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/support/models.py) | ![Python Validation](documentation/testing/validation/python/support_app/valid_support_models.png "Valid models.py") | All clear, no errors found. |
| support | [urls.py](support/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/support/urls.py) | ![Python Validation](documentation/testing/validation/python/support_app/valid_support_urls.png "Valid urls.py") | All clear, no errors found. |
| support | [views.py](support/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p5_treasures_untold/main/support/views.py) | ![Python Validation](documentation/testing/validation/python/support_app/valid_support_views.png "Valid views.py") | All clear, no errors found. |


## Responsiveness

I've tested my deployed project to check for responsiveness issues.

### Account and Error Pages
| Device | Login | Logout | Signup | 404 | 500 | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Mobile (devtools) | ![Login Page](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_login.png "login page") | ![Logout Page](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_logout.png "logout page") | ![Signup](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_signup.png "signup page") | ![404 Page](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_404.png "404 page") | ![500 Page](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_500.png "500 page") | Works as expected. |
| Tablet (devtools) | ![Login Page](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_login.png "login page") | ![Logout Page](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_logout.png "logout page") | ![Signup](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_signup.png "signup page") | ![404 Page](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_404.png "404 page") | ![500 Page](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_500.png "500 page") | Works as expected. |
| Desktop (devtools) | ![Login Page](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_login.png "login page") | ![Logout Page](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_logout.png "logout page") | ![Signup](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_signup.png "signup page") | ![404 Page](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_404.png "404 page") | ![500 Page](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_500.png "500 page") | Works as expected. |
| 2K Screen (devtools) | ![Login Page](documentation/testing/responsiveness/devtools_2K/devtools_2K_login.png "login page") | ![Logout Page](documentation/testing/responsiveness/devtools_2K/devtools_2K_logout.png "logout page") | ![Signup](documentation/testing/responsiveness/devtools_2K/devtools_2K_signup.png "signup page") | ![404 Page](documentation/testing/responsiveness/devtools_2K/devtools_2K_404.png "404 page") | ![500 Page](documentation/testing/responsiveness/devtools_2K/devtools_2K_500.png "500 page") | Works as expected. |
| iPhone 16 Pro | ![Login Page](documentation/testing/responsiveness/iphone/iphone_login.PNG "login page") | ![Logout Page](documentation/testing/responsiveness/iphone/iphone_logout.PNG "logout page") | ![Signup](documentation/testing/responsiveness/iphone/iphone_signup.PNG "signup page") | ![404 Page](documentation/testing/responsiveness/iphone/iphone_404.PNG "404 page") | ![500 Page](documentation/testing/responsiveness/iphone/iphone_500.PNG "500 page") | Works as expected. |
| iPad Mini | ![Login Page](documentation/testing/responsiveness/ipad_mini/ipad_mini_login.PNG "login page") | ![Logout Page](documentation/testing/responsiveness/ipad_mini/ipad_mini_logout.PNG "logout page") | ![Signup](documentation/testing/responsiveness/ipad_mini/ipad_mini_signup.PNG "signup page") | ![404 Page](documentation/testing/responsiveness/ipad_mini/ipad_mini_404.PNG "404 page") | ![500 Page](documentation/testing/responsiveness/ipad_mini/ipad_mini_500.PNG "500 page") | Works as expected. |
| Samsung Galaxy Tab 6 Lite | ![Login Page](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_login.jpg "login page") | ![Logout Page](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_logout.jpg "logout page") | ![Signup](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_signup.jpg "signup page") | ![404 Page](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_404.jpg "404 page") | ![500 Page](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_500.jpg "500 page") | Works as expected. |
| MacBook Air M3 | ![Login Page](documentation/testing/responsiveness/macbook/macbook_login.png "login page") | ![Logout Page](documentation/testing/responsiveness/macbook/macbook_logout.png "logout page") | ![Signup](documentation/testing/responsiveness/macbook/macbook_signup.png "signup page") | ![404 Page](documentation/testing/responsiveness/macbook/macbook_404.png "404 page") | ![500 Page](documentation/testing/responsiveness/macbook/macbook_500.png "500 page") | Works as expected. |
| 2K Monitor | ![Login Page](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_login.png "login page") | ![Logout Page](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_logout.png "logout page") | ![Signup](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_signup.png "signup page") | ![404 Page](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_404.png "404 page") | ![500 Page](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_500.png "500 page") | Works as expected. |

### Product Browsing
| Device | Homepage | Products | Product Details | Notes |
| --- | --- | --- | --- | --- |
| Mobile (devtools) | ![Homepage](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_homepage.png "homepage") | ![Products](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_products.png "products page") | ![Product Details](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_product_detail.png "product detail page") | Works as expected. |
| Tablet (devtools) | ![Homepage](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_homepage.png "homepage") | ![Products](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_products.png "products page") | ![Product Details](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_product_detail.png "product detail page") | Works as expected. |
| Desktop (devtools) | ![Homepage](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_homepage.png "homepage") | ![Products](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_products.png "products page") | ![Product Details](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_product_detail.png "product detail page") | Works as expected. |
| 2K Screen (devtools) | ![Homepage](documentation/testing/responsiveness/devtools_2K/devtools_2K_homepage.png "homepage") | ![Products](documentation/testing/responsiveness/devtools_2K/devtools_2K_products.png "products page") | ![Product Details](documentation/testing/responsiveness/devtools_2K/devtools_2K_product_detail.png "product detail page") | Works as expected. |
| iPhone 16 Pro | ![Homepage](documentation/testing/responsiveness/iphone/iphone_homepage.PNG "homepage") | ![Products](documentation/testing/responsiveness/iphone/iphone_products.PNG "products page") | ![Product Details](documentation/testing/responsiveness/iphone/iphone_product_detail.PNG "product detail page") | Works as expected. |
| iPad Mini | ![Homepage](documentation/testing/responsiveness/ipad_mini/ipad_mini_homepage.PNG "homepage") | ![Products](documentation/testing/responsiveness/ipad_mini/ipad_mini_products.PNG "products page") | ![Product Details](documentation/testing/responsiveness/ipad_mini/ipad_mini_product_detail.PNG "product detail page") | Works as expected. |
| Samsung Galaxy Tab 6 Lite | ![Homepage](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_homepage.jpg "homepage") | ![Products](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_products.jpg "products page") | ![Product Details](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_product_detail.jpg "product detail page") | Works as expected. |
| MacBook Air M3 | ![Homepage](documentation/testing/responsiveness/macbook/macbook_homepage.png "homepage") | ![Products](documentation/testing/responsiveness/macbook/macbook_products.png "products page") | ![Product Details](documentation/testing/responsiveness/macbook/macbook_product_detail.png "product detail page") | Works as expected. |
| 2K Monitor | ![Homepage](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_homepage.png "homepage") | ![Products](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_products.png "products page") | ![Product Details](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_product_detail.png "product detail page") | Works as expected. |

### Product Purchasing
| Device | Basket View | Checkout | Checkout Success | Profile | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (devtools) | ![Basket View](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_basket.png "basket page") | ![Checkout](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_checkout.png "checkout page") | ![Checkout Success](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_checkout_success.png "checkout success page") | ![Profile](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_profile.png "profile page") | Works as expected. |
| Tablet (devtools) | ![Basket View](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_basket.png "basket page") | ![Checkout](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_checkout.png "checkout page") | ![Checkout Success](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_checkout_success.png "checkout success page") | ![Profile](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_profile.png "profile page") | Works as expected. |
| Desktop (devtools) | ![Basket View](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_basket.png "basket page") | ![Checkout](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_checkout.png "checkout page") | ![Checkout Success](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_checkout_success.png "checkout success page") | ![Profile](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_profile.png "profile page") | Works as expected. |
| 2K Screen (devtools) | ![Basket View](documentation/testing/responsiveness/devtools_2K/devtools_2K_basket.png "basket page") | ![Checkout](documentation/testing/responsiveness/devtools_2K/devtools_2K_checkout.png "checkout page") | ![Checkout Success](documentation/testing/responsiveness/devtools_2K/devtools_2K_checkout_success.png "checkout success page") | ![Profile](documentation/testing/responsiveness/devtools_2K/devtools_2K_profile.png "profile page") | Works as expected. |
| iPhone 16 Pro | ![Basket View](documentation/testing/responsiveness/iphone/iphone_basket.PNG "basket page") | ![Checkout](documentation/testing/responsiveness/iphone/iphone_checkout.png "checkout page") | ![Checkout Success](documentation/testing/responsiveness/iphone/iphone_checkout_success.png "checkout success page") | ![Profile](documentation/testing/responsiveness/iphone/iphone_profile.png "profile page") | Works as expected. |
| iPad Mini | ![Basket View](documentation/testing/responsiveness/ipad_mini/ipad_mini_basket.PNG "basket page") | ![Checkout](documentation/testing/responsiveness/ipad_mini/ipad_mini_checkout.png "checkout page") | ![Checkout Success](documentation/testing/responsiveness/ipad_mini/ipad_mini_checkout_success.png "checkout success page") | ![Profile](documentation/testing/responsiveness/ipad_mini/ipad_mini_profile.png "profile page") | Works as expected. |
| Samsung Galaxy Tab 6 Lite | ![Basket View](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_basket.jpg "basket page") | ![Checkout](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_checkout.jpg "checkout page") | ![Checkout Success](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_checkout_success.png "checkout success page") | ![Profile](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_profile.png "profile page") | Works as expected. |
| MacBook Air M3 | ![Basket View](documentation/testing/responsiveness/macbook/macbook_basket.png "basket page") | ![Checkout](documentation/testing/responsiveness/macbook/macbook_checkout.png "checkout page") | ![Checkout Success](documentation/testing/responsiveness/macbook/macbook_checkout_success.png "checkout success page") | ![Profile](documentation/testing/responsiveness/macbook/macbook_profile.png "profile page") | Works as expected. |
| 2K Monitor | ![Basket View](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_basket.png "basket page") | ![Checkout](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_checkout.png "checkout page") | ![Checkout Success](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_checkout_success.png "checkout success page") | ![Profile](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_profile.png "profile page") | Works as expected. |

### Support Pages
| Device | FAQ | Contact Us | Contact Message Thank You | Newsletter | Newsletter Success | Returns Policy | Privacy Statement | Terms and Conditions | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (devtools) | ![FAQ](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_faqs.png "faqs page") | ![Contact Us](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_contact_us.png "contact us page") | ![Contact Message Thank You](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_thankyou.png "contact message acknowledgement page") | ![Newsletter](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_newsletter.png "newsletter page") | ![Newsletter Success](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_newsletter_success.png "newsletter confirm page") | ![Returns Policy](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_returns.png "returns policy page") | ![Privacy Statement](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_privacy.png "privacy policy page") | ![Terms and Conditions](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_terms.png "terms and conditions page") | Works as expected. |
| Tablet (devtools) | ![FAQ](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_faqs.png "faqs page") | ![Contact Us](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_contact_us.png "contact us page") | ![Contact Message Thank You](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_thankyou.png "contact message acknowledgement page") | ![Newsletter](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_newsletter.png "newsletter page") | ![Newsletter Success](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_newsletter_success.png "newsletter confirm page") | ![Returns Policy](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_returns.png "returns policy page") | ![Privacy Statement](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_privacy.png "privacy policy page") | ![Terms and Conditions](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_terms.png "terms and conditions page") | Works as expected. |
| Desktop (devtools) | ![FAQ](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_faqs.png "faqs page") | ![Contact Us](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_contact_us.png "contact us page") | ![Contact Message Thank You](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_thankyou.png "contact message acknowledgement page") | ![Newsletter](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_newsletter.png "newsletter page") | ![Newsletter Success](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_newsletter_success.png "newsletter confirm page") | ![Returns Policy](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_returns.png "returns policy page") | ![Privacy Statement](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_privacy.png "privacy policy page") | ![Terms and Conditions](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_terms.png "terms and conditions page") | Works as expected. |
| 2K Screen (devtools) | ![FAQ](documentation/testing/responsiveness/devtools_2K/devtools_2K_faqs.png "faqs page") | ![Contact Us](documentation/testing/responsiveness/devtools_2K/devtools_2K_contact_us.png "contact us page") | ![Contact Message Thank You](documentation/testing/responsiveness/devtools_2K/devtools_2K_thankyou.png "contact message acknowledgement page") | ![Newsletter](documentation/testing/responsiveness/devtools_2K/devtools_2K_newsletter.png "newsletter page") | ![Newsletter Success](documentation/testing/responsiveness/devtools_2K/devtools_2K_newsletter_success.png "newsletter confirm page") | ![Returns Policy](documentation/testing/responsiveness/devtools_2K/devtools_2K_returns.png "returns policy page") | ![Privacy Statement](documentation/testing/responsiveness/devtools_2K/devtools_2K_privacy.png "privacy policy page") | ![Terms and Conditions](documentation/testing/responsiveness/devtools_2K/devtools_2K_terms.png "terms and conditions page") | Works as expected. |
| iPhone 16 Pro | ![FAQ](documentation/testing/responsiveness/iphone/iphone_faqs.PNG "faqs page") | ![Contact Us](documentation/testing/responsiveness/iphone/iphone_contact_us.PNG "contact us page") | ![Contact Message Thank You](documentation/testing/responsiveness/iphone/iphone_thankyou.PNG "contact message acknowledgement page") | ![Newsletter](documentation/testing/responsiveness/iphone/iphone_newsletter.PNG "newsletter page") | ![Newsletter Success](documentation/testing/responsiveness/iphone/iphone_newsletter_success.PNG "newsletter confirm page") | ![Returns Policy](documentation/testing/responsiveness/iphone/iphone_returns.PNG "returns policy page") | ![Privacy Statement](documentation/testing/responsiveness/iphone/iphone_privacy.PNG "privacy policy page") | ![Terms and Conditions](documentation/testing/responsiveness/iphone/iphone_terms.PNG "terms and conditions page") | Works as expected. |
| iPad Mini | ![FAQ](documentation/testing/responsiveness/ipad_mini/ipad_mini_faqs.PNG "faqs page") | ![Contact Us](documentation/testing/responsiveness/ipad_mini/ipad_mini_contact_us.PNG "contact us page") | ![Contact Message Thank You](documentation/testing/responsiveness/ipad_mini/ipad_mini_thankyou.PNG "contact message acknowledgement page") | ![Newsletter](documentation/testing/responsiveness/ipad_mini/ipad_mini_newsletter.PNG "newsletter page") | ![Newsletter Success](documentation/testing/responsiveness/ipad_mini/ipad_mini_newsletter_success.PNG "newsletter confirm page") | ![Returns Policy](documentation/testing/responsiveness/ipad_mini/ipad_mini_returns.PNG "returns policy page") | ![Privacy Statement](documentation/testing/responsiveness/ipad_mini/ipad_mini_privacy.PNG "privacy policy page") | ![Terms and Conditions](documentation/testing/responsiveness/ipad_mini/ipad_mini_terms.PNG "terms and conditions page") | Works as expected. |
| Samsung Galaxy Tab 6 Lite | ![FAQ](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_faqs.jpg "faqs page") | ![Contact Us](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_contact_us.jpg "contact us page") | ![Contact Message Thank You](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_thankyou.png "contact message acknowledgement page") | ![Newsletter](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_newsletter.jpg "newsletter page") | ![Newsletter Success](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_newsletter_success.jpg "newsletter confirm page") | ![Returns Policy](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_returns.jpg "returns policy page") | ![Privacy Statement](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_privacy.jpg "privacy policy page") | ![Terms and Conditions](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_terms.jpg "terms and conditions page") | Works as expected. |
| MacBook Air M3 | ![FAQ](documentation/testing/responsiveness/macbook/macbook_faqs.png "faqs page") | ![Contact Us](documentation/testing/responsiveness/macbook/macbook_contact_us.png "contact us page") | ![Contact Message Thank You](documentation/testing/responsiveness/macbook/macbook_thankyou.png  "contact message acknowledgement page") | ![Newsletter](documentation/testing/responsiveness/macbook/macbook_newsletter.png "newsletter page") | ![Newsletter Success](documentation/testing/responsiveness/macbook/macbook_newsletter_success.png "newsletter confirm page") | ![Returns Policy](documentation/testing/responsiveness/macbook/macbook_returns.png "returns policy page") | ![Privacy Statement](documentation/testing/responsiveness/macbook/macbook_privacy.png "privacy policy page") | ![Terms and Conditions](documentation/testing/responsiveness/macbook/macbook_terms.png "terms and conditions page") | Works as expected. |
| 2K Monitor | ![FAQ](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_faqs.png "faqs page") | ![Contact Us](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_contact_us.png "contact us page") | ![Contact Message Thank You](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_thankyou.png "contact message acknowledgement page") | ![Newsletter](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_newsletter.png "newsletter page") | ![Newsletter Success](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_newsletter_success.png "newsletter confirm page") | ![Returns Policy](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_returns.png "returns policy page") | ![Privacy Statement](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_privacy.png "privacy policy page") | ![Terms and Conditions](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_terms.png "terms and conditions page") | Works as expected. |

### Staff Pages
| Device | Product Admin | FAQ Admin | Message Admin | Newsletter Admin | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (devtools) | ![Product Admin](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_product_admin.png "product admin page") | ![FAQ Admin](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_faq_admin.png "faq admin page") | ![Message Admin](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_message_admin.png "message admin page") | ![Newsletter Admin](documentation/testing/responsiveness/devtools_mobile/devtools_mobile_newsletter_admin.png "newsletter admin page") | Works as expected. |
| Tablet (devtools) | ![Product Admin](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_product_admin.png "product admin page") | ![FAQ Admin](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_faq_admin.png "faq admin page") | ![Message Admin](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_message_admin.png "message admin page") | ![Newsletter Admin](documentation/testing/responsiveness/devtools_tablet/devtools_tablet_newsletter_admin.png "newsletter admin page") | Works as expected. |
| Desktop (devtools) | ![Product Admin](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_product_admin.png "product admin page") | ![FAQ Admin](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_faq_admin.png "faq admin page") | ![Message Admin](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_message_admin.png "message admin page") | ![Newsletter Admin](documentation/testing/responsiveness/devtools_desktop/devtools_desktop_newsletter_admin.png "newsletter admin page") | Works as expected. |
| 2K Screen (devtools) | ![Product Admin](documentation/testing/responsiveness/devtools_2K/devtools_2K_product_admin.png "product admin page") | ![FAQ Admin](documentation/testing/responsiveness/devtools_2K/devtools_2K_faq_admin.png "faq admin page") | ![Message Admin](documentation/testing/responsiveness/devtools_2K/devtools_2K_message_admin.png "message admin page") | ![Newsletter Admin](documentation/testing/responsiveness/devtools_2K/devtools_2K_newsletter_admin.png "newsletter admin page") | Works as expected. |
| iPhone 16 Pro | ![Product Admin](documentation/testing/responsiveness/iphone/iphone_product_admin.PNG "product admin page") | ![FAQ Admin](documentation/testing/responsiveness/iphone/iphone_faq_admin.PNG "faq admin page") | ![Message Admin](documentation/testing/responsiveness/iphone/iphone_message_admin.PNG "message admin page") | ![Newsletter Admin](documentation/testing/responsiveness/iphone/iphone_newsletter_admin.PNG "newsletter admin page") | Works as expected. |
| iPad Mini | ![Product Admin](documentation/testing/responsiveness/ipad_mini/ipad_mini_product_admin.PNG "product admin page") | ![FAQ Admin](documentation/testing/responsiveness/ipad_mini/ipad_mini_faq_admin.PNG "faq admin page") | ![Message Admin](documentation/testing/responsiveness/ipad_mini/ipad_mini_message_admin.png "message admin page") | ![Newsletter Admin](documentation/testing/responsiveness/ipad_mini/ipad_mini_newsletter_admin.PNG "newsletter admin page") | Works as expected. |
| Samsung Galaxy Tab 6 Lite | ![Product Admin](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_product_admin.jpg "product admin page") | ![FAQ Admin](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_faq_admin.jpg "faq admin page") | ![Message Admin](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_message_admin.jpg "message admin page") | ![Newsletter Admin](documentation/testing/responsiveness/galaxy_tab/galaxy_tab_newsletter_admin.jpg "newsletter admin page") | Works as expected. |
| MacBook Air M3 | ![Product Admin](documentation/testing/responsiveness/macbook/macbook_product_admin.png "product admin page") | ![FAQ Admin](documentation/testing/responsiveness/macbook/macbook_faq_admin.png "faq admin page") | ![Message Admin](documentation/testing/responsiveness/macbook/macbook_message_admin.png "message admin page") | ![Newsletter Admin](documentation/testing/responsiveness/macbook/macbook_newsletter_admin.png "newsletter admin page") | Works as expected. |
| 2K Monitor | ![Product Admin](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_product_admin.png "product admin page") | ![FAQ Admin](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_faq_admin.png "faq admin page") | ![Message Admin](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_message_admin.png "message admin page") | ![Newsletter Admin](documentation/testing/responsiveness/2K_desktop_screen/2K_screen_newsletter_admin.png "newsletter admin page") | Works as expected. |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Safari | Edge | Notes |
| --- | --- | --- | --- | --- | --- |
| Login | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_login.png "chrome login") | ![Firefox Screenshot](documentation/testing/browser_compatibility//firefox/firefox_login.png "firefox login") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_login.png "safari login") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_login.png "edge login") | No issues found. |
| Logout | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_logout.png "chrome logout") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_logout.png "firefox logout") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_logout.png "safari logout") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_logout.png "edge logout") | No issues found. |
| Signup | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_signup.png "chrome signup") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_signup.png "firefox signup") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_signup.png "safari signup") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_signup.png "edge signup") | No issues found. |
| Homepage | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_homepage.png "chrome homepage") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_homepage.png "firefox homepage") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_homepage.png "safari homepage") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_homepage.png "edge homepage") | No issues found. |
| Products | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_products.png "chrome products") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_products.png "firefox products") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_products.png "safari products") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_products.png "edge products") | No issues found. |
| Product Detail | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_product_detail.png "chrome product detail") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_product_detail.png "firefox product detail") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_product_detail.png "safari product detail") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_product_detail.png "edge product detail") | No issues found. |
| Basket View | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_basket.png "chrome basket view") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_basket.png "firefox basket view") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_basket.png "safari basket view") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_basket.png "edge basket view") | No issues found. |
| Checkout | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_checkout.png "chrome checkout") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_checkout.png "firefox checkout") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_checkout.png "safari checkout") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_checkout.png "edge checkout") | No issues found. |
| Checkout Success | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_checkout_success.png "chrome checkout success") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_checkout_success.png "firefox checkout success") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_checkout_success.png "safari checkout success") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_checkout_success.png "edge checkout success") | No issues found. |
| Profile | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_profile.png "chrome profile page") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_profile.png "firefox profile page") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_profile.png "safari profile page") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_profile.png "edge profile page") | No issues found. |
| FAQ | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_faqs.png "chrome faq page") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_faqs.png "firefox faq page") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_faqs.png "safari faq page") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_faqs.png "edge faq page") | No issues found. |
| Contact Us | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_contact_us.png "chrome contact us") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_contact_us.png "firefox contact us") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_contact_us.png "safari contact us") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_contact_us.png "edge contact us") | No issues found. |
| Contact Us Thank You | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_thankyou.png "chrome contact us acknowledgement") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_thankyou.png "firefox contact us acknowledgement") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_thankyou.png "safari contact us acknowledgement") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_thankyou.png "edge contact us acknowledgement") | No issues found. |
| Newsletter | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_newsletter.png "chrome newsletter") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_newsletter.png "firefox newsletter") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_newsletter.png "safari newsletter") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_newsletter.png "edge newsletter") | No issues found. |
| Newsletter Success | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_newsletter_success.png "chrome newsletter success") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_newsletter_success.png "firefox newsletter success") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_newsletter_success.png "newsletter success") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_newsletter_success.png "edge newsletter success") | No issues found. |
| Returns Policy | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_returns.png "chrome returns") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_returns.png "firefox returns") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_returns.png "safari returns") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_returns.png "edge returns") | No issues found. |
| Privacy Statement | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_privacy.png "chrome privacy") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_privacy.png "firefox privacy") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_privacy.png "safari privacy") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_privacy.png "edge privacy") | No issues found. |
| Terms and Conditions | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_terms.png "chrome terms and conditions") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_terms.png "firefox terms and conditions") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_terms.png "safari terms and conditions") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_terms.png "edge terms and conditions") | No issues found. |
| Product Admin | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_product_admin.png "chrome product admin") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_product_admin.png "firefox product admin") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_product_admin.png "safari product admin") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_product_admin.png "edge product admin") | No issues found. |
| FAQ Admin | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_faq_admin.png "chrome faq admin") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_faq_admin.png "firefox faq admin") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_faq_admin.png "safari faq admin") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_faq_admin.png "edge faq admin") | No issues found. |
| Message Admin | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_message_admin.png "chrome message admin") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_message_admin.png "firefox message admin") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_message_admin.png "safari message admin") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_message_admin.png "edge message admin") | No issues found. |
| Newsletter Admin | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_newsletter_admin.png "chrome newsletter admin") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_newsletter_admin.png "firefox newsletter admin") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_newsletter_admin.png "safari newsletter admin") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_newsletter_admin.png "edge mewsletter admin") | No issues found. |
| 404 | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_404.png "chrome 404 page") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_404.png "firefox 404 page") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_404.png "safari 404 page") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_404.png "edge 404 page") | No issues found. |
| 500 | ![Chrome Screenshot](documentation/testing/browser_compatibility/chrome/chrome_500.png "chrome 500 page") | ![Firefox Screenshot](documentation/testing/browser_compatibility/firefox/firefox_500.png "firefox 500 page") | ![Safari Screenshot](documentation/testing/browser_compatibility/safari/safari_500.png "safari 500 page") | ![Edge Screenshot](documentation/testing/browser_compatibility/edge/edge_500.png "edge 500 page") | No issues found. |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Login | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_login.png "mobile login") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_login.png "desktop login") | Minor performance warnings. |
| Logout | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_logout.png "mobile logout") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_logout.png "desktop logout") | Minor performance warnings. |
| Signup | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_signup.png "mobile signup") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_signup.png "desktop signup") | Minor performance warnings. |
| Homepage | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_homepage.png "mobile homepage") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_homepage.png "desktop homepage") | Minor performance warnings. |
| Products | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_products.png "mobile products") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_products.png "desktop products") | Minor performance warnings. |
| Product Detail | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_product_detail.png "mobile product details") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_product_detail.png "desktop product details") | n/a |
| Basket | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_basket.png "mobile basket") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_basket.png "desktop basket") | Minor performance warnings. |
| Checkout | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_checkout.png "mobile checkout") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_checkout.png "desktop checkout") | Lower Best Practise scores due to third party cookies from Stripe. |
| Checkout Success | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_checkout_success.png "mobile checkout success") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_checkout_success.png "desktop checkout success") | Minor performance warnings. |
| Profile | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_profile.png "mobile profile") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_profile.png "desktop profile") | Minor performance warnings. |
| FAQs | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_faqs.png "mobile faqs") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_faqs.png "desktop faqs") | Minor performance warnings. |
| Contact Us | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_contact_us.png "mobile contact us") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_contact_us.png "desktop contact us") | Minor performance warnings. |
| Contact Us Acknowledgement | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_thankyou.png "mobile contact us acknowledgement") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_thankyou.png "desktop contact us acknowledgement") | n/a |
| Newsletter | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_newsletter.png "mobile newsletter") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_newsletter.png "desktop newsletter") | Minor performance warnings. |
| Newsletter Success | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_newsletter_success.png "mobile newsletter success") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_newsletter_success.png "desktop newsletter success") | n/a |
| Returns Policy | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_returns.png "mobile returns") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_returns.png "desktop returns") | Minor performance warnings. |
| Privacy Statement | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_privacy.png "mobile privacy") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_privacy.png "desktop privacy") | Minor performance warnings. |
| Terms and Conditions | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_terms.png "mobile terms") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_terms.png "desktop terms") | Minor performance warnings. |
| Product Admin | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_product_admin.png "mobile product admin") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_product_admin.png "desktop product admin") | Minor performance warnings. |
| FAQ Admin | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_faq_admin.png "mobile faq admin") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_faq_admin.png "desktop faq admin") | Minor performance warnings. |
| Message Admin | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_message_admin.png "mobile message admin") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_message_admin.png "desktop message admin") | Minor performance warnings. |
| Newsletter Admin | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_newsletter_admin.png "mobile newsletter admin") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_newsletter_admin.png "desktop newsletter admin") | Minor performance warnings. |
| 404 Page | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_404.png "mobile 404 page") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_404.png "desktop 404 page") | Lower Best Practise and SEO scores due to 404 error. |
| 500 Page | ![Lighthouse Mobile](documentation/testing/lighthouse/mobile/mobile_500.png "mobile 500 page") | ![Lighthouse Desktop](documentation/testing/lighthouse/desktop/desktop_500.png "desktop 500 page") | Lower Best Practise and SEO scores due to 500 error. |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

### Creating a new user account
| Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- |
| New user clicks on sign up link and is taken to the sign up page | Tested by clicking on the signup link on the login page | SUCCESS - user is taken to signup page | ![screenrecording](documentation/testing/manual_testing/signup/mt_signup_link.gif "treasures untold testing signup link") |
| New user clicks signup without entering any info and is informed of required fields. | Clicking on the signup button without entering data. | SUCCESS - user is informed that the form is not complete | ![screenrecording](documentation/testing/manual_testing/signup/mt_signup_blank_form.gif "treasures untold testing signup process") |
| New user clicks signup after entering just an email and is informed of required fields. | Clicking on the signup button with just an email entered. | SUCCESS - user is informed that the form is not complete | ![screenrecording](documentation/testing/manual_testing/signup/mt_signup_just_email.gif "treasures untold testing signup process") |
| New user clicks signup after entering just a username and is informed of required fields. | Clicking on the signup button with just a username entered. | SUCCESS - user is informed that the form is not complete | ![screenrecording](documentation/testing/manual_testing/signup/mt_signup_just_username.gif "treasures untold testing signup process") |
| New user clicks signup after entering just a password and is informed of required fields. | Clicking on the signup button with just a password entered. | SUCCESS - user is informed that the form is not complete | ![screenrecording](documentation/testing/manual_testing/signup/mt_signup_just_password.gif "treasures untold testing signup process") |
| New user clicks signup after entering an invalid email and is informed of this. | Clicking on the signup button with an invalid email. | SUCCESS - user is informed that the form is not valid | ![screenrecording](documentation/testing/manual_testing/signup/mt_signup_invalid_email.gif "treasures untold testing signup process") |
| New user clicks signup after entering an invalid username and is informed of this. | Clicking on the signup button with an invalid username. | SUCCESS - user is informed that the form is not valid | ![screenrecording](documentation/testing/manual_testing/signup/mt_signup_invalid_username.gif "treasures untold testing signup process") |
| New user clicks signup after entering an invalid password and is informed of this. | Clicking on the signup button with an invalid password. | SUCCESS - user is informed that the form is not valid | ![screenrecording](documentation/testing/manual_testing/signup/mt_signup_invalid_password.gif "treasures untold testing signup process") |
| New user clicks signup after entering mismatching emails and is informed of this. | Clicking on the signup button with mismatched emails. | SUCCESS - user is informed that the form is not valid | ![screenrecording](documentation/testing/manual_testing/signup/mt_signup_mismatch_emails.gif "treasures untold testing signup process") |
| New user clicks signup after entering mismatching passwords and is informed of this. | Clicking on the signup button with mismatched passwords. | SUCCESS - user is informed that the form is not valid | ![screenrecording](documentation/testing/manual_testing/signup/mt_signup_mismatch_password.gif "treasures untold testing signup process") |
| New user clicks signup after entering valid email, username and password. The account activation email is sent.  | Clicking on the signup button with valid info. | SUCCESS - user is sent and activation email | ![screenrecording](documentation/testing/manual_testing/signup/mt_signup_success.gif "treasures untold testing signup process") |
| New user clicks on the link in the email received. They are taken to the site to confirm account activation | Click on the link in the email received and confirm account activation. | SUCCESS - account is activated and the user can now log in | ![screenshot](documentation/testing/manual_testing/signup/mt_signup_activate.gif "treasures untold testing signup process") |

### Logging in
| Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- |
| User clicks on sign in without entering username or password and is informed of required fields. | Clicking on sign in without entering username or password. | SUCCESS - user is informed that the form is not complete. | ![screenrecording](documentation/testing/manual_testing/login/mt_login_blank.gif "treasures untold testing login process") |
| User clicks on sign in without entering password and is informed of required fields. | Clicking on sign in without entering password. | SUCCESS - user is informed that the form is not complete. | ![screenrecording](documentation/testing/manual_testing/login/mt_login_just_username.gif "treasures untold testing login process") |
| User clicks on sign in without entering username and is informed of required fields. | Clicking on sign in without entering username. | SUCCESS - user is informed that the form is not complete. | ![screenrecording](documentation/testing/manual_testing/login/mt_login_just_password.gif "treasures untold testing login process") |
| User clicks on sign in with invalid username or password and is informed of invalid input. | Clicking on sign in with invalid username or password. | SUCCESS - user is informed that the form is not valid. | ![screenrecording](documentation/testing/manual_testing/login/mt_login_invalid_match.gif "treasures untold testing login process") |
| User clicks on sign in with valid username an password and is taken to homepage. | Clicking on sign in with valid username and password. | SUCCESS - user is logged in and taken to homepage. | ![screenrecording](documentation/testing/manual_testing/login/mt_login_success.gif "treasures untold testing login process") |

### Resetting password
| Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- |
| User clicks on forgot password link and is taken to the page to enter an email address | Clicking on forgot password link. | SUCCESS - user is taken to the page to input an email address | ![screenrecording](documentation/testing/manual_testing/account_recovery/mt_recovery_link.gif "treasures untold testing forgot password process") |
| User enters no email address in forgot password field and is informed of required field. | Not entering an email address into the form. | SUCCESS - user is informed of required field | ![screenrecording](documentation/testing/manual_testing/account_recovery/mt_recovery_initial_blank.gif "treasures untold testing forgot password process") |
| User enters invalid email address in forgot password field and is informed of invalid form. | Entering an invalid email into the form. | SUCCESS - user is informed of invalid email address | ![screenrecording](documentation/testing/manual_testing/account_recovery/mt_recovery_initial_invalid.gif "treasures untold testing forgot password process") |
| User enters valid email address in forgot password field and is shown confirmation page. | Entering a valid email into the form. | SUCCESS - user is shown the confirmation page | ![screenrecording](documentation/testing/manual_testing/account_recovery/mt_recovery_initial_success.gif "treasures untold testing forgot password process") |
| User receives an email with link to reset password. | Checking to see if email is received. | SUCCESS - email is received with link to reset | ![screenrecording](documentation/testing/manual_testing/account_recovery/mt_recovery_email.png "treasures untold testing forgot password process") |
| User enters nothing in password reset form and is informed of required fields. | Entering nothing the fields and submitting form. | SUCCESS - user is informed of invalid form | ![screenrecording](documentation/testing/manual_testing/account_recovery/mt_recovery_blank.gif "treasures untold testing forgot password process") |
| User enters invalid password in form and is informed of invalid form. | Entering invalid passwords in the fields and submitting form. | SUCCESS - user is informed of invalid form | ![screenrecording](documentation/testing/manual_testing/account_recovery/mt_recovery_invalid.gif "treasures untold testing forgot password process") |
| User enters mismatched passwords in form and is informed of invalid form. | Entering mismatched passwords in the fields and submitting form. | SUCCESS - user is informed of invalid form | ![screenrecording](documentation/testing/manual_testing/account_recovery/mt_recovery_mismatch.gif "treasures untold testing forgot password process") |
| User enters correct input in password reset form and is shown the confirmation page. | Entering matching valid passwords in the fields and submitting form. | SUCCESS - user is shown the confirmation page | ![screenrecording](documentation/testing/manual_testing/account_recovery/mt_recovery_success.gif "treasures untold testing forgot password process") |
| User clicks on Sign In to return to login page. | Clicking on Sign In from the password reset confirmation page. | SUCCESS - user is taken to the login page. | ![screenrecording](documentation/testing/manual_testing/account_recovery/mt_recovery_complete.gif "treasures untold testing forgot password process") |

### Logging out
| Expectation | Test | Result | Screenshot Mobile | Screenshot Desktop |
| --- | --- | --- | --- | --- |
| User can easily access the sign out button from all main pages in the site. The sign out button is in the same place on all pages. Clicking on the sign out button prompts the user to confirm they want to sign out. | Click on the sign out button. | SUCCESS - Upon clicking the button the user is prompted to confirm. | ![screenrecording](documentation/testing/manual_testing/logout/mt_logout_mobile_logout.gif "treasures untold testing logging out") | ![screenrecording](documentation/testing/manual_testing/logout/mt_logout_desktop_logout.gif "treasures untold testing logging out") |
| User can cancel the logout process by clicking on cancel. They will be taken back to the home screen. | Click on the cancel button in the logout prompt. | SUCCESS - the user is taken back to the home page. | ![screenrecording](documentation/testing/manual_testing/logout/mt_logout_mobile_cancel.gif "treasures untold testing logging out") | ![screenrecording](documentation/testing/manual_testing/logout/mt_logout_desktop_cancel.gif "treasures untold testing logging out") |
| User clicks on sign out and is taken to the logon screen. They are notified that they logged out. | Click on sign out on the confirmation prompt. | SUCCESS - user is logged out and notified. | ![screenrecording](documentation/testing/manual_testing/logout/mt_logout_mobile_confirm.gif "treasures untold testing logging out") | ![screenrecording](documentation/testing/manual_testing/logout/mt_logout_desktop_confirm.gif "treasures untold testing logging out") |



| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Products | Feature is expected to allow users to browse products without registration. | Opened product pages as a guest user. | Products were fully accessible without requiring registration. | ![screenshot](documentation/defensive/products.png) |
| | Feature is expected to sort products by price and name. | Tested sorting options for price (low-to-high/high-to-low) and name (alphabetical). | Sorting worked correctly for all options. | ![screenshot](documentation/defensive/sorting.png) |
| | Feature is expected to filter products by category. | Applied category filters while browsing products. | Filters worked as expected, displaying only relevant products. | ![screenshot](documentation/defensive/filtering.png) |
| | Feature is expected to show detailed product information. | Clicked on individual products to view details. | Product details (description, price, image) were displayed correctly. | ![screenshot](documentation/defensive/product-details.png) |
| Shopping Cart | Feature is expected to allow customers to add items to the cart with quantity controls. | Added products to the cart and adjusted quantities. | Items were added successfully, and quantities updated as expected. | ![screenshot](documentation/defensive/add-to-cart.png) |
| | Feature is expected to allow customers to view and manage their cart. | Opened the cart page and edited cart contents. | Cart contents were displayed, updated, and removed correctly. | ![screenshot](documentation/defensive/manage-cart.png) |
| Checkout | Feature is expected to display cart items, grand total, and input fields for checkout. | Proceeded to checkout with items in the cart. | Checkout page displayed cart items, total, and input fields as expected. | ![screenshot](documentation/defensive/checkout.png) |
| | Feature is expected to allow secure payment via Stripe. | Entered valid card details using Stripe at checkout. | Payment was processed securely, and an order confirmation page was displayed. | ![screenshot](documentation/defensive/stripe-payment.png) |
| | Feature is expected to send a confirmation email after purchase. | Completed a purchase and checked email inbox. | Confirmation email was received with order details. | ![screenshot](documentation/defensive/confirmation-email.png) |
| | Feature is expected to display an order confirmation page with an order number. | Completed a purchase. | Order confirmation page displayed successfully with an order number. | ![screenshot](documentation/defensive/order-confirmation.png) |
| Account Management | Feature is expected to allow returning customers to log in and view past orders. | Logged in as a returning customer and accessed order history. | Past orders were displayed correctly in the account section. | ![screenshot](documentation/defensive/order-history.png) |
| | Feature is expected to remember the shipping address for returning customers. | Completed multiple checkouts as a returning customer. | Shipping address was pre-filled on subsequent purchases. | ![screenshot](documentation/defensive/saved-address.png) |
| Admin Features | Feature is expected to allow the site owner to create new products. | Created new products with valid data (name, price, description, image, category). | Products were added successfully and displayed on the site. | ![screenshot](documentation/defensive/create-product.png) |
| | Feature is expected to allow the site owner to update product details. | Edited product details as an admin user. | Product updates were saved and displayed correctly. | ![screenshot](documentation/defensive/update-product.png) |
| | Feature is expected to allow the site owner to delete products. | Deleted a product from the inventory. | Product was removed successfully from the site, after being prompted to confirm first. | ![screenshot](documentation/defensive/delete-product.png) |
| Orders | Feature is expected to allow the site owner to view all orders placed. | Accessed the orders dashboard as an admin user. | All orders were displayed correctly. | ![screenshot](documentation/defensive/view-orders.png) |
| Newsletter | Feature is expected to allow users to sign up for the newsletter. | Submitted valid email addresses for newsletter registration. | Email addresses were successfully added to the newsletter list. | ![screenshot](documentation/defensive/newsletter.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |

## User Story Testing

**Database Setup**
| Target | Expectation | Outcome | File | Screenshot |
| --- | --- | --- | :---: | --- |
| As a developer | I can create a JSON fixtures file for the product model | so that I can quickly and easily load products into the database. | [Product Fixtures](products/fixtures/products.json) | ![JSON Product Fixtures](documentation/testing/user_stories/products_fixtures.png "product fixtures") |
| As a developer | I can create a JSON fixtures file for the realm model | so that I can quickly and easily load realms into the database. | [Realm Fixtures](products/fixtures/realms.json) | ![JSON Realm Fixtures](documentation/testing/user_stories/realms_fixtures.png "realms fixtures") |
| As a developer | I need images for the products | so that site users can see the product. | n/a | ![Product Images](documentation/testing/user_stories/product_images.png "product images") |

**Viewing and Navigating Products**
| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a site user | I can see a homepage full of useful information | so that I can see what the site is and why I should spend my time here. | ![Homepage](documentation/testing/browser_compatibility/chrome/chrome_homepage.png "homepage") |
| As a user | I can view the available items | so that I can decide if I'd like to buy one or some of them. | ![Products page](documentation/features/viewing_products/desktop_all_products.png "products") |
| As a user | I can click on a product | so that I can see more detailed info on the product. | ![Product detail page](documentation/features/product_details/desktop_detail_stocked.png "product details") |
| As a user | I can access my shopping basket from anywhere | so that I can keep track of my current total and avoid spending too much. | ![Shopping basket](documentation/features/basket_view/desktop_basket_preview.png "basket preview") |
| As a user | I can easily see if items are out of stock | so that I know I cannot buy them. | ![Out of stock items](documentation/features/product_details/unavailable_items.png "unavailable stock") |
| As a user | I can see a custom 404 error page | so that I know the page I’m looking for doesn’t exist and can easily navigate back to the rest of the site. | ![404 page](documentation/features/error_pages/desktop_404.png "404 page") |
| As a user | I can see a custom 500 error page | so that I understand something went wrong on the server and can find a way to navigate back to the site. | ![500 page](documentation/features/error_pages/desktop_500.png "500 page") |
| As a user | I can sign up to be notified if an item that is sold or out of stock becomes available | so that I can purchase it. | **Not implemented in this iteration.** |
| As a user | I can share products directly to social media platforms | so that I can share items with my friends easily. | **Not implemented in this iteration.** |

**User Accounts**
| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a user | I can create an account | so that I can purchase items and view/edit my own profile. | ![account creation](documentation/features/user_accounts/desktop_register.png "create an account") |
| As a user | I can easily log in and out of my account | so that my details remain private and secure. | ![logging in](documentation/features/user_accounts/desktop_login.png "log in") ![logging out](documentation/features/user_accounts/desktop_logout.png "log out") |
| As a user | I can easily recover my account and change password | so that I can continue to log in and out if I forget my password. | ![Account recovery](documentation/testing/user_stories/password_reset.png "password reset") ![Recovery Email](documentation/testing/user_stories/email_reset_email.png "email reset email") |
| As a user | I should receive a verification email when I create my account | so that I can confirm my email address and activate my account. | ![Email account creation](documentation/testing/user_stories/account_creation_email.png "account creation email") |
| As a user | I can view a user profile page | so that I can see my purchase history and update my details. | ![Profile page](documentation/features/profile_page/desktop_profile_page.png "profile page") |
| As a developer | I can implement a social media login | so that users can create accounts quickly and easily. | **Not implemented in this iteration.** |

**Sorting and searching for items**
| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a user | I can search manually for an item from an input field | so that I can find and view specific items quickly. | ![Search Bar](documentation/testing/user_stories/search_bar.png "search bar") |
| As a user | I can sort products | so that view the list of products sorted based on a selected property. | ![Result sorting](documentation/testing/user_stories/order_items.png "product sorting") |
| As a user | I can filter products | so that only products that match the filter property are shown. | ![Filter products](documentation/features/navigation/desktop_sort_filter.png "product filtering") |
| As a user | I can sort search and filter results | so that I can view the results in the order that I want to. | ![Result sorting](documentation/testing/user_stories/order_items.png "product sorting") |

**Purchasing and checkout**
| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a user | I can select how many of a product I wish to buy | so that I can add the amount I need in one process to the basket. | ![Quantity modifier](documentation/features/product_details/stocked_product_updating.gif "quantity selection") |
| As a user | I can view the basket | so that see the total cost and all the items I have added to it. | ![Basket view](documentation/features/basket_view/desktop_basket_page.png "basket view") |
| As a user | I can adjust the quantity of product from the basket | so that I can easily edit how many I want. | ![Basket view quantity adjusting](documentation/testing/user_stories/adjusting_quanity_in_basket_view.gif "adjusting quantity in basket view") |
| As a user | I can remove an item directly from the basket | so that I can quickly adjust what I'm buying. | ![Removing item from basket](documentation/testing/user_stories/removing_item_from_basket.gif "removing item from basket") |
| As a user | I can easily enter my payment details | so that checkout quickly and hassle free. | ![Checkout payment form](documentation/features/checkout_view/desktop_checkout.png "checkout process") |
| As a user | I can see an order confirmation after completing a purchase | so that I know the transaction was successful. | ![Order confirmation](documentation/features/checkout_view/desktop_checkout_success.png "order confirmation") |
| As a user | I receive an email confirming my order confirmation and details | so that I know the transaction was successful. | ![Email order confirmation](documentation/features/checkout_view/checkout_success_email.png "email order confirmation") |
| As a developer | I can expand the application to support multiple currencies | so that users can view and complete transactions in their preferred currency, improving accessibility and user experience. |  **Not implemented in this iteration.** |

**Help and support page**
| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a user | I can send a message to the shop owner | so that if I have a question or message I can send it directly with my details so that they can get back to me. | ![Contact Us](documentation/features/support_pages/desktop_contact_us.png "contact us") |
| As a user | I can view the FAQ on the help and support page | so that I may find the answer to a question I have before sending a message to ask. | ![FAQs](documentation/features/support_pages/desktop_faq_expanded.png "faqs") |
| As a user | I can sign up to a newsletter | so that I can be informed when new magical items have been found and added to the store for sale. | ![Newsletter](documentation/features/support_pages/desktop_newsletter_page.png "newsletter") |
| As a user | I can view the sites privacy policy | so that I can see how my data is stored and used. | ![Privacy Policy](documentation/features/support_pages/desktop_privacy.png "privacy statement") |
| As a user | I can view the sites returns policy | so that I can see how the returns process works should I not be happy with a purchase. | ![Returns Policy](documentation/features/support_pages/desktop_returns_policy.png "returns policy") |
| As a user | I can view the sites general terms and conditions | so that I can I can understand the rules, policies, and my rights when using the website. | ![Terms and Conditions](documentation/features/support_pages/desktop_terms.png "terms and conditions") |

**Admin and store management**
| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a shop owner | I can access a shop admin page | so that they add edit and delete products so that they can keep the catalogue up to date. | ![Staff Dashboard](documentation/features/dashboard/desktop_product_admin.png "staff dashboard") |
| As a shop owner | I can add a new product | so that the shop can be updated with new items. | ![Add a product](documentation/features/dashboard/product_admin/desktop_product_add.png "adding a product") |
| As a shop owner | I can edit products | so that I can update prices, stock levels and keep the catalogue up to date. | ![Edit a product](documentation/features/dashboard/product_admin/desktop_product_update.png "update a product") |
| As a shop owner | I can delete products from the catalogue | so that I can make sure the catalogue is up to date. | ![Delete a product](documentation/features/dashboard/product_admin/desktop_product_delete.png "deleting a product") |
| As a shop owner | I can add new questions and answers to the FAQ section of the help and support page | so that site users have the most up to date FAQ. | ![Adding a FAQ](documentation/features/dashboard/faq_admin/desktop_faq_add.png "adding a faq") |
| As a shop owner | I can edit any FAQ entries | so that amend any that I need to. | ![Editing a FAQ](documentation/features/dashboard/faq_admin/desktop_faq_update.png "updating a faq") |
| As a shop owner | I can delete FAQ entries | so that I can keep the list up to date by removing any redundant entries. | ![Deleting a FAQ](documentation/features/dashboard/faq_admin/desktop_faq_delete.png "deleting a faq") |
| As a shop owner | I can view the messages sent from the contact us form | so that I can send an initial reply. | ![Message Viewing](documentation/features/dashboard/message_admin/messages.png "message viewing") |
| As a shop owner | I can manage newsletters including viewing previous newsletters and creating and sending newsletters | so that subscribers can be updated on any offers and news from the site. | ![Newsletter admin](documentation/features/dashboard/newsletter_admin/newsletters.png "newsletters") ![Creating newsletter](documentation/features/dashboard/newsletter_admin/desktop_newsletter_send.png "creating newsletter") |
| As a shop owner | I can see a list of the current subscribers including active, pending and expired memberships. I can also remove any individual subscriber and clear all expired subscribers from the list | so that I can I can keep the subscriber list accurate, organised, and up to date. | ![Subscribers](documentation/features/dashboard/newsletter_admin/subscribers.png "subscribers") ![Clearing expired](documentation/features/dashboard/newsletter_admin/desktop_clear_expired.png "clearing expired") |

**Easter Eggs**
| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a curious user | I can enter a classic phrase in the search bar | so that a special reward is unlocked! | ![Easter Egg](documentation/features/communication/message_toasts/reward_notification.png "easter egg notification") |
| As a curious user | I might notice that upon hovering over a certain item the cursor changes, | should I perform a certain action a special reward is unlocked! | ![Easter Egg](documentation/features/easter_eggs/reward_message_magic_lamp.png "easter egg notification") |
| As a curious user | I might know about the Cave of Wonders in Agrabah and know what I need to gain access | to unlock a special reward... | ![Easter Egg](documentation/features/easter_eggs/reward_message_cave_of_wonders.png "easter egg notification") |
| As a greedy user | I might not be able to stop myself from wanting a particular product when a certain reward is activated | and I will see the consequences... | ![Easter Egg](documentation/features/easter_eggs/reward_message_infidels.png "easter egg notification") |

**SEO and Marketing**
| Target | Expectation | Outcome | File | Screenshot |
| --- | --- | --- | :---: | --- |
| As a developer | I need to implement good marketing strategies | so that the site gains exposure and attracts customers. | n/a | ![Facebook Page Mockup](documentation/seo_marketing/marketing_facebook.png "facebook mockup") |
| As a developer | I can make sure that SEO methods are used in the site | so that it ranks higher in search engine results, attracts more organic traffic, and provides a better user experience. | [robots.txt](/robots.txt) [sitemap.xml](/sitemap.xml) | ![robots.txt](documentation/testing/user_stories/robots.png "robots.txt") ![sitemap.xml](documentation/testing/user_stories/sitemap.png "sitemap.xml") |

## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

⚠️ INSTRUCTIONS ⚠️

Adjust the code below (file names, function names, etc.) to match your own project files/folders. Use these notes loosely when documenting your own Python Unit tests, and remove/adjust where applicable.

⚠️ SAMPLE ⚠️

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py,manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python3 -m http.server`

Below are the results from the full coverage report on my application that I've tested:

![screenshot](documentation/automation/html-coverage.png)

#### Unit Test Issues

⚠️ INSTRUCTIONS ⚠️

Use this section to list any known issues you ran into while writing your Python unit tests. Remember to include screenshots (where possible), and a solution to the issue (if known). This can be used for both "fixed" and "unresolved" issues. Remove this sub-section entirely if you somehow didn't run into any issues while working with your tests.

⚠️ --- END --- ⚠️

## Bugs

⚠️ INSTRUCTIONS ⚠️

Nobody likes bugs,... except the assessors! Projects seem more suspicious if a student doesn't properly track their bugs. If you're about to submit your project without any bugs listed below, you should ask yourself why you're doing this course in the first place, if you're able to build this entire application without running into any bugs. The best thing you can do for any project is to document your bugs! Not only does it show the true stages of development, but think of it as breadcrumbs for yourself in the future, should you encounter the same/similar bug again, it acts as a gentle reminder on what you did to fix the bug.

If/when you encounter bugs during the development stages of your project, you should document them here, ideally with a screenshot explaining what the issue was, and what you did to fix the bug.

Alternatively, an improved way to manage bugs is to use the built-in **[Issues](https://www.github.com/apeskinian/p5_treasures_untold/issues)** tracker on your GitHub repository. This can be found at the top of your repository, the tab called "Issues".

If using the Issues tracker for bug management, you can simplify the documentation process for testing. Issues allow you to directly paste screenshots into the issue page without having to first save the screenshot locally. You can add labels to your issues (e.g. `bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s). Once you've solved the issue/bug, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following examples below.

⚠️ --- END --- ⚠️

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Aapeskinian%2Fp5_treasures_untold%20label%3Abug&label=bugs)](https://www.github.com/apeskinian/p5_treasures_untold/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/apeskinian/p5_treasures_untold/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/apeskinian/p5_treasures_untold/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

⚠️ INSTRUCTIONS ⚠️

You will need to mention any unfixed bugs and why they are not fixed upon submission of your project. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. Where possible, you must fix all outstanding bugs, unless outside of your control.

If you've identified any unfixed bugs, no matter how small, be sure to list them here! It's better to be honest and list them, because if it's not documented and an assessor finds the issue, they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

⚠️ --- END --- ⚠️

[![GitHub issues](https://img.shields.io/github/issues/apeskinian/p5_treasures_untold)](https://www.github.com/apeskinian/p5_treasures_untold/issues)

Any remaining open issues can be tracked [here](https://www.github.com/apeskinian/p5_treasures_untold/issues).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| On devices smaller than 375px, the page starts to have horizontal `overflow-x` scrolling. | ![screenshot](documentation/issues/overflow.png) |
| When validating HTML with a semantic `<section>` element, the validator warns about lacking a header `h2-h6`. This is acceptable. | ![screenshot](documentation/issues/section-header.png) |
| Validation errors on "signup.html" coming from the Django Allauth package. | ![screenshot](documentation/issues/allauth.png) |
| With a known order-number, users can brute-force "checkout_success.html" and see potentially sensitive information. | ![screenshot](documentation/issues/checkout-success.png) |
| If a product is in your bag/cart, but then gets deleted from the database, it throws errors from the session storage memory. | ![screenshot](documentation/issues/session-storage.png) |
| The `-`/`+` quantity buttons work well on "product_details.html", but not on "bag.html". | ![screenshot](documentation/issues/quantity-buttons.png) |

> [!IMPORTANT]
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

