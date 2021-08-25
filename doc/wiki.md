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
    1. Variable subject wait time
    2. A subject attention focus circle
    3. Stimulus display
    4. Blank wait screen
	5. Feedback display
	6. 1000 ms of additional wait time
Additionally, I will also discuss the conditions file which is used to 
determine the number of blocks in a task, the trail types present in each 
block, and the ratio of left to right arrows present in each block.
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

 
## Section 01 – Variable Subject Wait Time, 1]:
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
  
Figure 3
A “typical” sample set of the logarithmic function used to determine our 
variable ISI times (*100,000* samples).

### Builder implementation:
The sections of code used to sample and implement said samples are located under:
	'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’
	'Instructions' -> "run_on_start" -> ‘”Before Experiment”’ 
	'Pre_Trial' -> "pre_trial_stim”  -> ‘”Begin Routine”’
	'ISI' -> "blank_ISI_stim"

#### 'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’:
Under Inter-Stimulus Interval settings, this code block holds the user 
settings for the sampling of the log function above:
```python
# Inter-Stimulus Interval settings (see 'Instructions' -> "run_on_start"):
meanISItime = 1000    # ms
ISImin      = 500     # ms
ISImax      = 4000    # ms
ISIfactor   = 125     # ms
```

#### 'Instructions' -> "run_on_start" -> ‘”Before Experiment”’:
Under Functions, the python function `sample_logdist()` performs a single 
sample of the above logarithmic function. Under `## Generating ISI times… `
the number of trials being used in the experiment is determined and the 
function `sample_logdist()` is called to generate an array of ISIs for each.

#### 'Pre_Trial' -> "pre_trial_prep" -> ‘”Begin Routine”’:
Under the section `# Call ISI time` the current trial number is used to call 
the appropriate ISI time so it may be used in the following Routine.

#### 'ISI' -> "blank_ISI_stim":
This black polygon (which is invisible to the subject on the task’s black 
background) displays for the duration called during the 'Pre_Trial' routine 
above.



## Section 02 – Subject attention focus circle, 2]:
This

### Builder implementation:
The sections used to adjust the focus circles are located under:
	'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’
	'Standby' -> "focus_circle"

#### 'SETTINGS' -> "user_settings" -> ‘”Before Experiment”’:
Under Stimulus and feedback images, this code block holds the user settings for the focus circles, direction stimulus (arrows), and the feedback images:
```python
# Stimulus and feedback images:
fb_size = 0.6675      
arrowStimSize = 0.18  
circle_size = 1.24  
circle_thickness = 3
```

#### 'Standby' -> "focus_circle":
Under 








