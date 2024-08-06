## About
This action is creates a new repository in the specified organization on GitHub.

<br>

### Authentication

The authenticated user must be a member of the organization.
Allow PAT tokens or GitHub App with JWT. To generate a GitHub JWT see [here](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-json-web-token-jwt-for-a-github-app).

Authentication with username and password is not supported.
---
## Implementation
This action can be used to create GitHub repository.

Example:

```
stk run action stackspot-actions/github-simple-create-repository --org orgname --token ***** --name repo_name  --non-interactive
```
---
## Release notes
- First version create a GitHub repository
---
## Usage
This action can be used to create GitHub repository.

Example:

```
stk run action stackspot-actions/github-simple-create-repository --org orgname --token ***** --name repo_name  --non-interactive
```