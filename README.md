# SkillDonate

SkillDonate is an innovative web platform designed to connect skilled volunteers with charitable organizations seeking their expertise. Our primary goal is to create a user-friendly and intuitive platform that empowers volunteers to donate their time and skills to support charitable causes. SkillDonate enables volunteers to showcase the skills they are willing to contribute and browse skill requests posted by organizations. Likewise, charitable organizations can post their specific skill requirements and explore the skills offered by volunteers. This two-way interaction fosters seamless communication and collaboration, allowing volunteers and organizations to express interest and connect directly on the platform. SkillDonate aims to bridge the gap between skilled individuals passionate about giving back and organizations in need, fostering a culture of generosity and facilitating meaningful contributions.

## Features

- **Volunteer Profiles**: Volunteers can create profiles showcasing their skills, availability, and preferred causes. This allows them to present their expertise and attract organizations seeking specific skills.

- **Charity Profiles**: Volunteers can create profiles showcasing their skills, availability, and preferred causes. This allows them to present their expertise and attract organizations seeking specific skills.

- **Skill Requests**: Charitable organizations can post skill requests, specifying the skills they require and the duration of assistance needed. This helps volunteers find opportunities aligned with their expertise and availability.

- **Skill Donations**: Volunteers can post skill donations, specifying the skills they are offering up for donation. This helps charity organisations seek out the skills they are looking for.

- **Show Interest in skills Posted**: SkillDonate provides a system where volunteers can show interest in skills posted as required by charity organisations signifying that they are willing to offer up the skill that is being sought. Likewise charity organisations can also show interest in skills offered by volunteers on the platform, signifying to the volunteer that they are interested in the skill being donated.

- **Contact Us**: The platform facilitates direct communication to the administartors of the website through a contact us page.


## Installation

To run SkillDonate locally, follow these steps:

1. Clone the SkillDonate repository:
   ```bash
   git clone https://github.com/umlamulankunzi/skill-donate-website.git
   ```

2. Navigate to the project directory:
   ```bash
   cd skilldonate
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - For Windows:
     ```cmd
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Set up the database and migrate models:
   ```bash
   python manage.py migrate
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

8. Access SkillDonate in your web browser at `http://localhost:8000`.

## Author

- [@Prince D Jele](https://www.github.com/umlamulankunzi)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEV_ENV`  
`ENV`  
`SECRET_KEY`  
`MYSQL_DATABASE`  
`MYSQLUSER`  
`MYSQL_ROOT_PASSWORD`  
`MYSQLHOST`  
`MYSQLPORT`  
`EMAIL_HOST`  
`EMAIL_PORT`  
`EMAIL_HOST_USER`  
`EMAIL_HOST_PASSWORD`  

## Contributing

We welcome contributions to enhance SkillDonate and make it even more impactful. To contribute, please follow these steps:

1. Fork the SkillDonate repository.

2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your modifications and commit your changes:
   ```bash
   git commit -m "Add your commit message"
   ```

4. Push your branch to your forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request against the main repository's `develop` branch.

## License

SkillDonate is released under the [Apache License](LICENSE).

## Acknowledgements

We would like to express my gratitude to my peers in Alx-cohort-13 who helped helped me shape SkillDonate into what it is.


# Let's make a difference together with SkillDonate!
