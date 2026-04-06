# **Workshop Booking**

> This website is for coordinators to book a workshop(s), they can book a workshop based on instructors posts or can propose a workshop date based on their convenience.


### Features
* Statistics
    1. Instructors Only
        * Monthly Workshop Count
        * Instructor/Coordinator Profile stats
        * Upcoming Workshops
        * View/Post comments on Coordinator's Profile
    2. Open to All
        * Workshops taken over Map of India
        * Pie chart based on Total Workshops taken to Type of Workshops.


* Workshop Related Features
    > Instructors can Accept, Reject or Delete workshops based on their preference, also they can postpone a workshop based on coordinators request.

__NOTE__: Check docs/Getting_Started.md for more info.

<img width="1919" height="960" alt="Screenshot 2026-04-06 142228" src="https://github.com/user-attachments/assets/c721c4bc-022f-42ba-8bad-c4bf354de01b" />

<img width="1919" height="1079" alt="Screenshot 2026-04-06 142041" src="https://github.com/user-attachments/assets/4e3eebe2-7503-4aa2-818a-1684222413fc" />
<img width="1919" height="911" alt="Screenshot 2026-04-06 142049" src="https://github.com/user-attachments/assets/95d0c2c5-316c-4c9a-b0f9-3a33d50d39df" />
<img width="1919" height="910" alt="Screenshot 2026-04-06 142100" src="https://github.com/user-attachments/assets/8431845f-4e9d-4edb-b1f8-2dfe722e9fb8" />
<img width="1919" height="947" alt="Screenshot 2026-04-06 142108" src="https://github.com/user-attachments/assets/58f16209-f36d-49ed-a244-66f254c888fb" />
<img width="1919" height="916" alt="Screenshot 2026-04-06 142120" src="https://github.com/user-attachments/assets/e870747b-5fdc-46ed-a5ae-4fb49a895162" />
<img width="1919" height="884" alt="Screenshot 2026-04-06 142126" src="https://github.com/user-attachments/assets/f3fb901b-3130-4386-80bd-b0c7e19ff47b" />
<img width="1919" height="886" alt="Screenshot 2026-04-06 142159" src="https://github.com/user-attachments/assets/052f61ae-0b32-418d-baca-06bc058858ee" />
<img width="1919" height="886" alt="Screenshot 2026-04-06 142216" src="https://github.com/user-attachments/assets/8fe09363-b62c-49b8-bd3c-9b6281c25231" />

Reasoning
What design principles guided your improvements?
The core principle was visual hierarchy with purpose — every screen should answer one question for the user instantly. On the Home page, the hero section answers "what is this?" before anything else. The workshop cards below answer "what can I book?" with the most important info (name, date, duration, description) in a consistent, scannable layout. On the Dashboard, the three stat cards (Total Bookings / Upcoming / Completed) answer "what's my status?" at a glance before the user even reads the table.
A second principle was dark theme with intentional contrast. I chose a dark background (#0d0f1a range) not just for aesthetics but because FOSSEE's audience — students — often works late. White cards on a dark surface create natural separation without needing heavy borders. Status badges (yellow "Pending") pop immediately against both dark and white backgrounds.
Third, consistency as trust. Every page uses the same navbar, the same card shape, the same button style (dark filled for primary actions, outlined for secondary), and the same footer. When every page feels like the same product, users feel confident navigating it.

How did you ensure responsiveness across devices?
The layout was built mobile-first, meaning the base CSS targets small screens and larger sizes are layered on top:

Workshop cards use CSS Grid with auto-fill and minmax(280px, 1fr) so they naturally reflow from 1 column on mobile to 3 on desktop without media query breakdowns.
The navbar was kept minimal and horizontal — the links collapse cleanly on narrow screens without requiring a hamburger menu, keeping navigation one tap away at all times.
Forms (booking, login) are centered cards with max-width constraints and width: 100% inputs, so they feel comfortable on a 375px phone and don't stretch awkwardly on a 1440px monitor.
The dashboard stat cards use the same grid approach — side by side on desktop, stacked on mobile.
The profile page uses a simple single-column card layout that works identically at every width.
Touch targets throughout are at minimum 44px tall, per Apple and Google accessibility guidelines.


What trade-offs did you make between design and performance?
Dark background vs. image-based hero: I deliberately avoided a background image or gradient illustration in the hero section. An image would have added visual richness but increased page load time and would have required careful lazy-loading. The solid dark background with large bold text achieves the same emotional impact in zero extra bytes.
Client-side search vs. server-side filtering: The workshop search bar filters results entirely on the frontend without an API call. This means all workshops load upfront, which is a trade-off — but at the current data scale (5–10 workshops), it delivers instant, zero-latency search that feels far more responsive than a round-trip to the Django backend.
No animation library: I avoided Framer Motion or similar libraries. Micro-interactions (button hover, card hover elevation) are handled with plain CSS transition on transform and opacity only — these are GPU-composited properties that don't trigger layout recalculation, keeping interactions smooth even on low-end Android devices.
Statistics page with placeholder cards: Rather than building full charts (which would require Chart.js or Recharts adding ~150KB to the bundle), I built the stats page with clear category cards (Workshop Stats, Profile Stats, Team Stats, Public Stats) that describe what each section contains. This keeps the bundle lean while preserving the information architecture for when a charting library is justified.

What was the most challenging part of the task and how did you approach it?
The most challenging part was connecting the React frontend to the Django REST backend in a way that felt seamless — specifically around authentication state flowing through the app. The profile page needs to show the logged-in user's name, role (coordinator), and their booking history, all pulled from the Django API. The dashboard needs real booking counts. Managing this shared auth state (JWT token, user object) across pages — Navbar, Profile, Dashboard — without a heavy state library was the core problem.
My approach was to use React's Context API to hold the auth state globally, so any component (Navbar for the Login button, Profile for user data, Dashboard for booking counts) could read from the same source without prop drilling. On login, the token is stored and the user object is fetched once and cached in context, so subsequent page navigations don't re-fetch unnecessarily.
The second challenge was making the Django backend's existing API responses map cleanly to the new UI. The original endpoints returned data in formats tied to the old Django template structure. I wrote a thin adapter layer in the React services to transform API responses into the shape the components expected, keeping the components clean and the API integration isolated to one place.ShareContentPython Screening Task_ UI_UX Enhancement.docxdocxScreenshots.zipzip
