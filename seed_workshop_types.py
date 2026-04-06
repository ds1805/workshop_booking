"""
Run this once to populate WorkshopType data so the booking dropdown works.

Usage:
    python manage.py shell < seed_workshop_types.py

Or paste it directly into:
    python manage.py shell
"""

from workshop_app.models import WorkshopType

types = [
    {
        'name': 'Basics of Python',
        'description': 'A beginner-friendly workshop covering Python fundamentals including data types, control flow, functions, and file handling.',
        'duration': 2,
        'terms_and_conditions': 'Participants must bring their own laptops. Minimum 30 participants required.',
    },
    {
        'name': 'Scientific Python (SciPy)',
        'description': 'An intermediate workshop on scientific computing with Python using NumPy, SciPy, and Matplotlib.',
        'duration': 2,
        'terms_and_conditions': 'Basic Python knowledge required. Participants must bring their own laptops.',
    },
    {
        'name': 'NumPy and Data Analysis',
        'description': 'Workshop covering NumPy arrays, data manipulation, and introductory data analysis techniques.',
        'duration': 1,
        'terms_and_conditions': 'Basic Python knowledge required.',
    },
    {
        'name': 'Django Web Framework',
        'description': 'Hands-on workshop on building web applications with Django, covering models, views, templates, and REST APIs.',
        'duration': 3,
        'terms_and_conditions': 'Intermediate Python knowledge required. Participants must bring their own laptops.',
    },
    {
        'name': 'ISCP (Introduction to Scientific Computing with Python)',
        'description': 'A comprehensive workshop introducing scientific computing concepts using Python tools.',
        'duration': 2,
        'terms_and_conditions': 'No prior Python knowledge required.',
    },
]

created = 0
for t in types:
    obj, was_created = WorkshopType.objects.get_or_create(
        name=t['name'],
        defaults={
            'description':          t['description'],
            'duration':             t['duration'],
            'terms_and_conditions': t['terms_and_conditions'],
        }
    )
    if was_created:
        created += 1
        print(f"Created: {obj.name}")
    else:
        print(f"Already exists: {obj.name}")

print(f"\nDone. {created} new workshop type(s) added.")