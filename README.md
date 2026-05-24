<br />
<div align="center">
  <a href="https://github.com/ScottyLabs/chihuahua">
    <img src="https://static.wikia.nocookie.net/legallyblonde/images/2/23/Bruiser.jpg/revision/latest?cb=20201203022622" alt="Bruiser Woods" width="80" height="80">
  </a>

  <h3 align="center">Chihuahua</h3>

  <p align="center">
    A simple and powerful application for managing the legal documents required for prize distribution.
  </p>
</div>


## About The Project
ScottyLabs events bring hundreds or thousands of amazing people from all over to compete at various hackathons and other competitions.
We give out over 50 cash prizes in the course of a year to winners—the very best at those competitions.

Unfortunately, giving out cash means doing *taxes* 😔.
Winners have to fill out a bunch of forms, or maybe just one, with tons of repeated information across them.
It's slow, tedious, and error-prone, and a big reason why prize distribution takes so long for many of our hackathons.

This project sets out to speed up the process by providing a simple, straightforward way for participants to enter their details,
generate the necessary documents, and securely send them to the school financial office for processing. 

If you want to dig more into what this means, read [FLOW.md](/FLOW.md).

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [FastHTML](https://fastht.ml)
* Google [Drive](https://developers.google.com/workspace/drive/api/) and [Sheets](https://developers.google.com/workspace/drive/api/) APIs
* [Mailgun](https://www.mailgun.com)

## Getting Started

These are instructions for testing the project locally.

### Prerequisites
Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/).

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ScottyLabs/chihuahua.git
   ```
2. Run the project in debug mode
   ```sh
   uv run main.py --debug
   ```

## Usage
In production, the service should be able to run simply by providing relevant environment variables and running the main script.

Admins can upload lists of users.

## Contributing
To understand the objectives of the project, a good place to start is probably reading [FLOW.md](/FLOW.md).

This project will likely be mainly contributed to by ScottyLabs members
who will have access to the documents and communications with the finance office that will inform this project.
Outside contributors may, however, be accepted. Open an issue or make a pull request to get started.

This project will use [gitmoji](https://gitmoji.dev) for commit management.
It will represent emojis with Unicode, not shortcodes (e.g. `🐛`, not `:bug:`).
The reasoning for this is because it looks nice, and it's more fun this way.
If you have complaints, complain to Evan. But he'll probably be too busy laughing with glee to hear your disagreement.

## License
This project is licensed under the [MIT License](/LICENSE.md).

## Contact
If you're interested in contributing or using this for your own purposes, reach out to us at [hello@scottylabs.org](mailto:hello@scottylabs.org) to chat.

## Acknowledgments
