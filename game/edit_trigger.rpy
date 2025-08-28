#########################
#   GLOBAL VARIABLES    #
#########################

default used_triggers = []
default temp = []

############################
#   PYTHON FOR TRIGGERS    #
############################

init python:

    #trigger bonuses
    all_trigger_stats = {
    'scorpion':{'attack':1.5, 'mobility': 1.0},
    'kogetsu':{'attack':1.5},
    'senku':{'ranger':1.0},
    'genyo':{'ranger':0.5},
    'raygust':{'attack':1.25},
    'thruster':{'mobility':1.0},
    'asteroid':{'attack':1.0},
    'hound':{'attack':1.0},
    'meteor':{'attack':1.0},
    'viper':{'attack':1.0},
    'handgun (asteroid)':{'attack':1.0},
    'handgun (hound)':{'attack':1.0},
    'handgun (meteor)':{'attack':1.0},
    'handgun (viper)':{'attack':1.0},
    'assault rifle (asteroid)':{'attack':1.0},
    'assault rifle (hound)':{'attack':1.0},
    'assault rifle (meteor)':{'attack':1.0},
    'assault rifle (viper)':{'attack':1.0},
    'shotgun (asteroid)':{'attack':1.0},
    'shotgun (hound)':{'attack':1.0},
    'shotgun (meteor)':{'attack':1.0},
    'shotgun (viper)':{'attack':1.0},
    'grenade launcher (meteor)':{'defense':1.0},
    'lead bullet': {'defense':1.0},
    'egret':{'ranger':4.0},
    'lightning':{'ranger':3.0},
    'ibis':{'ranger':3.0},
    'shield':{'defense':1.5},
    'escudo':{'defense':2.5},
    'bagworm':{'defense':0.2},
    'grasshopper':{'mobility':2.0},
    'dummy beacon':{'defense':0.5},
    'spider':{'defense':1.0},
    'chameleon':{'command':1.0},
    'starmaker': {'defense':0.5},
    'free trigger': {'attack':0.0}
    } 

    all_triggers = []

    # TRIGGER CLASS SETUP
    class Trigger:
        def __init__(self, name, stats, position):
            self.name = name
            self.stats = stats
            self.position = position
            self.points = 3000

            self.importStats()
            all_triggers.append(self)

        #return as string
        def __repr__(self):
            return f'{self.position} trigger "{self.name}" has stats {self.stats}.'
            

        # Assigning stats
        def importStats(self):
            #    
            triggerStats = all_trigger_stats[self.name]
            #sets nonexistent stats to zero to avoid errors
            self.attack, self.mobility, self.defense, self.ranger = 0.0, 0.0, 0.0, 0.0

            #maps stats from the big stats object
            for stat in triggerStats:
                print(f"{self.name} has stats:")
                print(f"{stat}: {triggerStats[stat]}")
                statName = str(stat)
                if statName == "attack":
                    self.attack = triggerStats[stat]
                elif statName == "mobility":
                    self.mobility = triggerStats[stat]
                elif statName == "defense":
                    self.defense = triggerStats[stat]
                elif statName == "ranger":
                    self.ranger = triggerStats[stat] 

        #earning points for a certain trigger (aka ur points when the trigger is in the top main slot)
        #untested bc its a lot to set
        def addPoints(self, point_count = 0):

            if maintrigger[0] == self.name:
                self.points += point_count
                player.points = self.points
            return player.points


        #description
        @property
        def desc(self):
            return f"{self.position} trigger {self.name} has stats {self.stats}."


    #Trigger objects:
    scorpion = Trigger('scorpion', all_trigger_stats['scorpion'], 'attacker')
    kogetsu = Trigger('kogetsu', all_trigger_stats['kogetsu'], 'attacker')
    senku = Trigger('senku', all_trigger_stats['senku'], 'optional')
    genyo = Trigger('genyo', all_trigger_stats['genyo'], 'optional')
    raygust = Trigger('raygust', all_trigger_stats['raygust'], 'attacker')
    thruster = Trigger('thruster', all_trigger_stats['thruster'], 'optional')
    asteroid = Trigger('asteroid', all_trigger_stats['asteroid'], 'shooter')
    hound = Trigger('hound', all_trigger_stats['hound'], 'shooter')
    meteor = Trigger('meteor', all_trigger_stats['meteor'], 'shooter')
    viper = Trigger('viper', all_trigger_stats['viper'], 'shooter')
    handgun_asteroid = Trigger('handgun (asteroid)', all_trigger_stats['handgun (asteroid)'], 'gunner')
    handgun_hound = Trigger('handgun (hound)', all_trigger_stats['handgun (hound)'], 'gunner')
    handgun_meteor = Trigger('handgun (meteor)', all_trigger_stats['handgun (meteor)'], 'gunner')
    handgun_viper = Trigger('handgun (viper)', all_trigger_stats['handgun (viper)'], 'gunner')
    assault_rifle_asteroid = Trigger('assault rifle (asteroid)', all_trigger_stats['assault rifle (asteroid)'], 'gunner')
    assault_rifle_hound = Trigger('assault rifle (hound)', all_trigger_stats['assault rifle (hound)'], 'gunner')
    assault_rifle_meteor = Trigger('assault rifle (meteor)', all_trigger_stats['assault rifle (meteor)'], 'gunner')
    assault_rifle_viper = Trigger('assault rifle (viper)', all_trigger_stats['assault rifle (viper)'], 'gunner')
    shotgun_asteroid = Trigger('shotgun (asteroid)', all_trigger_stats['shotgun (asteroid)'], 'gunner')
    shotgun_hound = Trigger('shotgun (hound)', all_trigger_stats['shotgun (hound)'], 'gunner')
    shotgun_meteor = Trigger('shotgun (meteor)', all_trigger_stats['shotgun (meteor)'], 'gunner')
    shotgun_viper = Trigger('shotgun (viper)', all_trigger_stats['shotgun (viper)'], 'gunner')
    grenade_launcher = Trigger('grenade launcher (meteor)', all_trigger_stats['grenade launcher (meteor)'], 'gunner')
    lead_bullet = Trigger('lead bullet', all_trigger_stats['lead bullet'], 'optional')
    egret = Trigger('egret', all_trigger_stats['egret'], 'sniper')
    lightning = Trigger('lightning', all_trigger_stats['lightning'], 'sniper')
    ibis = Trigger('ibis', all_trigger_stats['ibis'], 'sniper')
    shield = Trigger('shield', all_trigger_stats['shield'], 'defense')
    escudo = Trigger('escudo', all_trigger_stats['escudo'], 'defense')
    bagworm = Trigger('bagworm', all_trigger_stats['bagworm'], 'optional')
    grasshopper = Trigger('grasshopper', all_trigger_stats['grasshopper'], 'optional')
    dummy_beacon = Trigger('dummy beacon', all_trigger_stats['dummy beacon'], 'optional')
    spider = Trigger('spider', all_trigger_stats['spider'], 'optional')
    chameleon = Trigger('chameleon', all_trigger_stats['chameleon'], 'optional')
    starmaker = Trigger('starmaker', all_trigger_stats['starmaker'], 'optional')
    free_trigger = Trigger('free trigger', all_trigger_stats['free trigger'], 'optional')

    #this doesnt work
    """def checkTriggerSet(trigger) :
        if trigger not in subtrigger and trigger not in maintrigger:
            return True
        else:
            return False"""


    #Calculating Stats!!!!!

    def calcStats():
        player.stats = player.base_stats.copy()
        print(player.stats, " are the") # this will just tell you the stats before any modifiers are added.
        # You should probably include something up here to reset the stats to defaults.

        counted_triggers = [] # this has to be reset to an empty list before you start going through all the triggers
        for i in maintrigger+subtrigger:
            trigger_data = all_trigger_stats[i]
            for stat in trigger_data:
                stat_change = trigger_data[stat]
                if i in counted_triggers:
                    stat_change /= 2
                if stat in player.stats:
                    player.stats[stat] += stat_change
                else:
                    print("Warning! Tried to modify a stat the player didn't previously have.")
                    player.stats[stat] = stat_change
            counted_triggers.append(i)
        player.setStats()

    def setTriggerSlot(trigger, side, slot):
        #if side == 'maintrigger':
            #otherside = subtrigger
        #elif side == 'subtrigger':
            #otherside = 'maintrigger'
        if trigger == 'free trigger' or trigger not in maintrigger+subtrigger:
            side[slot] = trigger
        elif trigger not in side:
            side[slot] = trigger
        elif side[slot] == trigger:
            side[slot] = 'free trigger'
        calcStats()
    
    def clearTrigger():
        maintrigger[0], maintrigger[1], maintrigger[2], maintrigger[3] = "free trigger", "free trigger", "free trigger", "free trigger"
        subtrigger[0], subtrigger[1], subtrigger[2], subtrigger[3] = "free trigger", "free trigger", "free trigger", "free trigger"
        calcStats()

python early:
    #Trigger Buttons in Edit Trigger Set
    class TriggerBtn(Action):
        def __init__(self,name,side,slot):
            self.name = name
            self.side = side
            self.slot = slot
            if self.side is maintrigger:
                self.otherside = subtrigger
                #self.otherside_str = "subtrigger"
                #self.side_str = "maintrigger"
            else:
                self.side_str = "subtrigger"
                #self.otherside_str = "maintrigger"
                #self.otherside = maintrigger

        def __call__(self):
            print(f"{self.name} . {self.side} . {self.slot}")
            if self.name not in self.side:
                    print(f"{self.side}","[",f"{self.slot}","]")
                    side = self.side
                    slot = self.slot
                    side[slot] = self.name
                    print(f"{self.side[self.slot]}")
                    if self.side == maintrigger:
                        selectedBtn = "maintrigger[", self.slot, "]" 
                    
                    elif self.side == subtrigger:
                        selectedBtn = "subtrigger[", self.slot, "]" 
            
            elif self.name == self.side[self.slot] or self.name == "free trigger":
                if self.side[self.slot] == "kogetsu": #kick out genyo and senku
                    x = 0
                    while x < 4:
                        if self.side[x] == "genyo" or self.side[x] == "senku":
                            self.side[x] = "free trigger"
                        x += 1
                elif self.side[self.slot] == "raygust": #kick out thruster
                    y = 0
                    while y < 4:
                        if self.side[y] == "thruster":
                            self.side[y] = "free trigger"
                        y += 1
                self.side[self.slot] = "free trigger"

            elif self.name == "free trigger":
                self.side[self.slot] = "free trigger"

            renpy.restart_interaction() 
            calcStats()

            return None

        def get_sensitive(self):
            if self.side is maintrigger and self.slot == 0:
                if self.name in "shield, lead bullet, bagworm, escudo, grasshopper, starmaker, spider, chameleon, dummy beacon":
                    return False
            if self.name == "free trigger":
                return True
            elif self.name in self.side and self.side[self.slot] != self.name:
                return False
            elif self.name == "genyo" or self.name== "senku": #make senku and genyo conditional
                if "kogetsu" in self.side and self.side[self.slot] != "kogetsu":
                    return True
                else:
                    return False
            elif self.name == "thruster": #make thruster conditional
                if "raygust" in self.side and self.side[self.slot] != "raygust":
                    return True
                else:
                    return False
            else:
                return True

        def get_selected(self):
            if self.name == self.side[self.slot]:
                return True
            else:
                return False



####################
#   TRIGGER SET    #
####################



screen triggerset():
    
#default subtrigger =  {'a': 'free trigger', "b":"free trigger", "c":"free trigger", "d":"free trigger"}
    style_prefix "triggerset"
    frame:
        ypadding 0
        xpadding 0
        yoffset -10
        has vbox
        if CurrentScreenName() == "stats_menu":
            frame: 
                yalign 1.0
                background Frame("gui/textbox_light.png", Borders(8, 8, 12, 12, 8, 8, 12, 18))
                padding (25, 10,25, 50)
                style_prefix "flat"

                grid 2 5:
                    spacing -5
                    transpose True
                    text "Main Trigger" xalign 0.5 font gui.interface_text_font yalign 0.5
                    textbutton maintrigger[0]: 
                        action NullAction()
                        if maintrigger[0] == "free trigger":
                            text_color "fff7"
                    textbutton maintrigger[1] : 
                        action NullAction()
                        if maintrigger[1] == "free trigger":
                            text_color "fff7"
                    textbutton maintrigger[2] : 
                        action NullAction()
                        if maintrigger[2] == "free trigger":
                            text_color "fff7"
                    textbutton maintrigger[3] : 
                        action NullAction()
                        if maintrigger[3] == "free trigger":
                            text_color "fff7"
                    text "Sub Trigger" xalign 0.5 font gui.interface_text_font yalign 0.5
                    textbutton subtrigger[0] : 
                        action NullAction()
                        if subtrigger[0] == "free trigger":
                            text_color "fff7"
                    textbutton subtrigger[1] : 
                        action NullAction()
                        if subtrigger[1] == "free trigger":
                            text_color "fff7"
                    textbutton subtrigger[2] : 
                        action NullAction()
                        if subtrigger[2] == "free trigger":
                            text_color "fff7"
                    textbutton subtrigger[3] : 
                        action NullAction()
                        if subtrigger[3] == "free trigger":
                            text_color "fff7"
                    

        elif CurrentScreenName() == "triggersetEdit":
            $tooltip = GetTooltip()
            if tooltip:
                $renpy.show_screen("tooltip_screen",top_tooltip=False,_zorder=9000)
            grid 2 5:
                spacing -5
                transpose True
                yoffset -10
                text "Main Trigger" xalign 0.5 font gui.interface_text_font yalign 0.5 yoffset 10
                textbutton maintrigger[0]: 
                    action Show("triggerChoices", side = maintrigger, slot = 0), SetVariable("selectedbtn", "maintrigger[0]"), SelectedIf(selectedbtn == "maintrigger[0]")
                    if format(maintrigger[0]) == "free trigger":
                        style_prefix "freeTrigger" 
                    tooltip "Your main offensive trigger, tied to your {b}Points{/b}."
                textbutton format(maintrigger[1]): 
                    action Show("triggerChoices", side = maintrigger, slot = 1), SetVariable("selectedbtn", "bmainbtn"), SelectedIf(selectedbtn == "bmainbtn")
                    if format(maintrigger[1]) == "free trigger":
                            style_prefix "freeTrigger" 
                textbutton format(maintrigger[2]): 
                    action Show("triggerChoices", side = maintrigger, slot = 2), SetVariable("selectedbtn", "cmainbtn"), SelectedIf(selectedbtn == "cmainbtn")
                    if format(maintrigger[2]) == "free trigger":
                            style_prefix "freeTrigger" 
                textbutton format(maintrigger[3]):
                    action Show("triggerChoices", side = maintrigger, slot = 3) , SetVariable("selectedbtn", "dmainbtn"), SelectedIf(selectedbtn == "dmainbtn")
                    if format(maintrigger[3]) == "free trigger":
                        style_prefix "freeTrigger" 
                text "Sub Trigger" xalign 0.5 font gui.interface_text_font yalign 0.5  yoffset 10
                textbutton format(subtrigger[0]):
                    action ShowMenu("triggerChoices", side = subtrigger, slot = 0), SetVariable("selectedbtn", "asubbtn"), SelectedIf(selectedbtn == "asubbtn")
                    if format(subtrigger[0]) == "free trigger":
                        style_prefix "freeTrigger" 
                textbutton format(subtrigger[1]): 
                    action Show("triggerChoices", side = subtrigger, slot = 1), SetVariable("selectedbtn", "bsubbtn"), SelectedIf(selectedbtn == "bsubbtn")
                    if format(subtrigger[1]) == "free trigger":
                        style_prefix "freeTrigger" 
                textbutton format(subtrigger[2]): 
                    action Show("triggerChoices", side = subtrigger, slot = 2) , SetVariable("selectedbtn", "csubbtn"), SelectedIf(selectedbtn == "csubbtn")
                    if format(subtrigger[2]) == "free trigger":
                        style_prefix "freeTrigger" 
                textbutton format(subtrigger[3]):
                    action Show("triggerChoices", side = subtrigger, slot = 3) , SetVariable("selectedbtn", "dsubbtn"), SelectedIf(selectedbtn == "dsubbtn")
                    if format(subtrigger[3]) == "free trigger":
                        style_prefix "freeTrigger" 

style triggerset_text is text:
    text_align 0.5
    xalign 0.5
style triggerset_button:
    is gear_button
    xsize 210
    ysize 60
    padding (20,10,20,12)
style triggerset_button_text:
    size 15
    kerning 1
    layout "greedy"

style freeTrigger_button:
    is triggerset_button
style freeTrigger_button_text:
    is triggerset_button_text
    selected_color "fff"
    idle_color "6da7a2"


style flat_button is button:
    xsize 220
    background Frame("gui/button/flat_background_light.png", 26, 8, 29, 12)
    padding (2,2,2,2)
    
style flat_button_text:
    color "fff"
    size 16

####################
#   EDIT SCREEN    #
####################

screen triggersetEdit():
    label "triggersetEdit"
    tag menu

    use game_menu(_("Edit Trigger")): 
        style_prefix "triggerEdit"
        text "click on a slot to change it.\nnote: the top slot of your main determines your combat position." line_spacing 0 line_leading 0 xalign 1.0 xoffset -30 yoffset -70 xsize 600

        #vbox: 
        #   xsize 250
        #    xalign 0.0
            
        vbox: #left side of screen
            xsize 415
            xalign 0.0
            spacing 0
            box_align 0.5
            
            vbox: # Main and Points label
                xoffset 10
                yoffset -5
                text "Main: {color=fff}[maintrigger[0]]{/color}" size 22 color gui.hover_color
                text "Points: {color=fff}4000{/color}" size 22 color gui.hover_color

            use triggerset#Triggerset boxes
            
            hbox: # Swap and Clear Buttons
                style_prefix "triggerset"
                xalign 0.5
                yoffset -20
                textbutton "swap":
                    action Function(swapTriggerSides)
                    ysize 50
                    xsize 100
                    text_size 14
                textbutton "clear":
                    ysize 50
                    xsize 100
                    text_size 14
                    action Confirm("Clear triggerset?",Function(clearTrigger),None)
            hbox:  #Radar chart and stat bars
                yoffset -20
                xoffset -20
                spacing 5
                hbox:
                    yalign 0.5
                    use statBars(125,13,3,13)
                add RadarChart(maximum = 5, expressions = player.statsArray(True), color1 = gui.accent_color_dark, color2 = "#dddddd", size=150, show_lines = True)

style triggerEdit_text:
    size 15
    kerning 1 
    color gui.selected_background_color 
    font gui.interface_text_font
    text_align 0.0

#trigger choice buttons (each button is a screen)

screen setTriggerBtn(trigger_name, side = maintrigger, slot = 0, icon_oversample = 3.3, icon_xpos = 22, icon_yalign = 0.5, img_name = 0, desc = ""):
    if img_name == 0:
        $link = "gui/trigger_icons/" + trigger_name + ".png"
    else: 
        $link = "gui/trigger_icons/" + img_name + ".png"
    $trigger_name_stripped = trigger_name.replace('\n', ' ')
    textbutton trigger_name: 
        action TriggerBtn(trigger_name_stripped, side, slot)
        foreground Image(link, yalign = icon_yalign, xpos = icon_xpos, oversample=icon_oversample)  
        tooltip desc


transform FadeInTransform:
        alpha 0.0
        pause(0.5)
        alpha 1.0

transform FadeInLinear:
        on show:
            alpha 0.0
            linear 0.5 alpha 1.0
        on hide:
            alpha 1.0
            linear 0.5 alpha 0.0

screen tooltip_screen(top_tooltip = True):
    
    $tooltip = GetTooltip()
    zorder 999
    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top top_tooltip
            frame: 
                at FadeInTransform
                xmaximum 340
                padding (10,5,10,5)
                yoffset 0
                if top_tooltip == True:
                    xalign 1.0
                elif top_tooltip == False:
                    xalign 0.0
                background "#03857fdd"
                text "[tooltip]" size 15 line_spacing 0

############################
#   TRIGGER CHOICES BOX    #
############################
     
screen triggerChoices(side = maintrigger, slot = 0, viewport="scroll"):
    #tag menu
    zorder 1
    #style_prefix "triggers"
    if side == maintrigger:
        $ otherside = subtrigger
    else:
        $ otherside = maintrigger

    #enables hover tooltips
    $ tooltip = GetTooltip()
    if tooltip:
        $renpy.show_screen("tooltip_screen",_zorder=9000)

    
    frame:
        #$ trigger_slot = eval(trigger_slot)
        frame:
            style_prefix "triggers"
            xpos 525
            ypos 150
            ymaximum 500
            xsize 700
            #xmaximum 700
            background Frame("gui/textbox.png", Borders(8, 8, 12, 12, 8, 8, 12, 18))
            padding (15, 7, 15, 20)
            #
            viewport:
                ysize 520
                scrollbars "vertical"
                mousewheel True
                has vbox
                xfill True
                xalign 0.5
                spacing 10

# DEFENSE TRIGGERS
                text "\nDefense" xoffset 20
                hbox:
                    spacing 2
                    xalign 0.5
                    box_align 0.5
                    box_wrap True
                    #box_wrap True

                    use setTriggerBtn("shield", side, slot, icon_xpos = 20, icon_oversample = 3, desc="highly recommended on both sides, unless you have {b}raygust{/b} or {b}escudo{/b} equipped.")
                    use setTriggerBtn("escudo", side, slot, icon_oversample = 3)

# ATTACKER TRIGGERS
                text "Attacker" xoffset 20
                hbox:
                    spacing 2
                    xalign 0.5
                    box_align 0.5
                    box_wrap True
                    
                    use setTriggerBtn("scorpion", side, slot, desc="Blade trigger that can change shape and extend/be removed from any part of the body. Powerful, lightweight, but less durable.")
                    use setTriggerBtn("kogetsu", side, slot, desc="A more traditional sword trigger, durable and powerful. Has optional triggers {b}senku{/b} and {b}genyo{/b}, which should be equipped on the same side.")
                    use setTriggerBtn("raygust", side, slot, icon_oversample = 2)
                    use setTriggerBtn("senku", side, slot, icon_oversample = 3, icon_xpos = 20, img_name = "optional", desc="optional trigger for {b}kogetsu{/b}. Extends slashes, improving your range.")
                    use setTriggerBtn("genyo", side, slot, icon_oversample = 3, icon_xpos = 20, img_name = "optional")
                    use setTriggerBtn("thruster", side, slot, icon_oversample = 3, icon_xpos = 20, img_name = "optional")

# SHOOTER TRIGGERS
                text "Shooter" xoffset 20
                hbox:
                    spacing 2
                    xalign 0.5
                    box_align 0.5
                    box_wrap True

                    use setTriggerBtn("asteroid", side, slot)
                    use setTriggerBtn("hound", side, slot)
                    use setTriggerBtn("meteor", side, slot, icon_oversample = 3.5)
                    use setTriggerBtn("viper", side, slot)

                    use setTriggerBtn("lead bullet", side, slot, icon_oversample = 3, icon_xpos = 20, img_name = "optional")
                    use setTriggerBtn("starmaker", side, slot, icon_oversample = 3, icon_xpos = 20, img_name = "optional")

                    
# GUNNER TRIGGERS
                text "Gunner" xoffset 20 
                hbox:
                    spacing 2
                    xalign 0.5
                    box_align 0.5
                    box_wrap True
                    style_prefix "gunner_triggers"

                    use setTriggerBtn("handgun\n(asteroid)", side, slot, icon_xpos = 17, icon_oversample = 3, img_name="handgun")
                    use setTriggerBtn("handgun\n(hound)", side, slot, icon_xpos = 17, icon_oversample = 3, img_name="handgun")
                    use setTriggerBtn("handgun\n(meteor)", side, slot, icon_xpos = 17, icon_oversample = 3, img_name="handgun")
                    use setTriggerBtn("handgun\n(viper)", side, slot, icon_xpos = 17, icon_oversample = 3, img_name="handgun")

                    use setTriggerBtn("shotgun\n(asteroid)", side, slot, icon_xpos = 18, icon_oversample = 3, img_name="shotgun")
                    use setTriggerBtn("shotgun\n(hound)", side, slot, icon_xpos = 18, icon_oversample = 3, img_name="shotgun")
                    use setTriggerBtn("shotgun\n(meteor)", side, slot, icon_xpos = 18, icon_oversample = 3, img_name="shotgun")
                    use setTriggerBtn("shotgun\n(viper)", side, slot, icon_xpos = 18, icon_oversample = 3, img_name="shotgun")
                    
                    use setTriggerBtn("assault rifle\n(asteroid)", side, slot, icon_xpos = 20, icon_oversample = 3, img_name="assault_rifle")
                    use setTriggerBtn("assault rifle\n(hound)", side, slot, icon_xpos = 20, icon_oversample = 3, img_name="assault_rifle")
                    use setTriggerBtn("assault rifle\n(meteor)", side, slot, icon_xpos = 20, icon_oversample = 3, img_name="assault_rifle")
                    use setTriggerBtn("assault rifle\n(viper)", side, slot, icon_xpos = 20, icon_oversample = 3, img_name="assault_rifle")

                    use setTriggerBtn("grenade launcher\n(meteor)", side, slot, icon_xpos = 20, icon_oversample = 2.5, img_name="grenade_launcher")

                        #xsize 245
                        #left_padding 15
                        #right_padding 5
# SNIPER TRIGGERS
                text "Sniper" xoffset 20
                hbox:
                    spacing 2
                    xalign 0.5
                    box_align 0.5
                    box_wrap True

                    use setTriggerBtn("egret", side, slot, icon_xpos = 20, icon_oversample = 3)
                    use setTriggerBtn("lightning", side, slot, icon_xpos = 20, icon_oversample = 3.2)
                    use setTriggerBtn("ibis", side, slot, icon_xpos = 20, icon_oversample = 3)

                text "Optional" xoffset 20
                hbox:
                    spacing 2
                    xalign 0.5
                    box_align 0.5
                    box_wrap True

                    use setTriggerBtn("bagworm", side, slot, icon_xpos = 20, icon_oversample = 3, img_name = "optional")
                    use setTriggerBtn("grasshopper", side, slot, icon_xpos = 20, icon_oversample = 3, img_name = "optional")
                    use setTriggerBtn("chameleon", side, slot, icon_xpos = 20, icon_oversample = 3, img_name = "optional")
                    use setTriggerBtn("spider", side, slot, icon_xpos = 20, icon_oversample = 3, img_name = "optional")
                    use setTriggerBtn("dummy beacon", side, slot, icon_xpos = 20, icon_oversample = 3, img_name = "optional")
                        
        hbox:
            spacing 10
            xpos 560
            xsize 700 
            ypos 130
            box_align 0.0
            textbutton "Free Trigger" style_prefix "free_trigger" text_size 13 xalign 0.5 action TriggerBtn("free trigger", side, slot)
            textbutton "Triggers" style_prefix "triggers_title" text_size 30 text_color "#eee" yoffset -6 style "large_glow_button"
            text ""
        
        #textbutton "Free Trigger" action SetDict(side,slot,"Free Trigger") 
    #Return()

style triggers_button: 
    is gear_button
    padding (45, 15, 30, 15)
    #foreground Image("gui/trigger_icons/%s.png",oversample=3, yalign = 0.5, xpos = 20) 
    #ymaximum 66 
    #xmaximum 200
    #xalign 0.5
    #yalign 0.5

style triggers_title:
    is gui_button

style free_trigger_button:
    is gear_button

style free_trigger_button_text:
    size 15
    kerning 1

style triggers_button_text:
    size 15
    kerning 1
    #xalign 0.5
    #yalign 0.5
style triggers_text:
    xalign 0.0
    line_leading 10
    color gui.hover_color
style gunner_triggers_button:
    ysize 66
    right_padding 27
    left_padding 40
    #yalign 0.5


#style triggers_text:
#   line_spacing 14



