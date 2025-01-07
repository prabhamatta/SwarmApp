# SwarmApp
### OpenAI Swarm github https://github.com/openai/swarm

## Installation of Homebrew and Python 3.10 and Swarm(yes, OpenAI Swarm needs python 3.10)
### Install Homebrew by running this command in Terminal:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

### After installation, you'll need to add Homebrew to your PATH. Run these two commands:
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

### Verify Homebrew is installed:
brew --version

### Now you can proceed with installing Python 3.10:
brew install python@3.10

### Finally, add Python 3.10 to your PATH:
echo 'export PATH="/opt/homebrew/opt/python@3.10/bin:$PATH"' >> ~/.zprofile
source ~/.zprofile

### Install Git
brew install git

### Now install Swarm (remember to use pip3.10 else you will get version error)
pip3.10 install git+https://github.com/openai/swarm.git
