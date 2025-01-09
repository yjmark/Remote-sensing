# Setup Guide

## Prerequisites

### Required Software

For this class, you will need [Python](https://www.python.org/downloads/), [VSCode](https://code.visualstudio.com/download), [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [Pyenv](https://github.com/pyenv/pyenv), [Pipenv](https://pipenv.pypa.io/en/latest/installation.html), and thte [Google Cloud CLI](https://cloud.google.com/sdk/docs/install). Prior to proceeding to the setup instructions, make sure you have all of these installed for your OS (see the hyperlinks to the setup instructions).

### Google Cloud Account

We will use Google Earth Engine at different points in this course. In order to do so, please [follow these instructions](https://towardsai.net/p/machine-learning/how-to-set-up-a-google-earth-engine-cloud-project) to make sure you have a Google Cloud account set up for use with Google Earth Engine.

## Setup Instructions

Once you have installed the required software and set up your Google Cloud account, open a git terminal and clone this repository in your desired location:

```
git clone https://github.com/nlebovits/musa-650-spring-2025.git
```

Once the repo is cloned, navigate to the root directory, install Python 3.11, install dependencies, and activate the virtual environment:

```
pyenv install 3.11
pyenv local 3.11
pipenv install
pipenv shell
```

Finally, using the Google Cloud CLI, run `earthengine authenticate` in your terminal to set up Google Earth Engine access (see these instructions for more information). _It is likely that you will run into issues here; please troubleshoot as a class in person or on the discussion board on GitHub so we can solve problems collectively._

Congrats! You're ready to go. :)
