﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on June 28, 2021, at 15:04
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'TestSoundSettingsv1p1'  # from the Builder filename that created this script
expInfo = {'': ''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.sep + u'psychopy_data_' + data.getDateStr()

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='S:\\Research\\Neil McNaughton\\Rhys\\PsychoPy\\Test_Sound\\TestSoundSettingsv1p1_lastrun.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Settings"
SettingsClock = core.Clock()
sound_freq_test_range = [100, 2000] # Hz
sound_freq_test_steps = 50 # Hz
sound_freq_default = 500

# Initialize components for Routine "TestSound"
TestSoundClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Soundcard Testing',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Set default values:
vol = 0.06120702


Volume = visual.Slider(win=win, name='Volume',
    size=(0.4, 0.05), pos=(0, 0), units=None,
    labels=('0', '', '', '', '', '', '', '', '', '', '1'), ticks=(0.0, 0.061207024560089175, 0.12885124808584156, 0.2036096767023117, 0.2862305178902687, 0.3775406687981455, 0.47845399210662964, 0.5899804622735316, 0.7132362736976229, 0.8494550119673449, 1.0), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-2, readOnly=False)
print_vol = visual.TextStim(win=win, name='print_vol',
    text='',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
# Set default Values:
freq = sound_freq_default
frequency = visual.Slider(win=win, name='frequency',
    size=(0.05, 0.4), pos=(-0.4, 0.0), units=None,
    labels=(sound_freq_test_range[0], sound_freq_test_range[1]), ticks=(sound_freq_test_range[0], sound_freq_test_range[1]), granularity=sound_freq_test_steps,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-5, readOnly=False)
print_freq = visual.TextStim(win=win, name='print_freq',
    text='',
    font='Open Sans',
    pos=(-0.4, 0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
test_sound = visual.ButtonStim(win, 
   text='Test Sound', font='Arvo',
   pos=(0.5, 0),
   letterHeight=0.05,
   size=[0.25/1.25, 0.25], borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='white', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='test_sound')
test_sound.buttonClock = core.Clock()
confirm_sound = visual.ButtonStim(win, 
   text='Confirm Sound Settings', font='Arvo',
   pos=(0.5, -0.5),
   letterHeight=0.025,
   size=(0.25/1.125, 0.25), borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='white', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='confirm_sound')
confirm_sound.buttonClock = core.Clock()

# Initialize components for Routine "play_sound"
play_soundClock = core.Clock()
play_sound = 0
print(vol)
print(freq)
play_test_sound = sound.Sound('A', secs=0.5, stereo=True, hamming=False,
    name='play_test_sound')
play_test_sound.setVolume(1.0)

# Initialize components for Routine "Display"
DisplayClock = core.Clock()
result_display = visual.TextStim(win=win, name='result_display',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Settings"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
SettingsComponents = []
for thisComponent in SettingsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SettingsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Settings"-------
while continueRoutine:
    # get current time
    t = SettingsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SettingsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SettingsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Settings"-------
for thisComponent in SettingsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Settings" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop_back = data.TrialHandler(nReps=50.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop_back')
thisExp.addLoop(loop_back)  # add the loop to the experiment
thisLoop_back = loop_back.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_back.rgb)
if thisLoop_back != None:
    for paramName in thisLoop_back:
        exec('{} = thisLoop_back[paramName]'.format(paramName))

for thisLoop_back in loop_back:
    currentLoop = loop_back
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_back.rgb)
    if thisLoop_back != None:
        for paramName in thisLoop_back:
            exec('{} = thisLoop_back[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "TestSound"-------
    continueRoutine = True
    # update component parameters for each repeat
    # Place marker:
    if Volume.markerPos is None:
        Volume.markerPos = vol
    Volume.reset()
    frequency.reset()
    # keep track of which components have finished
    TestSoundComponents = [text_7, Volume, print_vol, frequency, print_freq, test_sound, confirm_sound]
    for thisComponent in TestSoundComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TestSoundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TestSound"-------
    while continueRoutine:
        # get current time
        t = TestSoundClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TestSoundClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        # Get the current value of the slider to print:
        if Volume.markerPos is None:
            Volume.markerPos = vol
        vol = Volume.markerPos
        
        # Correct to a percentage:
        corrected_vol = 100*(vol - Volume.ticks[0])/(Volume.ticks[-1] - Volume.ticks[0])
        corrected_vol = round(corrected_vol, 2)
        
        # Convert to string:
        string_vol = str(corrected_vol) + ' %'
        
        # *Volume* updates
        if Volume.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Volume.frameNStart = frameN  # exact frame index
            Volume.tStart = t  # local t and not account for scr refresh
            Volume.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Volume, 'tStartRefresh')  # time at next scr refresh
            Volume.setAutoDraw(True)
        
        # *print_vol* updates
        if print_vol.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            print_vol.frameNStart = frameN  # exact frame index
            print_vol.tStart = t  # local t and not account for scr refresh
            print_vol.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(print_vol, 'tStartRefresh')  # time at next scr refresh
            print_vol.setAutoDraw(True)
        if print_vol.status == STARTED:  # only update if drawing
            print_vol.setText('Volume: ' + string_vol)
        # Get the current value of the slider to print:
        if frequency.markerPos is None:
            frequency.markerPos = freq
        freq = frequency.markerPos
        
        # Convert to string:
        string_freq = str(freq) + ' Hz'
        
        # *frequency* updates
        if frequency.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            frequency.frameNStart = frameN  # exact frame index
            frequency.tStart = t  # local t and not account for scr refresh
            frequency.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(frequency, 'tStartRefresh')  # time at next scr refresh
            frequency.setAutoDraw(True)
        
        # *print_freq* updates
        if print_freq.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            print_freq.frameNStart = frameN  # exact frame index
            print_freq.tStart = t  # local t and not account for scr refresh
            print_freq.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(print_freq, 'tStartRefresh')  # time at next scr refresh
            print_freq.setAutoDraw(True)
        if print_freq.status == STARTED:  # only update if drawing
            print_freq.setText(string_freq)
        
        # *test_sound* updates
        if test_sound.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            test_sound.frameNStart = frameN  # exact frame index
            test_sound.tStart = t  # local t and not account for scr refresh
            test_sound.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_sound, 'tStartRefresh')  # time at next scr refresh
            test_sound.setAutoDraw(True)
        if test_sound.status == STARTED:
            # check whether test_sound has been pressed
            if test_sound.isClicked:
                if not test_sound.wasClicked:
                    test_sound.timesOn.append(test_sound.buttonClock.getTime()) # store time of first click
                    test_sound.timesOff.append(test_sound.buttonClock.getTime()) # store time clicked until
                else:
                    test_sound.timesOff[-1] = test_sound.buttonClock.getTime() # update time clicked until
                if not test_sound.wasClicked:
                    continueRoutine = False  # end routine when test_sound is clicked
                    play_sound = 1
                test_sound.wasClicked = True  # if test_sound is still clicked next frame, it is not a new click
            else:
                test_sound.wasClicked = False  # if test_sound is clicked next frame, it is a new click
        else:
            test_sound.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
            test_sound.wasClicked = False  # if test_sound is clicked next frame, it is a new click
        
        # *confirm_sound* updates
        if confirm_sound.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            confirm_sound.frameNStart = frameN  # exact frame index
            confirm_sound.tStart = t  # local t and not account for scr refresh
            confirm_sound.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirm_sound, 'tStartRefresh')  # time at next scr refresh
            confirm_sound.setAutoDraw(True)
        if confirm_sound.status == STARTED:
            # check whether confirm_sound has been pressed
            if confirm_sound.isClicked:
                if not confirm_sound.wasClicked:
                    confirm_sound.timesOn.append(confirm_sound.buttonClock.getTime()) # store time of first click
                    confirm_sound.timesOff.append(confirm_sound.buttonClock.getTime()) # store time clicked until
                else:
                    confirm_sound.timesOff[-1] = confirm_sound.buttonClock.getTime() # update time clicked until
                if not confirm_sound.wasClicked:
                    continueRoutine = False  # end routine when confirm_sound is clicked
                    loop_back.finished = True
                    play_sound = 0
                confirm_sound.wasClicked = True  # if confirm_sound is still clicked next frame, it is not a new click
            else:
                confirm_sound.wasClicked = False  # if confirm_sound is clicked next frame, it is a new click
        else:
            confirm_sound.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
            confirm_sound.wasClicked = False  # if confirm_sound is clicked next frame, it is a new click
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestSoundComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TestSound"-------
    for thisComponent in TestSoundComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_back.addData('text_7.started', text_7.tStartRefresh)
    loop_back.addData('text_7.stopped', text_7.tStopRefresh)
    loop_back.addData('Volume.response', Volume.getRating())
    loop_back.addData('Volume.rt', Volume.getRT())
    loop_back.addData('Volume.started', Volume.tStartRefresh)
    loop_back.addData('Volume.stopped', Volume.tStopRefresh)
    loop_back.addData('print_vol.started', print_vol.tStartRefresh)
    loop_back.addData('print_vol.stopped', print_vol.tStopRefresh)
    loop_back.addData('frequency.response', frequency.getRating())
    loop_back.addData('frequency.rt', frequency.getRT())
    loop_back.addData('frequency.started', frequency.tStartRefresh)
    loop_back.addData('frequency.stopped', frequency.tStopRefresh)
    loop_back.addData('print_freq.started', print_freq.tStartRefresh)
    loop_back.addData('print_freq.stopped', print_freq.tStopRefresh)
    loop_back.addData('test_sound.started', test_sound.tStartRefresh)
    loop_back.addData('test_sound.stopped', test_sound.tStopRefresh)
    loop_back.addData('test_sound.numClicks', test_sound.numClicks)
    if test_sound.numClicks:
       loop_back.addData('test_sound.timesOn', test_sound.timesOn)
       loop_back.addData('test_sound.timesOff', test_sound.timesOff)
    else:
       loop_back.addData('test_sound.timesOn', "")
       loop_back.addData('test_sound.timesOff', "")
    loop_back.addData('confirm_sound.started', confirm_sound.tStartRefresh)
    loop_back.addData('confirm_sound.stopped', confirm_sound.tStopRefresh)
    loop_back.addData('confirm_sound.numClicks', confirm_sound.numClicks)
    if confirm_sound.numClicks:
       loop_back.addData('confirm_sound.timesOn', confirm_sound.timesOn)
       loop_back.addData('confirm_sound.timesOff', confirm_sound.timesOff)
    else:
       loop_back.addData('confirm_sound.timesOn', "")
       loop_back.addData('confirm_sound.timesOff', "")
    # the Routine "TestSound" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    check_play = data.TrialHandler(nReps=play_sound , method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='check_play')
    thisExp.addLoop(check_play)  # add the loop to the experiment
    thisCheck_play = check_play.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCheck_play.rgb)
    if thisCheck_play != None:
        for paramName in thisCheck_play:
            exec('{} = thisCheck_play[paramName]'.format(paramName))
    
    for thisCheck_play in check_play:
        currentLoop = check_play
        # abbreviate parameter names if possible (e.g. rgb = thisCheck_play.rgb)
        if thisCheck_play != None:
            for paramName in thisCheck_play:
                exec('{} = thisCheck_play[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "play_sound"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        play_test_sound.setSound(freq, secs=0.5, hamming=False)
        play_test_sound.setVolume(vol, log=False)
        # keep track of which components have finished
        play_soundComponents = [play_test_sound]
        for thisComponent in play_soundComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        play_soundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "play_sound"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = play_soundClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=play_soundClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop play_test_sound
            if play_test_sound.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                play_test_sound.frameNStart = frameN  # exact frame index
                play_test_sound.tStart = t  # local t and not account for scr refresh
                play_test_sound.tStartRefresh = tThisFlipGlobal  # on global time
                play_test_sound.play()  # start the sound (it finishes automatically)
            if play_test_sound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > play_test_sound.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    play_test_sound.tStop = t  # not accounting for scr refresh
                    play_test_sound.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(play_test_sound, 'tStopRefresh')  # time at next scr refresh
                    play_test_sound.stop()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in play_soundComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "play_sound"-------
        for thisComponent in play_soundComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        play_test_sound.stop()  # ensure sound has stopped at end of routine
    # completed play_sound  repeats of 'check_play'
    
# completed 50.0 repeats of 'loop_back'


# ------Prepare to start Routine "Display"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
result_display.setText('You picked:\nVolume = ' + str(corrected_vol) + ' % (' + str(round(vol,4)) + ')\nFrequency = ' + str(freq) + ' Hz')
# keep track of which components have finished
DisplayComponents = [result_display]
for thisComponent in DisplayComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
DisplayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Display"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = DisplayClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=DisplayClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *result_display* updates
    if result_display.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        result_display.frameNStart = frameN  # exact frame index
        result_display.tStart = t  # local t and not account for scr refresh
        result_display.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(result_display, 'tStartRefresh')  # time at next scr refresh
        result_display.setAutoDraw(True)
    if result_display.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > result_display.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            result_display.tStop = t  # not accounting for scr refresh
            result_display.frameNStop = frameN  # exact frame index
            win.timeOnFlip(result_display, 'tStopRefresh')  # time at next scr refresh
            result_display.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DisplayComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Display"-------
for thisComponent in DisplayComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('result_display.started', result_display.tStartRefresh)
thisExp.addData('result_display.stopped', result_display.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
