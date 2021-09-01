# The Stop Signal Task
This is the companion wiki for the Stop Signal Task (SST) written in PsychoPy for 
Niel McNorton’s lab in 2021 using the PsychoPy builder API. Its purpose is to 
illustrate where in the SST (Figures 1 (a) & (b)) the settings and code 
for each element of the flow chart (Figure 1 (c)) can be found.
![Circle Array](doc/figures/fullsetup.png?raw=true "SST flowchart")

<p align="center">
    Figure 1<br />  
    (a) The PsychoPy Builder interface. (b) An expanded flow chart map which 
    is shown in the Builder under the ‘Flow’ section. (c) The experimental 
    flow chart of the Stop Signal Task as the subject experiences it.
</p>


In Figure 1 (c) there are seven steps in a single loop of the task which have 
been labelled 1 through to 7 respectively. These steps consist of: 
    1. Sequence start
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
### 1.1 – Variable Subject Wait Time, 6]:
This section has the subject wait for a duration which randomly sampled from 
the logarithmic function
<p align="center">
    <i>t(x) = -ln(⁡x)/λ</i>,
</p>
such that *t(x) ∈ [ISImin, ISImax]* and each sampled value is a integer 
multiple of ISIfactor. Additionally, the scaling factor, *λ*, is chosen via 
*λ = meanISItime/1000*. Figure 3 shows an example of *10,000* samples 
using *t(x) ∈ [0.5, 4]* ms,  *ISIfactor = 125* ms, and, 
*meanISItime = 1000* ms.


![ISI values](doc/figures/ISIvalues.png?raw=true "ISI values")
<p align="center">
    Figure 3<br />  
    A “typical” sample set of the logarithmic function used to determine our 
    variable ISI times (*100,000* samples).
</p>

#### Builder implementation:
The sections of code used to sample and implement said samples are located under:
	'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’
	'Instructions' -> "run_on_start" -> ‘”Before Experiment”’ 
	'Pre_Trial' -> "pre_trial_stim”  -> ‘”Begin Routine”’
	'ISI' -> "blank_ISI_stim"

##### 'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’:
Under Inter-Stimulus Interval settings, this code block holds the user 
settings for the sampling of the log function above:
```python
# Inter-Stimulus Interval settings (see 'Instructions' -> "run_on_start"):
meanISItime = 1000    # ms
ISImin      = 500     # ms
ISImax      = 4000    # ms
ISIfactor   = 125     # ms
```

##### 'Instructions' -> "run_on_start" -> ‘”Before Experiment”’:
Under Functions, the python function `sample_logdist()` performs a single 
sample of the above logarithmic function. Under `## Generating ISI times… `
the number of trials being used in the experiment is determined and the 
function `sample_logdist()` is called to generate an array of ISIs for each.

##### 'Pre_Trial' -> "pre_trial_prep" -> ‘”Begin Routine”’:
Under the section `# Call ISI time` the current trial number is used to call 
the appropriate ISI time so it may be used in the following Routine.

##### 'ISI' -> "blank_ISI_stim":
This black polygon (which is invisible to the subject on the task’s black 
background) displays for the duration called during the 'Pre_Trial' routine 
above.




### 1.2 – Subject attention focus circle, 2]:
The focus circle shown in Figure 1 (c) serves to draw the patient's attention 
to the center of the screen before the stimulus is displayed.

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
`<=`. As was breifly mentioned in the ReadMe of this repository these arrows 
are not pre-determined but generated at the very start of the experiment for 
all blocks and trials. However the ratio of `<=` to `=>` in each block depends 
on the `L2R_ratio` column of the `conditions.xlsx` file. If no `L2R_ratio` 
column is present then the `BlockType` column is used with `practice` blocks to 
*0.5* (or a *50:50* split) and stop blocks to a random ratio.

III: From the moment the arrow stimuli appear PsychoPy will wait for a valid 
keypress which will correspond to either *left* or *right*. Which keys are 
valid depends on the subject's handedness. Once a key is pressed the 
__Routine__ moves to the next __Routine__ (4], see section 1.4); removing the 
stimuli and green circle in the process.

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
The code used to generated the left and right arrows can be found under 
`## Generate Stim Arrows` which uses the function `gen_LR_array()`. Once 
generated, the arrows are stored in the Python variable `direction`.

##### 'Pre_Trial' -> "pre_trial_prep" -> ‘”Begin Routine”’:
Under `# Call trial arrow` the current trial's arrow is called from the arrows
stored in `direction` using the `current_trial` counter (which keeps track of 
the total number of elapsed trials).

Additonally, this code block is also where whether or not the next trial is a 
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
is called from the participant's SSD staircases. These are initally generated 
in 'Rest_Period' -> "block_prep" -> ‘”Begin Routine”’ under 
`## Average the subject's last 16 RT's and calculate starting SSDs` and 
actively managed in 'stop_feedback' -> "checkKeypress_stop" -> 
‘”Begin Routine”’ (see 5] - section 1.4).


##### 'stop_stim' -> "stop_sound":
The properties menu for the "stop_sound" sound object houses the duration 
setting and the shows the variable names corresponding to the settings 
outlined  above.





### 1.4 – ISI delay & feedback, 4, 5]:












## Section 2 - Pre-Sequence Functions
Some functions aren't shown in the flow chart at the beginning of this 
document (Figure 1). This is because they are called before the 
builder's sequence is started. Presently there are only two such functions. 
The GUI used to gather subject information and the the psychopy script for 
testing the sound.


### 2.1 Subject Information GUI
The


### 2.2 Test Sound Psychopy Script
The

##### 'SETTINGS' -> "ext_scripts" -> ‘”Begin Routine”’:
T

