# Bed Bahadur Gurung — Official Portfolio (Frontend)

A modern, responsive Django frontend for an official political/film portfolio
website. This build is **frontend only**: templates, CSS, and JavaScript with
placeholder content. There are no models, no form processing, no database,
and no authentication yet — those are intentionally deferred to a later
stage, per the current project brief.

## Stack

- Django (templates + static files only)
- Bootstrap 5 (via CDN)
- Bootstrap Icons (via CDN)
- Google Fonts: Montserrat (headings) + Poppins (body)
- Vanilla JavaScript (countdown timer, scroll reveal, sticky navbar, back-to-top)

## Project layout

```
bedbahadurgurung/
├── manage.py
├── requirements.txt
├── config/                    # Django project (settings, urls, wsgi/asgi)
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── portfolio/                 # Django app
│   ├── views.py               # All placeholder content lives here
│   ├── urls.py
│   └── templates/portfolio/
│       ├── base.html          # Shared navbar, footer, head/scripts
│       ├── home.html          # Hero + countdown + intro
│       ├── journey.html       # Vertical career timeline
│       ├── film.html          # Movies, upcoming feature, song galleries
│       ├── politics.html      # Positions, ministries, political timeline
│       ├── about.html         # Bio, mission/vision, values, education
│       └── contact.html       # Contact form (frontend only) + info cards
└── static/
    ├── css/style.css          # All design tokens & component styles
    ├── js/
    │   ├── countdown.js       # Term-of-office countdown logic
    │   └── main.js             # Navbar scroll state, reveal animation, back-to-top
    └── images/                 # Placeholder SVGs — swap for real photos/posters
        ├── profile/
        ├── movies/
        ├── songs-written/
        └── songs-performed/
```

## Getting started

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/`.

## Editing content

Almost all editable content (movie titles, descriptions, poster paths, song
titles, timeline entries, ministries, contact details, term dates, etc.)
lives in **`portfolio/views.py`** as plain Python dictionaries and lists —
edit there, not in the templates. Replace the placeholder SVGs in
`static/images/` with real photos and posters (keep the same filenames, or
update the paths in `views.py`).

- **Countdown target date**: `term_end_iso` in `HomeView.get_context_data`
  (update once the exact B.S.→A.D. conversion is confirmed).
- **Movies**: `movies` list and `upcoming_movie` dict in `FilmView`.
- **Songs**: `songs_written` and `songs_performed` lists in `FilmView`.
- **Journey timeline**: `timeline` list in `JourneyView`.
- **Political timeline / ministries**: `PoliticsView`.
- **Bio, values, education, achievements**: `AboutView`.
- **Contact details**: `contact_details` dict in `ContactView`.

## Notes

- The contact form is frontend-only; submitting it shows an inline notice
  and does not send data anywhere. Wiring it up to email/a database is a
  follow-up task, along with any models, admin, or auth.
- All images are placeholder SVGs generated for layout purposes — replace
  them with real assets before launch.
