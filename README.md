# Kyyti

Transportation app for Levi

## Tech Stack

- **Laravel 12** - PHP web application framework
- **InertiaJS** - Modern monolith architecture
- **Vue 3** - Progressive JavaScript framework
- **Laravel Sail** - Docker development environment
- **Laravel Sanctum** - API authentication
- **MariaDB 11** - Database (latest LTS release)
- **Tailwind CSS** - Utility-first CSS framework
- **Vite** - Frontend build tool

## Features

- Modern web interface using Vue 3 and InertiaJS
- RESTful API for mobile applications
- User authentication and management via Laravel Sanctum
- Docker-based development environment with Laravel Sail
- MariaDB database

## Requirements

- Docker and Docker Compose
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jluopajarvi/kyyti.git
cd kyyti
```

2. Copy the environment file:
```bash
cp .env.example .env
```

3. Start the Docker environment:
```bash
./vendor/bin/sail up -d
```

4. Install PHP dependencies:
```bash
./vendor/bin/sail composer install
```

5. Generate application key:
```bash
./vendor/bin/sail artisan key:generate
```

6. Run database migrations:
```bash
./vendor/bin/sail artisan migrate
```

7. Install and build frontend assets:
```bash
./vendor/bin/sail npm install
./vendor/bin/sail npm run dev
```

8. Access the application at: http://localhost

## Development

### Using Sail

Laravel Sail is a light-weight command-line interface for interacting with Laravel's Docker development environment. You can use Sail commands with:

```bash
./vendor/bin/sail [command]
```

For convenience, you can create an alias:
```bash
alias sail='./vendor/bin/sail'
```

### Running Tests

```bash
./vendor/bin/sail artisan test
```

### Building for Production

```bash
./vendor/bin/sail npm run build
```

## API Authentication

The application uses Laravel Sanctum for API authentication. API routes are defined in `routes/api.php` and are prefixed with `/api`.

### Example API Request

To access protected API endpoints, include the Sanctum token in the Authorization header:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN_HERE" http://localhost/api/user
```

## Project Structure

- `app/` - Application core (Models, Controllers, etc.)
- `resources/js/Pages/` - Vue 3 components (Inertia pages)
- `resources/views/` - Blade templates
- `routes/web.php` - Web routes (Inertia)
- `routes/api.php` - API routes (Sanctum protected)
- `database/` - Migrations and seeders

## License

The Laravel framework is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
