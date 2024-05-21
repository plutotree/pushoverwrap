pushoverwrap is a simple [Pushover](https://pushover.net) API wrapper.

# Installation

Install pushoverwrap using pip

```bash
pip install pushoverwrap
```

## Usage

The most simple example:

```python

from pushoverwrap import Pushover

push = Pushover(
    app_token='APP_TOKEN',
    user_token='USER_TOKEN',
)

push.send_msg('message content')

```

A more complex example, with title and image

```python
push.send_msg('message content',
    title='message title',
    image='local/path/image.jpeg'
)

```
