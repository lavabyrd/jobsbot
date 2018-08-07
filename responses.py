attachm = [
    {
        "callback_id": "confirm_post",
        "fallback": "New job posting",
        "title": "Your job post",
        "color": "#7CD197",
        "actions": [
            {
                "type": "button",
                "text": "Post It!!",
                "name": "PostJob",
                "style": "primary"
            },
            {
                "type": "button",
                "text": "I've changed my mind!",
                "name": "cancelled_job",
                "style": "danger"
            }
        ]
    }
]

attachm_update = [
    {
        "callback_id": "confirmed",
        "fallback": "Posted",
        "title": "Done",
        "text": "job posted",
        "color": "#7CD197",
    }
]


def make_response(jtype, location, job_title, salary, message, contact):
    salary = salary or 'Salary not supplied' 
    return f"*[{jtype}] [{location}] [{job_title}] [{salary}]* {message}. Contact <@{contact}> for information!"
