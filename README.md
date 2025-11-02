# kyyti
Transportation app for Levi

A Django-based application for managing VIP rides in sports events.

## Features

- **Multi-organizer Support**: Multiple event organizers can use the application
- **Organizer Model**: Each organizer has name, contact details, address, and description
- **User Roles**: Users can be assigned roles (admin, manager, staff, viewer) for specific organizers
- **Customer Management**: Customers are mapped to organizers for ride management

## Models

### Organizer
- `name`: Unique name of the organizer
- `contact_details`: Contact information (phone, email, etc.)
- `address`: Physical address
- `description`: Optional description of the organizer
- `created_at`, `updated_at`: Timestamps

### OrganizerUser
Junction table that maps users to organizers with specific roles:
- `user`: Foreign key to Django's User model
- `organizer`: Foreign key to Organizer
- `role`: One of: admin, manager, staff, viewer
- `created_at`: Timestamp

### Customer
Maps users to organizers as customers:
- `user`: Foreign key to Django's User model
- `organizer`: Foreign key to Organizer
- `notes`: Optional notes about the customer
- `created_at`: Timestamp

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create a superuser:
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

5. Access the admin interface at http://localhost:8000/admin

## Testing

Run tests with:
```bash
python manage.py test
```

