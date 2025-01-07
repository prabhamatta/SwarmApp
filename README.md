# SwarmApp

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
