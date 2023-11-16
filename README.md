#__dotThink: A web-based personal diary app__
#### Video Demo: <https://youtu.be/iYlONk5Uo1E>

## __Description__
dotThink is a web-based personal diary app to store all your memories.

Project features :
- Login and Register: dotThink allows you to create an account where you can store all your personal memories and thoughts safely. dotThink doesn’t allow anyone to get access to your credentials which are stored safely on dotThink servers

- Create, edit, or delete entries: dotThink lets you create new memories and store them in one place. You can edit your existing memories if you want to add more to your valuable memories. If you wish to delete any memory for some reason, dotThink offers you a simple delete button.

- Favorite your special entries: We all have some very special memories we wish to keep safe. They are very close to our hearts. dotThink values your feelings and lets you save your important memories in a favorites section where you can relive those memories again!

- Simple and elegant design: dotThink is made for everyone. With that thought, dotThink offers a very simple and beautiful design to suit everyone. It has gorgeous color patterns and also smooth animations to make your experience even better!

## **Installation**
All required libraries for dotThink can be installed using pip

Just type the following command in the terminal and install all the necessary libraries
```
pip install -r requirements.txt
```

After installation make all the migrations using these commands
```
python manage.py makemigrations
python manage.py migrate
```

Now, run the server using this command
```
python manage.py runserver
```

## __Specifications__

### __Views__
The project has multiple views to handle login, logout, register, create entry, delete entry, and favorite <br>
```Login view``` makes sure that the user is a valid user and then logs in. <br>
```Register view``` helps in registering the new users. <br>
```index view``` this view lets the user see all their entries and lets them add new entries, edit or delete existing entries, and favorite the special entries. <br>
```create view``` lets you create the entries. <br>
```edit view``` lets you edit the entries that are already there in the list. <br>
```delete view``` lets you delete any existing entry. <br>
```favorites view``` lets you see all the favorite entries that are already inside the favorites tab. <br>
```favorites toggle view``` lets you add or remove the entries from the favorites tab.

### __Models__
The project has one model ```DiaryEntry``` to support all the functions.

### __Forms__
The project has one form ```DiaryEntryForm``` for getting diary entry information.

### __Urls__
The project has multiple URLs for all the functions of the website <br>
```default page``` to load homepage. <br>
```login page``` to load login form. <br>
```register page``` to load register form. <br>
```create page``` to load the create entry form. <br>
```edit page``` to load the edit entry form. <br>
```delete page``` to delete the entry and then load the homepage. <br>
```favorite toggle page``` to add or remove from favorites and load homepage. <br>
```favorites page``` to load favorites tab. <br>
```logout page``` to logout a user and load the login page.

### __Styling__
The project uses Bootstrap and Cloudflare CSS libraries to implement styling for the website. <br>
There is also a custom ```styles.css``` which I created to add more styles and animations to the website.

#### Project created by Yash Firke.
