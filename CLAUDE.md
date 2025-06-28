# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Structure

This repository contains multiple Flask application samples organized by date:

- `20250426/` - TODO application with LocalStorage and time display features
- `20250517/` - Multi-page Flask application with navigation  
- `20250531/` - Message box application demonstrating GET/POST methods
- `project/` - Time zone comparison application

Each directory is a self-contained Flask application with its own `app.py`, templates, and static files.

## Common Development Commands

### Setup and Installation
```bash
# Navigate to specific project directory first
cd 20250426  # or 20250517, 20250531, project

# Install dependencies
pip install -r requirements.txt
# For projects without requirements.txt:
pip install flask pytz
```

### Running Applications
```bash
# Run Flask application (from within project directory)
python app.py

# Applications typically run on:
# - http://127.0.0.1:5000 (default)
# - http://127.0.0.1:5001 (20250531 project)
```

### Testing Applications
No automated test frameworks are configured. Testing is done manually by:
1. Starting the Flask application
2. Accessing endpoints in browser
3. Verifying functionality matches README descriptions

## Application Architecture

### Common Flask Patterns
- All applications use Flask with Jinja2 templating
- Static files in `static/` directories (CSS)
- HTML templates in `templates/` directories
- Simple route-based architecture without blueprints
- Most applications run in debug mode (`app.run(debug=True)`)

### Data Persistence Patterns
- **20250426**: Client-side LocalStorage (JavaScript)
- **20250517**: Static sample data in Python dictionaries
- **20250531**: JSON file storage (`data/messages.json`)
- **project**: No data persistence (dynamic time display)

### Time Zone Handling
Projects using time zones (`20250517`, `project`) use the `pytz` library:
- Japan: `pytz.timezone('Asia/Tokyo')`
- US: `pytz.timezone('US/Central')`
- China: `pytz.timezone('Asia/Shanghai')`

## Key Features by Project

### 20250426 (TODO App)
- Routes: `/` (main TODO), `/todo2` (time-based TODO), `/time` (clock display)
- Frontend: JavaScript DOM manipulation with LocalStorage
- No backend data persistence

### 20250517 (Navigation Demo)
- Routes: `/` (top page with time), `/memo` (sample memos), `/profile` (sample profile)
- Server-side time rendering with pytz
- Static sample data

### 20250531 (Message Box)
- Routes: `/` (home), `/post_message` (POST), `/explanation`, `/data_view`, `/search`
- Demonstrates GET vs POST methods
- JSON file-based data persistence
- Flash messaging system

### project (Time Zones)
- Routes: `/` (Japan time), `/us`, `/ch`, `/diff` (comparison view)
- Real-time timezone conversion
- Template reuse with different data

## Development Notes

- No linting, formatting, or type checking configured
- All applications are educational/demonstration purposes
- Japanese language used in comments and UI text
- No authentication or security considerations implemented
- Direct file system access for data storage (20250531)