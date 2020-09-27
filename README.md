# git_contributing
The goal of this project is to make project search and filtering on Github more accessible, thereby enabling users to find projects they can make valuable contributions to.

## Setup

First, set up an auth token with Github, copy it and pass it as an argument to --token in the api_creds_setup.py script. 
This stores an encrypted version of the token along with the key in the environment you store the script in via environment variables

Navigate to the project root folder via cli and run the following:
```bash
python api_creds_setup.py --token <your_github_token>
```

Next, source changes in your respective environment config file

If bashrc then: 
```bash
source ~/.bashrc
```
If zshrc then: 
```zsh
source ~/.zshrc
```

Finally, verify the creation of environment variables GH_KEY and GH_TOKEN with the following line:
```bash
echo $GH_KEY '\n' $GH_TOKEN
```
You should see an output of two encrypted credentials after running this