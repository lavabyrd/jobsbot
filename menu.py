job_menu = {
    "callback_id": "job-post",
    "title": "Post a job",
    "submit_label": "Post a Job",
    "notify_on_cancel": "true",
    "elements": [
        {
            "type": "text",
            "label": "Company Name",
            "name": "comp"
        },
        {
            "type": "text",
            "label": "Company city",
            "name": "city"
        },
        {
            "label": "Type of job",
            "type": "select",
            "name": "contract_type",
            "options": [
                    {
                        "label": "Temp",
                        "value": "temp"
                    },
                {
                        "label": "Permanent",
                        "value": "perm"
                    },
                {
                        "label": "Contract",
                        "value": "contract"
                    }
            ]
        },
        {
            "label": "url",
            "name": "website",
            "type": "text",
            "subtype": "url",
            "placeholder": "https://mycompany.com/careers"
        },
        {
            "label": "Additional information",
            "name": "info",
            "type": "textarea",
            "hint": "Provide additional information if needed."
        }

    ]
}
