job_menu = {
    "callback_id": "job_post",
    "title": "Post a job",
    "submit_label": "Submit",
    "notify_on_cancel": "true",
    "elements": [
        {
            "type": "text",
            "label": "Company city",
            "name": "city",
            "placeholder": "Dublin",
            "hint": "The location if possible, if its remote, pop that in"
        },
        {
            "type": "text",
            "label": "Job Title",
            "name": "job_title",
            "placeholder": "Ember Developer",
            "hint": "Please put in the job title"
        },
        {
            "type": "text",
            "label": "Salary Range",
            "name": "salary",
            "placeholder": "€80K",
            "hint": "Please provide a salary.",
            "optional": "true"
        },
        {
            "label": "Type of job",
            "type": "select",
            "name": "contract_type",
            "hint": "What type of Role?",
            "options": [
                    {
                        "label": "Temporary",
                        "value": "Temporary"
                    },
                {
                        "label": "Permanent",
                        "value": "Permanent"
                    },
                {
                        "label": "Contract",
                        "value": "Contract"
                    },
                {
                        "label": "Other",
                        "value": "Other (explained below)"
                    }
            ]
        },
        {
            "label": "Additional information",
            "name": "info",
            "type": "textarea",
            "placeholder": "Hey, have a Senior engineering role with another start-up in Dublin. They are looking for a...",
            "hint": "Provide additional information if needed."
        }

    ]
}
