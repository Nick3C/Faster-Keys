# -*- coding: utf-8 -*-
#
# Faster-Keys (a plugin for Anki)
# Coded by Nick Cook <nick@n-line.co.uk>
# Version 0.1b (2009-07-04)
#
# Based on the Change Review Shortcut Keys Plugin by Damien Elmes <anki@ichi2.net>
#
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
#
#
"""
This is a simple plugin that makes some changes to Anki's keyboard shortcuts to improve workflow.


== Detailed Changes ===

1) Accept Recommendations:
      Anki's normally recommends which button you should push if you know the word.
      This is the default choice if you press space to answer the word.
      
      This is normally "good" (i.e. 3).
      In some circumstances, such as after a failed answer, Anki will recommend you only rate it hard and not "good" or "easy".
      
      However, if you use the number keys to rate your cards then these recommendations are ignored.
      This plugin will add partial respect for the recommendation to give added conservatism so Anki remembers the failure for you.
      
      It lets you rate using just the number keys without using space bar and still get the benefit of recommendations.
            
      If Anki recommends a "good" (3) or "easy" (4) then nothing is changed.
      If Anki recommends pressing "hard" (2) then if you press 3 or 4 the grade will be lowered by one level to 2 or 3 respectively.
      You can always access the old "good" (3) by pressing 6 or "easy" (4) by pressing the 7 key.

      If Anki recommends an "easy" (4) answer then 3 will produce this answer (but "hard" (2) will be unchanged).

      The old "3" key is defined as 8 in case you want it for some reason.
      

2) Double Press & Fast Show Answer
      If Anki is displaying a question then keys 1 to 5 will now jump to the answer.
      Normally this does nothing and only space advances to the question.

      This means that you can double press in a question to jump to the answer and set it (if you are sure you know the answer, be careful)


3) Skim Cards (Forward-style Button)
      The number 5 is defined as bury. This is quite convenient in itself.
      It also lets you skim through the pack using just 2 keys (4 and 5).

      It thus works like a next button or "forward" button on a browser.
      
      This is particularly useful for skimming through a backlog to clear cards you know well (and thus get the count down).
      Likewise it can be used to skim through new cards, adding only easy cards.
      
      Another application is that you can skip over one type of card (for example sentences, which take some time).


4) Back-style Undo
      The key "`" has been mapped to undo.
      This can save a lot of time and lets you use your pinky finger to go back, like in a browser.
      
      A word of caution: be careful of accidentally undoing a major change (it takes a while).

You can also add your own shortcuts. Note that this plugin is incompatible with the Change Review Shortcut Keys Plugin (just put your change in this file instead)


"""
from ankiqt import mw

def newEventHandler(evt):
    if (evt):
        key = unicode(evt.text())
    else:
        return oldEventHandler(evt)
    

    ### Don't set any shortcuts if not showing question or answer
    if not (mw.state == "showQuestion") and not (mw.state == "showAnswer"): 
        return oldEventHandler(evt)

    
    
    if key =="5" or key=="b":                           # add shortcuts to bury the fact
        evt.accept()   
        return mw.onBuryFact()
    """
    # Consider adding shortcute to mark keys and to increase and decrease priority with + and - keys:
    Prompt("Priority is now %s", cardpriotiry

        if key =="6":
            evt.accept()    
            undo = _("Mark Fact (Faster-Keys)")
            mw.deck.setUndoStart(undo)
            mw.currentCard.fact.tags = canonifyTags(mw.currentCard.fact.tags +
                                                    "," + "Marked"  "FasterKeys")
            mw.currentCard.fact.setModified()
            mw.deck.updateFactTags([mw.currentCard.fact.id])
            mw.deck.deleteCard(mw.currentCard.id)
            mw.reset()
            mw.deck.setUndoEnd(undo)
            return
    """


    if (mw.mainWin.actionUndo.isEnabled()):              # add undo shortcuts
        if key=="z" or key=="`" or key=="q":           
            evt.accept()
            return mw.onUndo()

    if (key) and (key >= "1") and (key <= "7"):
        press = int(key)
        evt.accept()                       
        if mw.state == "showQuestion":             # if we are on the question jump to the answer
            return mw.mainWin.showAnswerButton.click()               
        defaultpress=mw.defaultEaseButton()

        if (press == 3):                            # Redefine 3 as whatever the default key is
            press = defaultpress
        if (press == 4) and (defaultpress==2):      # lower by one if reccomendation is "hard" and you chose "easy"
            press = 3
        if (press == 6):                             # reset the original 3 as 6
            press = 3
        if (press == 7):                            # reset the original 4 as 7
            press = 4

        if mw.state == "showAnswer":                  # push an answer button
            return mw.cardAnswered(press)        


    return oldEventHandler(evt)


oldEventHandler = mw.keyPressEvent
mw.keyPressEvent = newEventHandler

mw.registerPlugin("Faster-Keys", 7)
