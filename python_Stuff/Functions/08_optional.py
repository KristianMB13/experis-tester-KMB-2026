def send_email(subject, body, to, cc = None):
    if cc is not None:
        print(f"Sending email to {to} with CC: {cc}")
    else:
        print(f"Sending email to {to} without CC")

send_email("Meeting reminder", "Don't forget about the meeting tomorrow", "john@company.com", "boss@company.com")




print([1, 2, 3], [4, 5, 6], sep = " | ")