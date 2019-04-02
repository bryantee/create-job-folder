# Create a Job!

## The problem being solved
This project was concieved years ago while I was working for a general contractor. At the time it aimed to solve the problems we faced with keeping track of jobs and associated files in an organized and structured way. The basic premise of this script was to maintain a client list, and based on the job type being started, a user could easily add the job, assign a client and name the job. The script takes care of appending the correct date for sortability, placing it in the corresponding client folder and then copying over the template directory structure and potential starter files.

## Roadmap foing forward
- [x] Add full database support for easier management and portability
- [ ] Add a gui using tkinter
- [ ] Add true dropbox support using sdk

## Installation and running the script
To get it up and running, you'll first need to install dependencies:

```sh
# python2
pip install -r requirements.txt

#python3
pip3 install -r requirements.txt
```

Running the script is as simple as:
```sh
python create_job.py
```