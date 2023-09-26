# Assignment 4

## APP
Check out the link to my [APP](https://stockit.adaptable.app/main/)
## Answers

### 1.  What is UserCreationForm in Django? Explain its advantages and disadvantages.
UserCreationForm is a built-in form class in Django that allows us to create a new user with a username and a password.

`Advantages`:
- It is easy to use and saves you time from writing your own form class and validation logic.
- It has a built-in password confirmation field that checks if the two passwords match.
- It uses the default User model in Django, which has some useful attributes and methods for authentication and authorization.
`Disadvantages`:
- It only has two fields: username and password. If you want to add more fields to your user model, such as email, first name, last name, etc., you need to either extend the UserCreationForm class or create a custom form class that inherits from it.
- It does not provide any customization options for the appearance or behavior of the form. For example, you cannot change the labels, placeholders, help texts, error messages, or widgets of the fields. You also cannot add any extra logic or functionality to the form, such as sending a confirmation email or logging the user in after registration.
- It does not protect against brute force attacks or password cracking attempts. You may need to implement your own rate limiting mechanism or use the ones provided by your web server.

### 2.  What is the difference between authentication and authorization in Django application? Why are both important?
Authentication is the process of verifying the identity of a user, usually by asking for their username and password. Authorization is the process of granting or denying access to certain resources or actions based on the user’s identity, role, or permissions1.

Both authentication and authorization are important for security and functionality reasons. Authentication ensures that only legitimate users can access the application and prevents unauthorized access from malicious actors. Authorization ensures that users can only perform the actions that they are allowed to do and prevents abuse of privileges or data leakage. Together, authentication and authorization provide a robust and flexible way of managing user access and control in Django application.

### 3.  What are cookies in website? How does Django use cookies to manage user session data?
Cookies are small pieces of data that a website sends to a user’s web browser. The browser may store the cookie and send it back to the same website with later requests. Cookies are used to remember information about the user, such as their login, preferences, shopping cart, or other data1.

Django uses cookies to manage user session data by placing a session ID cookie on the client side, and storing all the related data on the server side. The session ID cookie is a unique identifier that Django uses to link the browser with the session data on the server. The session data is not stored in the cookie itself, but in a database or cache on the server2. This way, Django can provide a secure and efficient way of handling user sessions.

### 4.  Are cookies secure to use? Is there potential risk to be aware of?
Yes cookies are seucre to use, but they can pose some security and privacy risks if they are not handled properly. Some of the potential risks are:

- Cookie theft: If an attacker can intercept the communication between our browser and a website, they can steal the cookies and use them to impersonate us or access our sensitive information. This can happen if we use an unsecured network, such as a public Wi-Fi, or if the website does not use encryption (HTTPS) to protect the data transmission.
- Cookie tampering: If an attacker can modify the cookies on our browser or on the server, they can alter the information stored in them and cause unexpected or malicious behavior. For example, they can change our preferences, settings, or shopping cart items on a website, or inject malware code into the cookies that can execute on our browser or on the server.
- Cookie tracking: If a website or a third-party service uses cookies to track our online activity, they can collect information about our browsing habits, interests, preferences, and personal data. This can be used for targeted advertising, marketing, or profiling purposes, which may violate our privacy or expose us to unwanted content.
### 5.   Explain how you implemented the checklist above step-by-step (not just following the tutorial).
- Setting Up User Registration:

1. Start the virtual environment.
2. Open views.py inside the main folder and create a register function that accepts a request as a parameter.
3. Import redirect, UserCreationForm, and messages at the beginning of the file.
4. Use UserCreationForm to create a registration form effortlessly.
5. Handle form submission:
    - Create a new form with UserCreationForm(request.POST)
    - Validate the form with form.is_valid()
    - Save the user account with form.save()
    - Display a success message using messages.success()
    - Redirect to the login page with return redirect('main:login').
6. Create a new HTML file named register.html in the main/templates folder.
7. Extend the base template, set the title, and create a registration form with CSRF token and submit button.
8. Display success messages using {% if messages %}.

- Setting Up User Login:

1. In views.py, create a login_user function that accepts a request as a parameter.
2. Im port authenticate and login at the beginning of the file.
3. Use authenticate to verify the user's credentials.
4. If authentication is successful, log in the user using login(request, user).
5. Create an HTML file named login.html and create a login form.
6. Add error messages for incorrect login attempts.
7. Include a link to the registration page.
8. Configure URL routing to access the login_user function.

- Implementing User Logout:

1. Create a logout_user function in views.py that accepts a request as a parameter.
2. Import logout at the beginning of the file.
3. Use logout(request) to log out the user.
4. Redirect to the login page and delete the 'last_login' cookie.
5. Add a logout button to the main page in main.html.
6. Configure URL routing to access the logout_user function.

- Restricting Access to the Main Page:

1. Import login_required from django.contrib.auth.decorators in views.py.
2. Apply the @login_required decorator to the show_main function to restrict access.
3. Test the login restriction by running the Django project.

- Using Data from Cookies:

1. Import HttpResponseRedirect, reverse, and datetime in views.py.
2. Modify the login_user function to set a 'last_login' cookie when a user logs in.
3. Display the 'last login' data on the main page.
4. Modify the logout_user function to delete the 'last_login' cookie when a user logs out.
5. Run the Django project and verify the 'last_login' feature.

- Connecting the Product Model to User Model:

1. In models.py, import User from django.contrib.auth.models.
2. Add a foreign key relationship between Product and User in the Product model.
3. Modify the create_product function in views.py to associate products with the logged-in user.
4. Update the show_main function to display only the products of the logged-in user.
5. Run migrations and apply them to the database.
6. Test the functionality by creating and viewing products for different user accounts.

# Assignment 3

## APP
Check out the link to my [APP](https://stockit.adaptable.app/main/)
## Answers

### 1.  What is the difference between POST form and GET form in Django?
POST method:
    - Used to submit data from a form to a web server using the HttpPost object.
    - The data is sent internally, so it is not shown in the URL parameters. This makes it more secure than the GET method.
    - You can send unlimited data using the POST method.
    - Django uses a csrf_token to protect POST requests from cross-site request forgery (CSRF) attacks.

GET method:
    - Used to submit data from a form to a web server using URL parameters.
    - The GET method calls the HttpGet object to send data from the form to the web server.
    - All data is shown in the URL, so the GET method is not as secure as the POST method.
    - You can only send a limited amount of data using the GET method.
    - The default URL method is GET, so when you visit a web URL in your web browser, it is called using the GET method.

### 2.  What are the main differences between XML, JSON, and HTML in the context of data delivery?
XML
    - Represents data in a tree pattern
    - Uses tags to differentiate between data attributes and the actual data
    - Offers the capability to display data
    - More secure compared to JSON
    - Used to represent data in a machine-readable way
    - Still the go-to choice for transmitting structured data over the web
    - Used to store or transport data in web applications
JSON
    - Represents data using key-value pairs
    - Has no display capabilities
    - Less secured compared to XML
    - Independent of any programming language and is a common API output in a wide variety of applications
    - Used to store and transmit data
    - Gaining popularity as a storage medium for web applications because of its simplicity
    - Faster than XML because of its smaller footprint and more straightforward syntax
HTML
    - Used to format and display data
    - Not used for data interchange
    - Used to create web pages
    - Used to define the structure and content of web pages

 ### 3. Why is JSON often used in data exchange between modern web applications?
 It is because JSON is a popular data format that is easy to read and write for humans and computers. It is a lightweight alternative to XML and is used for easy parsing on the web. JSON uses a human-readable format of key-value pairs and arrays, which makes it easy to write and understand. It does not require any special tags, attributes, or schemas, unlike XML, which is another common data format for web applications. JSON supports common data types such as strings, numbers, booleans, nulls, objects, and arrays, which can be nested and combined in various ways. JSON can be easily converted to and from JavaScript objects, which makes it convenient for web developers who use JavaScript as the main scripting language for web applications. JSON's simplicity is part of its appeal, as it is easy to write, read, and translate between the data structures used by most languages.

### 4.Explain how you implemented the checklist above step-by-step (not just following the tutorial).
 1. First let's create `forms.py` inside our `main` folder.

    After we navigate inside the file `forms.py` we need to create a class named `ProductForm` for running the form by using `ModelForm ` as parameter. Inside the class we create a `META` class containing `model = Product` to point to a model used by the form. It also contain `fields = ["name",  "amount", "price", "description", "category", "location"]` to be used to select attributes of the model `Item`.
 2. Next, we create `create_product` object inside views.py

    Inside the file `views.py` we create a function named `create_product` that accept a parameter request. In `create_product` we create a new `ProductForm` filled with user input in `request.POST` as a `QueryDict`. Then we authorize the content by using `form.is_valid()` and save the content of the form by using `form.save()`. After the content has been saved, we need to transfer the user back to the main page by using `return HttpResponseRedirect(reverse('main:show_main'))`. the function will render `create_product.html`.
 3. Modify the `show_main` function inside `views.py`

    add `items = Item.objects.all()` to fetch all `item` object from the application's database.
 4. Create URL routing for `create_product`

    in `urls.py` inside `library_col` we need to add `path('create-product', create_product, name='create_product'),`.
 5. Create an HTML file `create_product.html` inside a folder named as `templates` inside the `main` folder

    Fill the HTML file with the suitable code to display the form as a table, used `{% csrf_token %}` as a security, and used `<form method="POST">` to tag the form with `POST` method.
 6. Create an object `show_xml` to show the content as XML and create the URL routing for it

    Fetched `Item` objects and return as XML by using 
    ```py
    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    in `urls.py` inside `library_col` add `path('show_xml/', show_xml, name='show_xml'),`.
 7. Create object `show_json`to show the table content as JSON and create the URL routing for it

    Fetched `Item` objects and return as XML by using 
    ```py
    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    in `urls.py` inside `library_col` add `path('show_json/', show_json, name='show_json'),`.
 8. Create object `show_xml_by_id` to search a particular object in XML views by their object's id and create the URL routing for it

    Fetched `Item` objects and return as XML by using 
    ```py
    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    in `urls.py` inside `library_col` add `path('show_xml_by_id/', show_xml_by_id, name='show_xml_by_id'),`.
 9. Create object `show_json_by_id` to search a particular object in JSON views by their object's id and create the URL routing for it

    Fetched `Item` objects and return as XML by using 
    ```py
    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    in `urls.py` inside `library_col` add `path('show_json_by_id/', show_json_by_id, name='show_json_by_id'),`.
 10. Run Postman app to view our data
     Open an app named as Postman in the same dekstop as our code, create a new request with the GET method and put the suitable URL to view the content in many ways, HTML, XML, JSON, XML by id and JSON by id

 11. Deploy our web to PBP Fasilkom UI PaaS and git add, commit and push our directory to our GitHub Repository

### Access the five URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.
<img src="/assets/Screenshot (106).png">
<img src="/assets/Screenshot (107).png">
<img src="/assets/Screenshot (108).png">
<img src="/assets/Screenshot (109).png">
<img src="/assets/Screenshot (110).png">

# Assignment 2

## APP
Check out the link to my [APP](https://stockit.adaptable.app/main/)
## Answers

### 1. How do you implement the tasks in the checklist?
1. Create a new Django Project
    - Let's first create a new folder in file explorer
    - Name the folder as free as we wanted, i named it Stockit
    - Run the folder in Visual Studio Code Terminal using Command Prompt
    - In the CMD, We need to create a Virtual Environtment by running this code:
    ```
    python -m venv env
    ```
    Then, We need to activate the environment with
    ```
    env\Scripts\activate.bat
    ```
    if we are using windows, and with
    ```
    source env/bin/activate
    ```
    if we are using Linux
    - If it is Active, in the terminal we will see (env) in the beginning of the output in the terminal
    - In the same directory, we need to create a file named `requirements.txt` and added some dependencies on it.
    - We install the dependencies of the requirements by running the command `pip install -r requirements.txt` in the terminal
    - After installing the dependencies, we start our django project by running `django-admin startproject shopping_list .`
    - Set the value of `ALLOWED_HOSTS` in `settings.py` to allow access from any host, which will make the application accessible widely
    - Make sure that is in the active folder in our VS Code, then we run our server with `python manage.py runserver`
    - We could see the server running with the given URL in the terminal, for example: `http://127.0.0.1:8000/main/`
    - Create a new GitHub repository, name it with the name we would use for the project for example: `stockit`
    - Initialize our folder to GitHub as a GitHub repository
    - After initializing, we Add a `.gitignore file` which is a configuration file used in a Git repository to specify files and directories that should be ignored by Git
    - When everything is ready, Perform `add`, `commit`, and `push` from the local repository directory.
2. Create an app with the name `main`.
    - Let's create a new application as the root directory
    - Run `python manage.py startapp main` in the env terminal to create the `main` app
    - Find `INSTALLED_APPS` and add `'main'` to register it to the list of existing applications
    - Create a folder name `templates` inside `main` and add `main.html` inside the folder
    - Then check the `main.html` in the web browser for checking the basic HTML
3. Create a URL routing configuration to access the `main` app.
    - Create a urls.py inside the `main`
    - Import path from django.urls to define the URL patterns.
    - Use the show_main function from the main.views module as the view to be displayed when the related URL is accessed.
    - Open the urls.py inside the project folder `stockit` and Import the include function from django.urls with
    ```
    from django.urls import path, include
    ```
    - Then, add `path('main/', include('main.urls')),` in the `urlpatterns` variable
4. Create a model on the `main` app with name `Item` and add some mandatory attributes
    - Inside `models.py` on the `main` app, let's add an app name `Item` and add some attributes:
        - `name` with type CharField
        - `date_added` with type DateField.
        - `amount`with type IntegerField
        - `price` with type IntegerField
        - `description` with type TextField.
        - `category` with type CharField
        - `location` with type TextField
    - Change the database schema to match the changes you've made to your models in your code by running
    ```
    python manage.py makemigrations
    ```
    and apply the migrations to the local database with `python manage.py migrate`
5. Create a function in `views.py` that returns an HTML template containing my application name, your name, and your class.
    - Inside the `views.py` we need to add a function called `show_main` with context of _app_name_, _name_, and _class_
    - Then render the context to `main.html`
    - On the main.html file that you created earlier in the templates directory within the main application, we could replace the statically created name with `{{app_name}}`, `{{name}} and `{{class}}`
6. Create a routing in `urls.py` to map the function in `views.py` to an URL
    - Create a file name `urls.py` inside the `main` app folder
    - Under `from django.urls import path` and `from main.views import show_main` add `app_name = 'main'`
    - Next, add `path('', show_main, name='show_main')` to a list variable name `urlpatterns
    - Open `urls.py` inside the `stockit` project directory
    - Inside the file, import the include function from django.urls by adding `from django.urls import path, include`
    - To direct the URL to the main view, within the urlpatterns variable add `path('main/', include('main.urls')),`
7. Deploy the app to adaptable
    - Login to Adaptable with our GitHub Account, then press the New App button
    - Choose Connect an Existing Repository and select All Repositories
    - Select our project directory which is the `stockit` folder
    - Choose `Python App Template` as the deployment template and select `PostgreSQL` as the database type to be used.
    - Select python version according to our current `python --version`, in my case the python version is 3.11.5 so i chose 3.11
    - Enter the command python manage.py migrate && gunicorn stockit.wsgi
    - Enter our app name, `stockit`
    - Checkclick on the `HTTP Listener on PORT` option and click `Deploy App` to initiate the application deployment process
  
### 2. Create a diagram explaining the flow of client requests to a Django web app and its response.
<img src="/assets/Flowchart_PBP_Assignment2.jpg">
### 3. What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?
It is possible to create a Django web without a virtual environment, but in most cases it is better to use a virtual environment. The purpose of virtual environment is to have stable, reproducible, and portable environments. Isolating the Python environment for a project from the rest of the system ensures that the dependencies for each project are consistent and can be easily replicated across different environments.
A virtual environment provides a stable environment for our project by isolating the project’s dependencies from the rest of the system. This means that changes to the system or other projects on the system will not affect the stability of our project. It can also help us easily recreate the same environment on different systems or at different times, ensuring that your project runs consistently regardless of the environment it is running in by specifying the exact versions of Python and other packages required by your project. Another advantages is that we can also easily move our  project to different systems or share it with others without having to worry about dependencies or conflicts with other projects on the system
### 4. What is MVC, MVT, and MVVM? Explain the differences between the three.
Model View Controller(MVC) is a model that is often used by software developers
  - Model: This component contains business logic and data status in the application. This component is tasked with obtaining and manipulating data, communicating with the controller, interacting with the database, and sometimes updating the appearance of the application being developed.
  - View: This component is related to the user interface consisting of HTML/CSS.XML. These components communicate with the controller and sometimes interact with the model. View works together with the controller to create a dynamic view of the application being developed. Apart from being tasked with handling the interface and user interaction, the view component also has the task of presenting appropriate data to the user.
  - Controller: The controller is an activity/fragment that functions as a communicator between the view and the model. This component requires a user input from the view/REST service. Then the “Get Data” request is processed from the model and passed to the view to be displayed to the user.
  - Advantage: MVC creates separate business logic in the Model and supports asynchronous techniques. If a modification occurs, it will not affect the entire Midel. The application development process can be carried out faster.
  - Disadvantage: This architecture can increase complexity. Unit testing is hindered and controller code is so large that developers can't manage it.
Model View Presenter(MVP) is a derivative of the MVC architectural design pattern and focuses on improving presentation logic
  - Model: The model represents a set of classes that describe business logic and data. It also describes business rules for data such as retrieving and manipulating data, and interacting with the database. The model is used to communicate with the presenter, but the model does not interact with the view.
  - View: Views are used to create interactions with users such as XML (UI), activities, and fragments as well as interacting with Presenter.
  - Presenter: The Presenter presents data from the model and controls all the behavior it wants to display from the application that drives and tells the View what to do. The interaction between the model and view is handled by the presenter. Not only that, the presenter is also tasked with saving data back to the model.
  - Advantage: It can make it easy to change views. View and Presenter can be reused for application development. Code that is easier to read and maintain. Ease of testing due to separate business logic from the UI.
  - Disadvantage: Code size is too large. The number of interfaces for interaction between separate layers. Have a close relationship between View and Presenter
Model View ViewModel(MVVM)
  - Model: The model used for MVVM is similar to the model used by MVC, where the model consists of the basic data used to run the software.
  - View: Views are used as a graphical interface between users and design patterns, and display the output of processed data. The views used by MVVM are similar to the views used in MVC.
  - ViewModel: ViewModel is on the one hand an abstraction of the View, and on the other hand, it provides a model data wrapper to link to. A ViewModel consists of a Model that is converted into a View, and contains commands that the View can use to influence the Model.
  - Advantage: There is no relationship (dependency) between View and ViewModel. There is no interface between View and Model. Easy unit testing and event-driven code.
  - Disadvantage: Developers must create a measurable quantity in each UI component. Code size is too large.
