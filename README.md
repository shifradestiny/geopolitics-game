# Geopolitics Game

A fullstack web based application that uses dynamic database management, business logic, and session security for the UCT Bcom Hons Information Systems Entrance Exam.

## Table of Contents

- [Live Application](#live-application)
- [Core Mechanics and Implemented Rules](#core-mechanics-and-implemented-rules)
- [Marker Authentication Details](#marker-authentication-details)
- [Technology Stack](#technology-stack)
- [Contact](#contact)

## Live Application

**The game can be played here:**

## Core Mechanics and Implemented Rules

Web-based territory control game.

1. **Garrison Rule:** Attackers leave exactly 1 troop behind in their home territory after a successful capture.
2. **Combat Ties:** Dice roll ries result end up in 0 losses for both the attacker and defender.
3. **Capture Bonus:** After successfully capturing a territory, the attacker receives a reinforcement bonus of the defenders base value divided by 2 (with a minimum of 2).
4. **Turn Reinforcements:** At the beginning of every turn, players and NPC's get 2 extra soldiers for each territory they control at the time.
5. **Anti-Soft-Lock:** The starting player receives a commanders bonus ensuring a minimum of 3 starting soldiers to ensure an actionable first turn.
6. **Visual Combat Telemetary:** Battles are visually rendered through generated DOM elements and CSS animations.

## Marker Authentication Details

You may use the following details to access the game board and test the game logic:

- **Username:** uctmarker
- **Password:** 12345

You may use the following details to access the `geopolitics_db` database:

- **Username:** game-admin
- **Password:** 24680

## Technology Stack

- **Backend:** Flask, Python
- **Database:** MongoDB Atlas (PyMongo)
- **Frontend:** HTML, CSS, JavaScript
- **APIs:** Gemini 1.5 Flash

## Contact

**Applicant Name:** Shifra Destiny Ssebuliba
**UCT Application Number:** SSBSHI001
**Email:** [destinyssebuliba@gmail.com](destinyssebuliba@gmail.com)
**LinkedIn Profile:** [https://www.linkedin.com/in/shifra-destiny-ssebuliba/](https://www.linkedin.com/in/shifra-destiny-ssebuliba/)

Last Updated: 6 November 2026
