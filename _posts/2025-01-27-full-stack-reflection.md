---
toc: true
comments: true
layout: post
title: Full Stack Reflection
---
# User Profile Feature Blog

## Purpose of the Group's Program
Our group's project is a social media platform designed to foster community engagement and holiday gifts shared among each other. It integrates both frontend and backend components, ensuring seamless user interactions through a well-structured API and an intuitive UI.

## Purpose of My Individual Feature
The feature I developed is the user profile management system, which allows users to view, update, and delete their profiles. This includes handling profile pictures, usernames, and theme preferences while ensuring secure API communication between the frontend and backend.

## Input/Output Requests
### Frontend API Request and Response Demonstration
- **Input**: Fetching user profile details using JavaScript `fetch` API.
- **Output**: JSON response containing user profile data.

```javascript
const userId = localStorage.getItem("user_id");
const apiUrl = `http://127.0.0.1:8887/user/${userId}/profile`;

async function loadProfile() {
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        document.getElementById('link').src = data.link || 'default_image.png';
        document.getElementById('username').textContent = data.name || 'Unknown User';
        document.getElementById('theme-preference').textContent = `Preferred Theme: ${data.theme || 'Light'}`;
    } catch (error) {
        console.error('Error fetching profile data:', error);
    }
}
```

### API Response Example
```json
{
    "user_id": 1,
    "link": "http://127.0.0.1:8887/socialmedia_frontend/images/profile.png",
    "name": "Spencer Lyons",
    "theme": "Dark"
}
```

### Postman API Request & RESTful Response
**GET Request:** `http://127.0.0.1:8887/api/user_profile?user_id=1`
**Response:**
```json
{
    "user_id": 1,
    "link": "/images/profile.png",
    "name": "Spencer Lyons",
    "theme": "Dark"
}
```

## Database Queries & Data Manipulation
### Extracting Data from Database
```python
profile = UserProfile.query.filter_by(user_id=user_id).first()
```
- This query retrieves a specific user's profile from the database.

### Working with Lists & Dictionaries
- **List:** Fetching all users from the database.
```python
profiles = UserProfile.query.all()
```
- **Dictionary:** Formatting response data.
```python
return jsonify([profile.read() for profile in profiles])
```

## Class Methods for CRUD Operations
### Create
```python
def post(self):
    data = request.get_json()
    profile = UserProfile(
        user_id=data['user_id'],
        link=data.get('link', 'default_link'),
        name=data.get('name', 'Default User'),
        theme=data.get('theme', 'light')
    )
    profile.create()
    return jsonify(profile.read())
```

### Read
```python
def get(self):
    user_id = request.args.get('user_id')
    profile = UserProfile.query.filter_by(user_id=user_id).first()
    return jsonify(profile.read())
```

### Update
```python
def put(self):
    data = request.get_json()
    profile = UserProfile.query.filter_by(user_id=data['user_id']).first()
    profile.update(data)
    return jsonify(profile.read())
```

### Delete
```python
def delete(self):
    data = request.get_json()
    profile = UserProfile.query.filter_by(user_id=data['user_id']).first()
    profile.delete()
    return {"message": "User profile deleted successfully"}
```

## API Calls & Responses
### Fetch API Call (Frontend to Backend)
```javascript
async function deleteProfile() {
    const confirmation = confirm('Are you sure you want to delete this profile?');
    if (!confirmation) return;
    try {
        const response = await fetch(`${apiUrl}`, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId })
        });
        if (response.ok) {
            alert('Profile deleted successfully!');
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.message}`);
        }
    } catch (error) {
        console.error('Error deleting profile:', error);
    }
}
```

## Handling Different Responses
### Normal Case
- **Input:** Valid user ID
- **Response:** Profile deleted successfully
```json
{"message": "User profile deleted successfully"}
```

### Error Case
- **Input:** Non-existent user ID
- **Response:** Profile not found
```json
{"message": "User profile not found"}
```

## Conclusion
This review highlights the frontend-backend integration for user profile management, including API requests, database interactions, and error handling. It demonstrates the collaborative and structured approach in software development, addressing CRUD operations and optimizing user experience through API-driven solutions.