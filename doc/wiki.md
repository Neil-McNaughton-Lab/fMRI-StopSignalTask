# ♥ The Stop Signal Task ♥
This is the companion wiki for the Stop Signal Task (SST) written in PsychoPy for 
Niel McNorton’s lab in 2021 using the PsychoPy builder API. Its purpose is to 
illustrate where in the SST (Figures 1 (a) & (b)) the settings and code 
for each element of the flow chart (Figure 1 (c)) can be found. For information 
on the behaviour of the SST see the ReadMe of this repo or Appendix A.
![Circle Array](doc/figures/fullsetup.png?raw=true "SST flowchart")

<p align="center">
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

![Circle Array](doc/figures/builder_codeblock.png?raw=true "Psychopy SST")
<p align="center">
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
the total number of trails that have occured within the experiment and the 
second keeps track of which block the experiment is up to. These counters are 
incremented in 'Pre_Trial' -> "pre_trial_prep" -> ‘”Begin Routine”’ under 
`# Increment counters`.


#### II. Preparing SSD staircases:
During each block of trials the participant will experience stop trials 
(except, of course, during practise runs). When these stop trails occur a
sound will play some time after the directional stimuli (arrows) are presented.
This time is called the stop signal delay (SSD). It indicates to the 
participant that they must refrain from pressing anything. 

The duration of the SSD is controlled by three independant staircases. 
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
participant's inital staircase SSDs and the minimum/maximum times these SSDs
can be.

###### 'Rest_Period' -> "block_prep" -> ‘”Begin Routine”’:
The participant's inital staircase times are calculated under 
`## Calculate SSDs`.


#### III. Average participant reaction time:
During non-practice trials participants will perform stop trials. These trails
use different delay times which are initally determined by taking specific 
ratio of the participant's go-trial reaction time averaged over their most 
recent 16 go-trials. 

##### Builder implementation:
The storage of the averages and subsequent averaging are located under:
	'Instructions' -> "run_on_start" -> ‘”Before Experiment”’
	'go_feedback' -> "checkKeypress_go" -> ‘”Begin Routine”’
	'Rest_Period' -> "block_prep" -> ‘”Begin Routine”’

###### 'Instructions' -> "run_on_start" -> ‘”Before Experiment”’:
The section of code under `## Generate necessary variables for...` is used 
to initalise the array for storing the go-trial reaction times into.

###### 'go_feedback' -> "checkKeypress_go" -> ‘”Begin Routine”’:
Every time a go-trial occurs the paticipant's reaction time is recorded and
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
size, and poition settings.

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
The GUI used to gather subject information and the psychopy script for 
testing the sound.


### 2.1 Subject Information GUI
The


### 2.2 Test Sound Psychopy Script
The

##### 'SETTINGS' -> "ext_scripts" -> ‘”Begin Routine”’:
T





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
