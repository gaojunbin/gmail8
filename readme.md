# GMAIL

## News

### Support mail type

 - [x] Support gmail
- [ ] Support qqmail

### Support mail content

- [x] Support plain
- [x] Support html
- [ ] Support markdown

### Support reminder

- [x] Support custom reminder server (docker)
- [x] Support free reminder server

## What can it do

This is a tool that allows you to easily use mail with the help of python, as well as helping you to monitor your program and alert you with timely emails!

## Installation
```shell
pip install gmail8
```

---

## Getting Started

1. Universal email sending API

```python
gmail(**kwargs_A)(**kwargs_B)
```

### **`kwargs_A` Parameters**:

| Parameter           | Type   | Description                                                  | Default         |
| ------------------- | ------ | ------------------------------------------------------------ | --------------- |
| **`mailtype`**      | string | Email provider, supports `gmail`, `qq`.                      | `gmail`         |
| **`gmail_mail`**    | string | Sender's Gmail address(can be set via the environment variable `gmail_mail`). | None (Required) |
| **`gmail_passkey`** | string | Gmail app password or passkey (can be set via the environment variable `gmail_passkey`). | None (Required) |
| **`qq_mail`**       | string | Not supported yet.                                           | None            |
| **`qq_passkey`**    | string | Not supported yet.                                           | None            |

---

### **`kwargs_B` Parameters**:

| Parameter        | Type   | Description                                         | Default        |
| ---------------- | ------ | --------------------------------------------------- | -------------- |
| **`to`**         | string | Recipient email address.                            | None(Required) |
| **`subject`**    | string | Email subject.                                      | `No subject`   |
| **`message`**    | string | Email content, supports `html` and `markdown`.      | `No message`   |
| **`mode`**       | string | Email format, supports `plain`, `html`, `markdown`. | `plain`        |
| **`attachment`** | string | Path to the file to be attached.                    | None           |
| **`from_who`**   | string | Sender's name.                                      | `from_mail`    |

---

### Example Usage 1:

```python
from gmail8 import gmail
gmail(
    mailtype="gmail",
    gmail_mail="your_email@gmail.com",
    gmail_passkey="your_passkey"
)(
    to="recipient@example.com",
    subject="Test Email",
    message="""<h1>Hello!</h1>""",
    mode="html",
    attachment="path/to/your/file.txt",
    from_who="Your Name"
)
```

This example demonstrates how to send an email with a subject, HTML content, and an attachment using the `gmail` function.

2. Reminder API (Forked from [Oswells/reminder](https://github.com/Oswells/reminder), Thanks Junjie!)

```
reminder(**kwargs)
```

#### Required Parameters for `reminder`

| Parameter | Type  | Description                                |
| --------- | ----- | ------------------------------------------ |
| `url`     | `str` | The URL that will be used by the reminder. |
| `to`      | `str` | Email address to send the reminder to.     |

#### Forbidden Parameters for `reminder`

The following parameters **cannot** be passed into `reminder`:

| Parameter  | Description                           |
| ---------- | ------------------------------------- |
| `FilePath` | Internal file path, cannot be passed. |
| `Error`    | Error handling is managed internally. |
| `CostTime` | Time calculation handled internally.  |
| `Ppid`     | Process-related information.          |

#### Additional Parameters

You can pass any other parameters into `reminder`, and all these parameters will appear in your email.

### Example Usage 2:

```python
from gmail8 import reminder
@reminder(to="your_email@gmail.com", url='https://mail.junbingao.com/reminder')
def train():
    train code

if __name__ == '__main__':
    train()
```

An email will be sent to you when the program runs completes or terminates unexpectedly.  
[Click here for more demos and en example of email you will receive.](./demo/)

#### Details
I offer a free website: https://mail.junbingao.com/reminder. Of course, you can build your own website for personal use with proposed docker-compose file.
The purpose of this decorator is to submit a POST request to the `url` with the data content of {'to':your_email, 'FilePath':os.getcwd(),'Error':error, ...}
