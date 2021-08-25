#![Circle Array](doc/figures/fullsetup.png?raw=true "SST flowchart")
#![Circle Array](doc/figures/builder_codeblock.png?raw=true "Psychopy SST")

# Stop Signal Task - fMRI
## Overview
Welcome! This is Neil McNaughton Lab's Stop Signal Task (SST) experiment (see 
the below figure). This SST was created with the intention of being used in 
conjunction with functional magnetic resonance imaging (fMRI). 

As is standard with SSTs this task can broken into two types of trials: 
go trials and stop trials. A single go trial our SST consists of the 
following steps: a variable inter-trial interval 
(ITI), a 0.5 s attention stimulus, a 1 s directional stimulus, and a 0.5 s 
feedback stimulus. The ITI times are a set of values, between 0.5 and 4 s, 
which were sampled from a logarithmic distribution (t(x) = -ln(x)/λ). While 
these times will appear random to a participant engaging with the task, they 
are fixed across all trials. 

In the case of stop trials, all of the steps are the same with the exception
of the directional stimulus where a stop sound will play some time after the 
stimulus has been presented. It is the participant's job to refrain from 
entering a left or right key press when they hear the sound. The time between 
the onset of the stimuli and the stop sound, known as the stop signal delay 
(SSD), is drawn from one of three staircase designs.

![SST Flowchart](doc/figures/SST_flow_2021-07-20.png?raw=true "SST flowchart")


## Installation:
The SST is has been created in [PsychoPy3](https://github.com/psychopy/psychopy/releases) 
and requires PsychoPy3 2021.1.3 or newer to run (provided PsychoPy's "Use 
PsychoPy version:" option still works).


## Quick Set Up:
Once PsychoPy3 is installed you can open `SST.psyexp` and run the task. If you 
installed a newer version of PsychoPy3 you may need to change the PsychoPy 
version being used to run the task. This should be located under: 
`experiment settings`(the gear icon) `-> Basic -> Use PsychoPy version`.

As stated above, this SST was created with the intention of being used in 
conjunction with functional magnetic resonance imaging (fMRI). As such, in 
between blocks of trials the task will wait for a keyboard press (`=` by 
default) before continuing the experiment.

Additionally, the left and right response keys are mapped to `2` & `3` for 
right handed participants and `7` & `8` for left handed participants. 
<!---These can be changed in the code if necessary (see wiki [link]).--->