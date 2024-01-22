from django.core.mail import EmailMessage


def send_email(first_name, last_name, email, date, occupation):
    message_body = f"""
    Your job application was submitted. Thank you, {first_name}.
    
    Your data:
    Name: {first_name} {last_name}
    Occupation: {occupation}
    Possible start date: {date}
    
    We will contact you as soon as possible.
    """
    EmailMessage("Application submition confirmation", message_body, to=[email]).send()
