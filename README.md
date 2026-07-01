# Board Builder

> Define your project once. Build it anywhere.

Board Builder is an Infrastructure-as-Code tool for project management platforms.

Instead of manually creating boards, lists, cards, labels, and descriptions, you define your project as a JSON template and let Board Builder provision it automatically.

Today Board Builder supports Trello, with additional providers planned for the future.

---

# Features

- Create Trello boards
- Reuse existing boards
- Create lists
- Reuse existing lists
- Create cards
- Reuse existing cards
- Support card descriptions
- JSON project templates
- Idempotent builds (safe to run multiple times)

---

# Installation

Clone the repository.

```bash
git clone https://github.com/ertztech/board-builder.git

cd board-builder
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Configuration

Create a `.env` file.

```text
TRELLO_API_KEY=YOUR_API_KEY
TRELLO_TOKEN=YOUR_TOKEN
```

An example file is included as `.env.example`.

---

# Usage

Run the builder with a template.

```bash
python board_builder.py templates/after_the_amen.json
```

---

# Example Template

```json
{
  "board": "After the Amen",
  "lists": [
    {
      "name": "📋 Product Backlog",
      "cards": [
        {
          "name": "Project Vision",
          "description": "Describe the long-term vision."
        }
      ]
    }
  ]
}
```

---

# Project Vision

Board Builder treats project management like Infrastructure as Code.

Instead of manually building boards, you define them in code.

The template becomes the source of truth.

Future providers may include:

- GitHub Projects
- Jira
- Azure DevOps
- Notion

---

# Roadmap

- Labels
- Checklists
- Due dates
- Members
- Sync mode
- Interactive CLI
- AI-generated templates
- Multiple providers

---

# Contributing

Issues and pull requests are welcome.

Please create an issue before beginning major changes.

---

# License

MIT