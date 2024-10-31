# Setup Guide

## Prerequisites

This project relies heavily on Google Earth Engine, so, before anything else, make sure you have a Google Cloud account set up. Once you do, install the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install) and authenticate.

Next, clone this repository:

```
git clone https://github.com/nlebovits/musa-650-spring-2025.git
```

Create a `/credentials` subdirectory in the root of the repository. This will be ignored by Git. Download a service account key associated with the HotspotStoplight project, place it in the `/credentials` subdirectory, and name it `service-account-key.json`.

1. Create a `credentials/` subdirectory in the root directory and add it to `.gitignore`.
2. Place the downloaded service account key in the `credentials/` directory.
3. Create a `.env` file in the `src/` directory with the following content:

   ```
   GOOGLE_CLOUD_PROJECT=your-project-name
   GOOGLE_CLOUD_BUCKET=your-bucket-name
   GOOGLE_APPLICATION_CREDENTIALS=credentials/service-account-key.json
   ```

4. Enable the Google Earth Engine (GEE) API for your project and register for GEE usage.
5. Run `earthengine authenticate` in your terminal.

### Setup

Install the following tools:

1. `pipenv`: Follow the instructions at https://pipenv.pypa.io/en/latest/installation.html
2. `pyenv`: Follow the instructions at https://github.com/pyenv/pyenv

Once installed and the repo is cloned, navigate to the root directory, install Python 3.11, install dependencies, and activate the virtual environment:

```
pyenv install 3.11
pyenv local 3.11
pipenv install
pipenv shell
```
