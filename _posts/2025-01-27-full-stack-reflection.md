---
toc: true
comments: true
layout: post
title: Ful Stack API Reflection
---

# Collaborating on a Full Stack User Profile Feature

## Introduction

In this blog, we will review the design and implementation of a full-stack feature for managing user profiles. The program aligns with the Create performance task, focusing on solving problems, enabling innovation, and exploring personal interests.

## Purpose of the Program

The purpose of our my api is to provide a robust system for managing user profiles on our website. This feature enables users to create, read, update, and delete their profiles, creating a personalized and engaging user experience.

### Purpose of My Feature

My contribution focuses on implementing the backend API for user profile management and connecting it to a dynamic frontend. This includes creating CRUD operations in the API, ensuring secure data handling, and building an interactive user interface for seamless interactions.

---

## Input/Output Demonstrations

### Using the Frontend

The frontend connects to the backend API to fetch, display, and manage user profiles dynamically. Below is a demonstration:

```html
<script>
    const apiUrl = 'http://127.0.0.1:8887/api/user_profile';

    async function loadProfile() {
        try {
            const response = await fetch(`${apiUrl}`);
            const data = await response.json();

            document.getElementById('link').src = data.profilePicture || '/images/logo.png';
            document.getElementById('name').textContent = data.username || 'Unknown User';
            document.getElementById('theme').textContent = `Preferred Theme: ${data.theme || 'Light'}`;
        } catch (error) {
            console.error('Error fetching profile data:', error);
        }
    }

    document.addEventListener('DOMContentLoaded', loadProfile);
</script>
```

### Using Postman

#### Raw API Request and Response

**POST Request**:
```json
{
    "user_id": 1,
    "link": "/images/custom_profile.png",
    "name": "John Doe",
    "theme": "dark"
}
```
**Response**:
```json
{
    "profile_id": 10,
    "user_id": 1,
    "link": "/images/custom_profile.png",
    "name": "John Doe",
    "theme": "dark"
}
```

### Database Management

Using `db_init`, `db_restore`, and `db_backup`, we can create, restore, and backup database data. Example:

```python
# Initializing sample data
initUserProfile()
```

---

## Working with Lists, Dictionaries, and Databases

### Lists and Dictionaries

In the API, database queries return lists of rows, where each row is represented as a dictionary:

```python
profiles = UserProfile.query.all()
return jsonify([profile.read() for profile in profiles])
```

### Formatting API Response Data

The `read()` method in the `UserProfile` model formats database rows into JSON:

```python
return {
    "profile_id": self.profile_id,
    "user_id": self.user_id,
    "link": self.link,
    "name": self.name,
    "theme": self.theme
}
```

### Database Queries

Queries like `filter_by` extract rows:

```python
profile = UserProfile.query.filter_by(user_id=data['user_id']).first()
```
These queries are powered by SQLAlchemy, a third-party ORM library.

---

## Algorithmic Code

### API Class

The `UserProfileAPI._CRUD` class handles GET, POST, PUT, and DELETE methods:

```python
class _CRUD(Resource):
    @token_required()
    def post(self):
        data = request.get_json()
        profile = UserProfile(
            user_id=data['user_id'],
            link=data.get('link', '/images/logo.png'),
            name=data.get('name', 'toby'),
            theme=data.get('theme', 'light')
        )
        profile.create()
        return jsonify(profile.read())
```

### Method with Sequencing, Selection, and Iteration

The `update` method in the `UserProfile` class combines these elements:

```python
def update(self, data):
    self.link = data.get('link', self.link)
    self.name = data.get('name', self.name)
    self.theme = data.get('theme', self.theme)
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        logging.warning(f"Error updating profile for user '{self.user_id}': {str(e)}")
```

---

## Calling Algorithms

### Fetching Data from the API

The frontend uses `fetch` to call the API:

```javascript
const response = await fetch(`${apiUrl}`);
const data = await response.json();
```

### Handling Responses

Response data is processed dynamically in the DOM:

```javascript
document.getElementById('name').textContent = data.username || 'Unknown User';
```

### Error Handling and Different Conditions

Errors are logged and displayed:

```python
if not profile:
    return {"message": "User profile not found"}, 404
```

---

## Conclusion

This full-stack user profile feature demonstrates the power of collaboration and innovation in programming. From API development to frontend integration, each component plays a vital role in delivering a seamless user experience. Feedback is welcome as we continue to refine and enhance this feature.
