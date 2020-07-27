# Shakespeare-In-Your-Service
** This is a mini Project in which I have made a Sequence Model, that would complete a Poem provided some initial words.

** The user needs provide 2 arguments to generate the sequence- The initial phrase & Required length of generated sequence.

** The model uses a Many to One sequence generation RNN to generate the next probable word.

** The model was trained on text sequences of length 20 (due to restricted RAM), on Google Colab on a GPU.

** However, the model performs good only upto a small length of sequence generation (normally length of 600), after that it starts repeating same words. One way to avoid this is, using an LSTM or GRU which are able to capture long term dependencies (which I will try to incorporate in future versions).

![Training Loss](/loss.jpg)

** An example of generated poem (of length 500) is-

```
Input: "brave was he"

Output: "brave was her than thou art the dear love you living sick of you, but not the disgrace, And summer's successify's day, To line, Then look into the beauty doth the time do I not muse, and make wire is thine and in my mind, So thou art strangely pass, By self-killed: That thou art thy mind's dead, Than you with thee that the world to stop parthese in thee and thine image strengths of mine own desert, And therefore to be must not be foes.    Those lips thou art thy mind's dead, Than you with thee"
```

** The repository contains following files-
	- Model.ipynb: Contains all the code in single IPython Notebook.
	- Shakespere.txt: Contains the data which is taken from Shakespeare's famous poem Sonet.
	- predict.py: Contains code to generate the sequence.
	- server.py: Contains code to push the prediction on localhost server. 
	- shakespeare-rnn-generation.pt: It is the weights file for the RNN model.
