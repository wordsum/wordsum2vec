## wordsum2vec

A tool that extracts the character dialog and the narrator of a short or book story and plot the plots given with the different characters.

## Tools

1. wordsum 


## Source Structure:

wordsum/ src

tests/ unit tests

data/ is a directory to contain any test data or output data before it is put
        into a container image for archive.

data/test/ is a directory of wordsum modeled test data. The file hierarchy may get
        deeper as more test are had.

## Model Versioning

(Work in progress)

## Local Setup:

### Local Setup on Ubuntu with Python3 and virtualenv:

1. git clone https://github.com/wordsum/wordsum2vec

2. cd wordsum2vec

3. (if pip and virtualenv not installed) sudo apt-get install python3-pip python3-dev python-virtualenv python3.6-tk

4. virtualenv --system-site-packages -p python3 .

5. source ./bin/activate

6. export PYTHONHASHSEED=0

7. pip3 install -r requirements.txt

8. pip install --ignore-installed six


## Testing:
1  cd wordsum2vec
2. pytest test

## ToDo:
1. Test everything...


##Copyright

  Open Story License

  Story: wordsum2vec
  Writer: Kalab J. Oster&trade;
  Copyright Holders: Kalab J. Oster&trade;
  copyright &copy; 2017 Kalab J. Oster&trade;

  Permission is granted by the Copyright Holders for humans or other intelligent agents to read, write, edit, publish and critique the Story
  if the humans or intelligent agents keep this Open Story License with the Story,
  and if the Story you tell remains free,
  and if another writer writes or edits the Story then the writer's name needs to be appended to the end of the Writer list of this Open Story License.