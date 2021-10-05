# Stop Signal Task - fMRI
## Overview:
Welcome! This is Professor Neil McNaughton's Lab's Stop Signal Task (SST) 
experiment (see the below figure). This SST was created with the intention of 
being used in conjunction with functional magnetic resonance imaging (fMRI). 

As is standard with SSTs this task can be broken into two types of trials: 
go trials and stop trials. A single go trial our SST consists of the 
following steps: a variable inter-trial interval (ITI), a 0.5 s attention 
stimulus, a 1 s directional stimulus, and a 0.5 s feedback stimulus. The ITI 
times are a set of values, between 0.5 and 4 s, which were sampled from a 
logarithmic distribution (*t(x) = -ln(x)/λ*). While these times will appear 
random to a participant engaging with the task, they are fixed across all 
trials. 

In the case of stop trials, all of the steps are the same with the exception
of the directional stimulus where a stop sound will play some time after the 
stimulus has been presented. It is the participant's job to refrain from 
entering a left or right key press when they hear the sound. The time between 
the onset of the stimuli and the stop sound, known as the stop signal delay 
(SSD), is drawn from one of three staircase designs.

![SST Flowchart](doc/figures/SST_flow_2021-07-20.png?raw=true "SST flowchart")



## Installation:
The SST is has been created in [PsychoPy3](https://www.psychopy.org/) 
and requires [PsychoPy3 2021.1.3](https://github.com/psychopy/psychopy/releases) 
or newer to run (provided PsychoPy's "Use PsychoPy version:" option still works).


## Quick Set Up:
Once PsychoPy3 is installed you can open `SST.psyexp` and run the task. If you 
installed a newer version of PsychoPy3 you may need to change the PsychoPy 
version being used to run the task. This should be located under: 
__experiment settings__ (the gear icon) __-> Basic -> Use PsychoPy version__.

As stated above, this SST was created with the intention of being used in 
conjunction with functional magnetic resonance imaging (fMRI). As such, in 
between blocks of trials the task will wait for a keyboard press (`=` by 
default) before continuing the experiment.

Additionally, the left and right response keys are mapped to `2` & `3` for 
right handed participants and `7` & `8` for left handed participants. 
<!---These can be changed in the code if necessary (see wiki [link]).--->

Ensure your conditions file has been filled out correctly. 
The conditions file is used to define the trial blocks and the type of trial 
presented to the participant. In particular trials labelled `0` under 
`TrialTypes` will be __go__ trials, while any other integer will be a __stop__ 
trials with each number representing a unique staircase. Each block is defined 
by a set of repeating integers under the `Block` header. For example, 
*1, 1, 1, 2, 2, 2, 3, 3, 3* indicates three blocks: 1, 2, and 3. These integers 
must be in ascending order. The `BlockType` column is used to indicate whether 
or not a block is a practise run or not. This is important as practise blocks
will not wait for a `=` keyboard press to trigger them and will not have stop 
trials. To indicated a block as a practise block simply insert the keyword 
`practice` under the `BlockType` column, next to the first integer in the block.
Any other keyword will be treated as "not-a-practise." So I like to use `fMRI`.
Finally, the `L2R_ratio` column is used to indicate the ratio of left stimuli 
to right stimuli you would like to appear during each block. Leaving this 
column empty will default practise blocks to *0.5* (or a *50:50* split) and 
stop blocks to a random ratio.


### Disabling ESC and Fullscreen:
By default I have left the task with full screen disabled and the Esc key, 
which exits the task, available. This is because I assume you'd like to test 
the task before using it on participants. 
To enable fullscreen you will need to go into the `experiment settings` and 
untick the `Enable Escape key` tick box in under the __Basic__ tab (see 
Figure 3). Likewise, to disable the escape key you will need to go into the 
`experiment settings` and untick the `Full-screen window` tick box in under the 
__Screen__ tab (see Figure 3).

![DisableFSandESC](doc/figures/DisableFSandESC.png.png?raw=true "Disable Fullscreen and ESC key")
<p align="center" style="font-size:10px">
    Figure 3<br />  
    Menus to traverse in order to disable the Escape key and/or enable full 
    screen.
</p>



---
---
#COPY PASTE OF THE WIKI DOCUMENT:
# ♥ The Stop Signal Task ♥
This is the companion wiki for the Stop Signal Task (SST) written in PsychoPy for 
Niel McNorton’s lab in 2021 using the PsychoPy builder API. Its purpose is to 
illustrate where in the SST (Figures 1 (a) & (b)) the settings and code 
for each element of the flow chart (Figure 1 (c)) can be found. For information 
on the behaviour of the SST see the ReadMe of this repository or Appendix A.
![Circle Array](doc/figures/fullsetup.png?raw=true "SST flowchart")

<p align="center" style="font-size:10px">
    Figure 1<br />  
    (a) The PsychoPy Builder interface. (b) An expanded flow chart map which 
    is shown in the Builder under the ‘Flow’ section. (c) The experimental 
    flow chart of the Stop Signal Task as the subject experiences it.
</p>


In Figure 1 (c) there are seven steps in a single loop of the task which have 
been labelled 1 through to 7 respectively. These steps consist of: 
    1. Sequence preparation
    2. A subject attention focus circle
    3. Stimulus display
    4. Blank wait screen
	5. Feedback display
	6. Variable subject wait time

Additionally, I will also discuss the external functions (Subject GUI and sound 
testing script) called prior to the sequence shown in Figure 1 and the 
conditions file (which is used to determine the number of blocks in a task, 
the trail types present in each block, and the ratio of left to right arrows 
present in each block).

Finally, and of some import, is the naming convention I use in this document.  
The PsychoPy Builder structures tasks in three levels: Routines, Components, 
and Properties (see Figure 2). A brief description of level is given below, 
but for our purposes you just need to know where they’re located in the 
Builder. When referring to a specific level I will use the syntax: 
'Routine' -> "Component" -> ‘”Property”’. I chose this syntax over the 
standard folder path syntax to ensure uniqueness. 

![Circle Array](doc/figures/builder_codeblock.png?raw=true "PsychoPy SST")
<p align="center" style="font-size:10px">
    Figure 2<br />  
    An illustration of the location of the Routines, Components, and 
    Properties inside the PsychoPy Builder interface.
</p>

__Routine:__ 
“An experiment consists of one or more Routines. A Routine might 
specify the timing of events within a trial or the presentation of 
instructions or feedback” (excerpt from the PsychoPy webpage). 

__Component:__
“Routines in the Builder contain any number of components, which typically 
define the parameters of a stimulus or an input/output device” (excerpt from 
the PsychoPy webpage).

__Property:__ 
Properties are where the settings of a component are viewed and edited. 
These are accessed by clicking on the component in the builder.




## Section 1 - Sequence Elements

### 1.1 Pre-trial & pre-block processing 1]:
Before each trial, and each block of trials, there are some things which aren't
shown in Figure 1 that need to be determined, such as:
    I.   Counters
    II.  Preparing stop signal delay (SSD) staircases    
    III. Average participant reaction time
    IV.  Choosing display messages
    V.   Pre-block start countdown

#### I. Counters:
There are two counters used by various other code blocks within the SST 
experiment, these counters are: `current_trial` and 
`current_block_trial`. True to their names, the first serves to keep track of 
the total number of trails that have occurred within the experiment and the 
second keeps track of which block the experiment is up to. These counters are 
incremented in 'Pre_Trial' -> "pre_trial_prep" -> ‘”Begin Routine”’ under 
`# Increment counters`.


#### II. Preparing SSD staircases:
During each block of trials the participant will experience stop trials 
(except, of course, during practise runs). When these stop trails occur a
sound will play some time after the directional stimuli (arrows) are presented.
This time is called the stop signal delay (SSD). It indicates to the 
participant that they must refrain from pressing anything. 

The duration of the SSD is controlled by three independent staircases. 
Which stop trials correspond to which staircases is controlled by the user in
the `conditions.xlsx` file. At the beginning of the block of trials each 
staircase is assigned a time equal to *20 %*, *40 %*, and *80 %* of the 
average of the participant's last 16 reaction times (see Section 1.1 III 
below).

Following each stop trial, the SSD staircase that was used is adjusted in a 
0.05 s increment (see section 1.5). Increasing the delay time if the subject 
answers a stop trail correctly and decreasing it if they answer incorrectly 
(see Section 1.5).

##### Builder implementation:
The sections used to for SSDs are located under:
	'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’
	'Rest_Period' -> "block_prep" -> ‘”Begin Routine”’

###### 'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’:
The constants under `# SSD settings ` hold the settings used for defining a 
participant's initial staircase SSDs and the minimum/maximum times these SSDs
can be.

###### 'Rest_Period' -> "block_prep" -> ‘”Begin Routine”’:
The participant's initial staircase times are calculated under 
`## Calculate SSDs`.


#### III. Average participant reaction time:
During non-practice trials participants will perform stop trials. These trails
use different delay times which are initially determined by taking specific 
ratio of the participant's go-trial reaction time averaged over their most 
recent 16 go-trials. 

##### Builder implementation:
The storage of the averages and subsequent averaging are located under:
	'Instructions' -> "run_on_start" -> ‘”Before Experiment”’
	'go_feedback' -> "checkKeypress_go" -> ‘”Begin Routine”’
	'Rest_Period' -> "block_prep" -> ‘”Begin Routine”’

###### 'Instructions' -> "run_on_start" -> ‘”Before Experiment”’:
The section of code under `## Generate necessary variables for...` is used 
to initialise the array for storing the go-trial reaction times into.

###### 'go_feedback' -> "checkKeypress_go" -> ‘”Begin Routine”’:
Every time a go-trial occurs the participant’s reaction time is recorded and
stored into the `goRTs` array under `# Store reaction time for SSD computation`.

###### 'Rest_Period' -> "block_prep" -> ‘”Begin Routine”’:
The averaging of the 16 most recent go-trial reaction times is found under 
`## Average the subject's last 16 RT's`.



#### IV. Choosing display messages:
Between blocks display messages are loaded onto the screen to let the 
participant know what is happening during the experiment.

##### Builder implementation:
These messages are found and implemented under:
	'Rest_Period' -> "block_prep" -> ‘”Before Experiment”’
	'Rest_Period' -> "block_prep" -> ‘”Begin Routine”’
	'Wait4Celeritas' -> "wait_message"

###### 'Rest_Period' -> "block_prep" -> ‘”Before Experiment”’:
This is where the constant strings containing each message for the participant 
are defined.

###### 'Rest_Period' -> "block_prep" -> ‘”Begin Routine”’:
What message is displayed to the participant depends on whether the upcoming 
block of trails is a practise block (one where the participant can become 
familiar with the task) or a real block (where data is actually collected)
depends on a few logic statements in the code. These logic statements are 
found under: `## Choose which message to display to the subject`.

###### 'Wait4Celeritas' -> "wait_message":
This text object is used to display the message to the participant. 
The properties menu for the "wait_message" text object houses the font, 
font-size, and text colour settings.


#### V. Running a pre-block countdown:
This routine simply give the participant warning that the next block of trials 
are about to begin by displaying a 10 second countdown. The routine is self 
contained and consists of 10 text objects which appear on screen during their 
respective seconds.






### 1.2 – Subject attention focus circle, 2]:
The focus circle shown in Figure 1 (c) serves to draw the patient's attention 
to the centre of the screen before the stimulus is displayed.

#### Builder implementation:
The sections used to adjust the focus circle are located under:
	'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’
	'Standby' -> "focus_circle"

##### 'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’:
Under Stimulus and feedback images, this code block holds the user settings for 
the focus circles, direction stimulus (arrows), and the feedback images:
```python
# Stimulus and feedback images:
fb_size = 0.6675
arrowStimSize = 0.18
circle_size = 1.24
circle_thickness = 3
```

##### 'Standby' -> "focus_circle":
The properties menu for the "focus_circle" object houses additional settings
such as colour, screen position, and onset duration.





### 1.3 – Subject stimulus, 3]:
Following the focus stimulus, the circle changes to green and the participant is 
presented with a left or right pointing arrow. The participant has 1 second to
respond with a key press, where valid key presses are chosen from the 
participant's handedness (see Chapter 2, section 1). 

There are three notable sections in 'go_stim' and four in 'stop_stim'. These 
are broken into:
    I.   green focus circle
    II.  arrow image
    III. key press
    IV.  stop_sound (exclusive to stop_stim)

I: The green focus circle is simply a replica of the white focus circle from 2] 
and serves as a visual que for the participant that they need to make a 
response. 

II: The arrow image is an on screen print of the correct response, `=>` or 
`<=`. As was briefly mentioned in the ReadMe of this repository these arrows 
are not pre-determined but generated at the very start of the experiment for 
all blocks and trials. However, the ratio of `<=` to `=>` in each block depends 
on the `L2R_ratio` column of the `conditions.xlsx` file. If no `L2R_ratio` 
column is present then the `BlockType` column is used with `practice` blocks to 
*0.5* (or a *50:50* split) and stop blocks to a random ratio.

III: From the moment the arrow stimuli appear PsychoPy will wait for a valid 
keypress which will correspond to either *left* or *right*. Which keys are 
valid depends on the subject's handedness. Once a key is pressed the 
__Routine__ moves to the next __Routine__ (4], see section 1.4); removing the 
stimuli and green circle in the process. Additionally, when a key press is 
made the reaction time is recorded. This reaction time, *t_r*, is used (see 
section 1.4) to create an Inter-Stimulus Interval (ISI) between the arrow 
stimuli and the feedback equal to *1* s *- t_r*.

IV: If the trail presented to the subject is a stop trial then a stop sound
will play after the participant's SSD time has elapsed.

#### I Builder implementation:
I. The sections used to adjust the green focus circle are located under:
	'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’
	'go_stim' -> "green_go_polygon"
for go trials and 
	'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’
	'stop_stim' -> "green_stop_polygon"
for stop trials.

##### 'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’:
These are the same settings outlined in section 1.2 above.

##### 'go_stim' -> "green_go_polygon":
The properties menu for the "green_go_polygon" polygon object houses additional 
settings such as colour, screen position, and onset duration.

##### 'stop_stim' -> "green_stop_polygon":
The properties menu for the "green_stop_polygon" polygon object houses 
additional settings such as colour, screen position, and onset duration.
---


#### II Builder implementation:
II. The sections used to adjust the stimulus arrows are located under:
	'Instructions' -> "run_on_start" -> ‘”Before Experiment”’
	'Pre_Trial' -> "pre_trial_prep" -> ‘”Begin Routine”’
	'go_stim' -> "arrow_stim_go"
for go trials and 
	'Instructions' -> "run_on_start" -> ‘”Before Experiment”’
	'Pre_Trial' -> "pre_trial_prep" -> ‘”Begin Routine”’
	'stop_stim' -> "arrow_stim_stop"
for stop trials.

##### 'Instructions' -> "run_on_start" -> ‘”Before Experiment”’:
The code used to generate the left and right arrows can be found under 
`## Generate Stim Arrows` which uses the function `gen_LR_array()`. Once 
generated, the arrows are stored in the Python variable `direction`.

##### 'Pre_Trial' -> "pre_trial_prep" -> ‘”Begin Routine”’:
Under `# Call trial arrow` the current trial's arrow is called from the arrows
stored in `direction` using the `current_trial` counter (which keeps track of 
the total number of elapsed trials).

Additionally, this code block is also where whether or not the next trial is a 
Go trial or a Stop trial is determined (under: `# Check go/stop trial`).

##### 'go_stim' -> "arrow_stim_go":
The properties menu for the "arrow_stim_go" text object houses additional 
settings such as font. Text size is included in 'SETTINGS' -> "user_settings" 
-> ‘”Before Experiment”’ (see section 1.2 above).

##### 'stop_stim' -> "arrow_stim_stop":
The properties menu for the "arrow_stim_stop" text object houses additional 
settings such as font. Text size is included in 'SETTINGS' -> "user_settings" 
-> ‘”Before Experiment”’ (see section 1.2 above).
---


#### III Builder implementation:
III. The section used to adjust the recording of participant's key presses are
	'go_stim' -> "gokey_resp"
for go trials and 
	'stop_stim' -> "stopkey_resp"
for stop trials.

##### 'go_stim' -> "gokey_resp":
The properties menu for the "gokey_resp" key-press object houses 
additional settings such as duration, allowed keys, and whether or not to 
force the end of the Routine on a key press. 

##### 'stop_stim' -> "stopkey_resp":
The properties menu for the "stopkey_resp" key-press object houses 
additional settings such as duration, allowed keys, and whether or not to 
force the end of the Routine on a key press.
---


#### IV Builder implementation:
IV. The sections that control the stop sound settings are found under:
	'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’
	'stop_stim' -> "stop_sound"

##### 'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’:
The default values for the frequency and volume of the stop signal sound are 
found under `# Default sound values`. These can be overridden if the external 
sound function `TestSound()` is called (see Chapter 2 Section 2).

The delay before the stop sound is played following the arrow stimuli's onset
is called from the participant's SSD staircases. These are 
initially generated in 'Rest_Period' -> "block_prep" -> ‘”Begin Routine”’ under 
`## Average the subject's last 16 RT's and calculate starting SSDs` and 
actively managed in 'stop_feedback' -> "checkKeypress_stop" -> 
‘”Begin Routine”’ (see 5] - section 1.5).

##### 'stop_stim' -> "stop_sound":
The properties menu for the "stop_sound" sound object houses the duration 
setting and the shows the variable names corresponding to the settings 
outlined above.





### 1.4 – ISI delay, 4]:
Once the stimuli have been shown to the subject there is a short ISI whose time 
is chosen to ensure the time from the onset of the arrow stimuli to the onset
of the feedback stimuli is always 1 s. In PsychoPy this is achieved by 
calculating the remaining time by subtracting the participants reaction time 
from 1 s and delaying the onset of the feedback by this duration.

#### Builder implementation:
The sections that control the stop sound settings are found under
	'go_feedback' -> "checkKeypress_go" -> ‘”Begin Routine”’
for go trials and
	'stop_feedback' -> "checkKeypress_stop" -> ‘”Begin Routine”’
for stop trials.

##### 'go_feedback' -> "checkKeypress_go" -> ‘”Begin Routine”’:
The ISI time is computed as described above in the section of code labelled
`#Compute ISI wait time after subject response`.

##### 'stop_feedback' -> "checkKeypress_stop" -> ‘”Begin Routine”’:
As for the go trials, the ISI time is computed as described above in the 
section of code labelled `#Compute ISI wait time after subject response`.





### 1.5 – Feedback, 5]:
Once the 1 second wait time is over, the participant receives feedback based 
on whether or not they responded to the SST correctly. That is, pressing the 
correct direction key for go trials and not pressing anything for stop trials.


#### Builder implementation:
The sections that control the stop sound settings are found under
	'go_feedback' -> "checkKeypress_go" -> ‘”Begin Routine”’
	'go_feedback' -> "go_feedback_img"
for go trials and
	'stop_feedback' -> "checkKeypress_stop" -> ‘”Begin Routine”’
	'stop_feedback' -> "stop_feedback_img"
for stop trials.

##### 'go_feedback' -> "checkKeypress_go" -> ‘”Begin Routine”’:
The chunk of code that determines what feedback the participant receives is 
found under: `## Determine feedback:`.

##### 'stop_feedback' -> "checkKeypress_go" -> ‘”Begin Routine”’:
Similarly, the chunk of code that determines what feedback the participant 
receives during stop trials is found under: `## Determine feedback:`. However,
this section also houses where the SSD time is adjusted, as mentioned in 
section 1.1.

##### 'go_feedback' -> "go_feedback_img":
The properties menu for the "go_feedback_img" image object houses the duration,
size, and position settings.

##### 'stop_feedback' -> "stop_feedback_img":
The properties menu for the "stop_feedback_img" image object houses the duration,
size, and position settings.





### 1.7 – Variable Subject Wait Time (ITI), 6]:
This section has the subject wait for a duration which randomly sampled from 
the logarithmic function
<p align="center">
    <i>t(x) = -ln(⁡x)/λ</i>,
</p>
such that *t(x) ∈ [ITImin, ITImax]* and each sampled value is a integer 
multiple of ITIfactor. Additionally, the scaling factor, *λ*, is chosen via 
*λ = meanITItime/1000*. Figure 3 shows an example of *10,000* samples 
using *t(x) ∈ [0.5, 4]* s,  *ITIfactor = 125* ms, and, 
*meanITItime = 1000* ms.


![ISI values](doc/figures/ISIvalues.png?raw=true "ISI values")
<p align="center">
    Figure 3<br />  
    A “typical” sample set of the logarithmic function used to determine our 
    variable ITI times (*100,000* samples).
</p>

#### Builder implementation:
The sections of code used to sample and implement said samples are located under:
	'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’
	'Instructions' -> "run_on_start" -> ‘”Before Experiment”’ 
	'Pre_Trial' -> "pre_trial_stim”  -> ‘”Begin Routine”’
	'ITI' -> "blank_ITI_stim"

##### 'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’:
Under Inter-Stimulus Interval settings, this code block holds the user 
settings for the sampling of the log function above:
```python
# Inter-Stimulus Interval settings (see 'Instructions' -> "run_on_start"):
meanITItime = 1000    # ms
ITImin      = 500     # ms
ITImax      = 4000    # ms
ITIfactor   = 125     # ms
```

##### 'Instructions' -> "run_on_start" -> ‘”Before Experiment”’:
Under Functions, the python function `sample_logdist()` performs a single 
sample of the above logarithmic function. Under `## Generating ITI times… `
the number of trials being used in the experiment is determined and the 
function `sample_logdist()` is called to generate an array of ITIs for each.

##### 'Pre_Trial' -> "pre_trial_prep" -> ‘”Begin Routine”’:
Under the section `# Call ITI time` the current trial number is used to call 
the appropriate ISI time so it may be used in the following Routine.

##### 'TTI' -> "blank_ITI_stim":
This black polygon (which is invisible to the subject on the task’s black 
background) displays for the duration called during the 'Pre_Trial' routine 
above.









## Section 2 - Pre-Sequence Functions
Some functions aren't shown in the flow chart at the beginning of this 
document (Figure 1). This is because they are called before the 
builder's sequence is started. Presently there are only two such functions. 
The GUI used to gather subject information and the PsychoPy script for 
testing the sound.


### 2.1 Subject Information GUI
Presently, PsychoPy’s default General User Interface (GUI) for inputting 
participant information isn't very good and only allows text inputs. To get 
around this limitation I coded a GUI in Tkinter and call 
this GUI as a function prior to the SST. I chose Tkinter because it is included 
as a base package in Python which means that no additional packages need to be 
loaded when using the SST task on other computers.

Figure 4 shows a picture of the GUI. It contains settings that allow the 
participant to indicate their participant number, their handedness, and their 
ethnicity. The are other options such as gender which are Presently
uncommented in the Python script. The last setting present in the GUI is a 
tick box which allows the user to indicate whether or not they would like to 
load the sound settings interface, see section 2.2.

![Tkinter GUI](doc/figures/GUI.png?raw=true "Participant details GUI")
<p align="center" style="font-size:10px">
    Figure 4<br />  
    An screenshot of the participant details GUI.
</p>

#### Implementation:
##### PsychoPy:
The section of code used to import the GUI into the SST is located under:
	'SETTINGS' -> "ext_scripts" -> ‘”Before Experiment”’

##### Python script:
The function where the Tkinter GUI is coded is found in 
`participant_details_GUI_v2p2.py` under the 
`external_functions` folder of this repository.







### 2.2 Test Sound PsychoPy Script
Because the SST involves playing a sound to the participant it naturally 
follows that a means to adjust the frequency and volume is needed. This takes
the form of a separate PsychoPy experiment made in the PsychoPy builder which
is used to generate PsychoPy python script which has then been cut down so 
that it can be imported into the SST builder as its own function. The reason
for doing it through this convoluted method is that I wanted to test the sound
natively within the PsychoPy but I didn't want to bloat the SST's flow panel.
Unfortunately, there isn't presently a method for calling/importing separate 
PsychoPy experiments into the builder. Hence, manually cutting down the python
script and manually loading it into the SST experiment.



#### PsychoPy experiment:
A copy of the test sound experiment made in the PsychoPy builder can be found 
under `external_functions\test_sound\TestSoundSettingsv1p1.psyexp` of this 
repository.

##### Python script:
Here I will talk about how I converted the PsychoPy psyexp test sound 
experiment to a Python function that can be called within the SST. This is
fundamentally straightforward if you have a good grasp on Python because 
PsychoPy is, at it's heart, a Python package. While the builder is simply a
piece of software to make it easy to generate the Python script without knowing 
Python. 

When `TestSoundSettingsv1p1.psyexp` is run inside the PsychoPy builder  
PsychoPy generates a `TestSoundSettingsv1p1_lastrun.py` file. This file is the 
Python code that, when run in Python, executes the experiment. The long and 
short method for converting this `.py` script (if you ever change the 
TestSoundSettings experment) is compare it with `test_soundv1p1.py` under 
`external_functions`. I have simply commented out the unnecessary sections
of code (using doc strings to distinguish them from standard comments) so it 
should be possible to compare the `test_soundv1p1.py` with 
`TestSoundSettingsv1p1_lastrun.py`.

The longer, and much more esoteric, answer is you will need to comment out the 
sections of code that generate a window and ExperimentHandler for the 
experiment. This is because we want to have PsychoPy bring up the Sound Test 
Settings inside the window generated by the SST. We then comment out the 
section that Initialises the PsychoPy components because we want to yield 
control of this step to the SST experiment. We then comment out the section of 
code which initialises Routine "Display" because this too is inside the SST. 
Finally, we remove any `thisExp.____` calls that are looking for variables that
are no longer present, such as `addLoop`.

Once the appropriate sections of code are removed, I wrap the Python in a 
function:
```python
def TestSound(SST_window, SST_defaultKeyboard, SST_expInfo, 
              SST_frameTolerance=0.001, SST_endExpNow=False, nReps=100):
    
    # Edited TestSoundSettingsv1p1_lastrun.py here
    
    return vol, freq 
```
Here, the parameters SST_window, SST_defaultKeyboard, SST_expInfo are the 
experiment window, keyboard, and info objects used in the SST PsychoPy script.
While SST_frameTolerance is how close to onset of a new screen the next screen 
can be to be considered the 'same' frame, SST_endExpNow is a flag for exiting 
the SST, and nReps is the number of times you can click the test sound button 
before breaking out of the PsychoPy loop. For almost all use cases these 
settings can be ignored.
        

#### SST Implementation:
The section of code used to import the sound test psychopy script into the SST 
is located under 'SETTINGS' -> "ext_scripts" -> ‘”Begin Routine”’. It simply
tells the SST to load and run the `TestSound` function.






## Appendix A - SST task overview
As is standard with SSTs this task can be broken into two types of trials: 
go trials and stop trials. A single go trial our SST consists of the 
following steps: a variable inter-trial interval (ITI), a 0.5 s attention 
stimulus, a 1 s directional stimulus, and a 0.5 s feedback stimulus. The ITI 
times are a set of values, between 0.5 and 4 s, which were sampled from a 
logarithmic distribution (*t(x) = -ln(x)/λ*). While these times will appear 
random to a participant engaging with the task, they are fixed across all 
trials. 

In the case of stop trials, all of the steps are the same with the exception
of the directional stimulus where a stop sound will play some time after the 
stimulus has been presented. It is the participant's job to refrain from 
entering a left or right key press when they hear the sound. The time between 
the onset of the stimuli and the stop sound, known as the stop signal delay 
(SSD), is drawn from one of three staircase designs.
