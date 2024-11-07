# Example poll wrapper

This project creates the wrapper flows that should be used alongside a poll within RapidPro. There is a pipeline which takes the csv inputs in the 'poll data' folder and creates the wrappers.

## Usage

The pipeline is intended to be run by triggering a Github Actions workflow or by running commands on the command line.

## Github actions

1. Navigate to the page for the [Produce Poll Wrappers][1] action
2. Click on the _Run workflow_ button; a drop-down will appear
3. Make sure _Branch_ is set to _main_
4. Click on the green _Run workflow_ button

## Running from command line

These steps need to be followed if you want to run the pipeline from the command line or develop the pipeline further.

### Setup

1. Clone or fork the repo to a local folder
1. Install Python >= 3.8
1. Create a Python virtual environment `python -m venv .venv`
1. Activate the environment:
    - Linux: `source .venv/bin/activate`
    - Windows: `.venv/Scripts/activate`
1. Upgrade pip `pip install --upgrade pip`
1. Install project Python dependencies `pip install -r requirements.txt`
1. Install latest Node and NPM Long-Term Support (LTS) versions
1. Install project Node dependencies `npm install`
1. Change to the 'techical' folder where the config.json file is held `cd technical`

## Run

```
python -m parenttext_pipeline.cli pull_data compile_flows 
```

