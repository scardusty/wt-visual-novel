 
# edit this list to rename, add or delete time of days
define end_of_day = "night" # set this as the last time of day before new day begins
#default end_of_day = time_of_day[-1] # this can automatically pick up the last element of time_of_day as above, remove above line if you want to use this.

# TOP BARS OF TOP BUTTONS ETC



screen top_buttons(buttons_xoffset = -15, buttons_yoffset = 15):
    zorder 99999
    style_prefix "light"
    $tod_icon = "gui/button/" + clock.time + ".png"
    hbox:
        style_prefix "light"
        xanchor 1.0
        yanchor 0.0
        xpos 1.0
        ypos 0.0
        xoffset buttons_xoffset
        yoffset buttons_yoffset
        spacing -3
        if CurrentScreenName() != "stats_menu":
            #textbutton "character maker" action ShowMenu("chooseStats")

            #textbutton "inventory" action ShowMenu("inventory_screen")  #xoffset -30

            textbutton "[clock.weekday]" style "top_dark_button" xsize 115

            textbutton "Day [clock.day]":
                text_xalign 0.0 
                left_padding 50
                #why isnt this working
                foreground Image(tod_icon, ysize = 17, ypos = 13, xpos = 22, oversample=3.3) 
                action [Function(clock.advance), SetScreenVariable(tod_icon, "gui/button/" + clock.time + ".png")]
        if CurrentScreenName() == "stats_menu":
            $tod_icon = "gui/button/" + clock.time + "_light.png"
            textbutton "Day [clock.day]" style_prefix "glow":
                text_xalign 0.5

                left_padding 50
                foreground Image(tod_icon, ysize = 17, ypos = 13, xpos = 22, oversample=3.3) 
                #why isnt this working
            textbutton "[player.money]" style_prefix "glow":
                padding (50,7,30,14)
                text_font gui.text_font
                text_size 20
                yalign 0.0
                xsize None
                foreground Image("gui/button/piggy.png",oversample = 3.3, ysize = 17, ypos = 12, xpos = 22,) 
            

        #stats icon button
        if CurrentScreenName() != "stats_menu":            
            imagebutton: 
                auto "gui/button/stats_%s.png"
                action ShowMenu("stats_menu")


style glow_button is light_button:
    ysize 50
    yoffset -1
    textalign 0.5
    background Frame("gui/button/glow_background3.png", 24, 8, 28, 12)
    #padding (27, 10, 27, 10)
style glow_button_text is light_button_text:
    yoffset 1
    color "fffe"
    size 16

style top_dark_button is light_button:
    background Frame("gui/button/flat_background.png", 24, 8, 28, 12)
    

style top_dark_button_text:
    color "fff" 
    xalign 0.5
    xoffset 1

style light_button_text:
    size 18
    color gui.muted_color

style light_button:
    xsize None
    yalign 0.5
    textalign 1.0
    xalign 0.5
    ysize 50
    background Frame("gui/button/light_background.png", 24, 8, 28, 12)
    padding (28, 10, 33, 14)

#style statBars_text:
    #line_leading 0
    
# STATS MENU

screen stats_menu(name = "statsUI"):
    tag menu 
    use game_menu(_("Stats")):#, scroll="viewport"):    
        
        use top_buttons(buttons_xoffset = -180, buttons_yoffset = -122)
        hbox:   
            hbox:
                spacing 10
                xalign 0.5
                yalign 1.0
                xfill True
                yoffset 10
                
                frame:
                    
                    style_prefix "statsUI"
                    xalign 0.5
                    yalign 0.0
                    ypadding 30
                    right_padding 15

                    has vbox
                    spacing 10

                    text "Agent Info" font "fonts/PixelSplitter.ttf" color gui.accent_color
                    vbox:
                        xsize 200
                        spacing 0
                        text "{b}Name{/b}: [player.name]"
                        text "{b}Age{/b}: 18"
                        text "{b}Pronouns{/b}: he/him"
                        text "{b}Zodiac{/b}: lupus"
                        text "\n"

                        textbutton "Inventory" style "quick_button" foreground Image("gui/button/backpack.png", ysize = 20, ypos = 14, xpos = 22, oversample=3.3) xsize 220 text_align 0.5 left_padding 10 bottom_padding 2 xalign 0.5 action ShowMenu("inventory_screen")
                        textbutton "Relationships" style "quick_button" foreground Image("gui/button/smile.png", ysize = 20, ypos = 14, xpos = 22, oversample=3.3) xsize 220 text_align 0.5 left_padding 10 bottom_padding 1 xalign 0.5 text_size 16

                frame:
                    yoffset -26
                    background Frame("gui/textbox_light.png", Borders(8, 8, 12, 12, 8, 8, 12, 18))
                    left_padding 30
                    vbox:   
                        style_prefix "statsMenu"
                        yalign 0.0
                        spacing 10
                        yoffset -20
                        xoffset -10
                        textbutton "Parameters" xalign 0.5:
                            style "large_glow_button"
                            text_size 25
                            yoffset -12
                            action NullAction()
                        add RadarChart(maximum = 5, expressions = player.statsArray(True), color1 = gui.accent_color_dark, color2 = "#dddddd", size=210, show_lines = True) yoffset -10 xalign 0.5
                        use statBars(150,20,7,17, gui.hover_color)

                        #vbox:
                        #     xoffset -60
                        #    spacing 11
                        #    xsize 30
                        #    text "[attack]" 
                        #     text "[mobility]"
                        #     text "[skill]"
                        #    text "[defense]" yalign 0.5
                        #     text "[command]"
                        #          text "[trion]"
                    #points and triggerset
                vbox:
                    style_prefix "points"
                    ypos 0.0
                    yoffset -50
                    spacing 20
                    #points hbox
                    hbox:
                        xsize 485
                        spacing 40
                        box_align 0.5
                        yoffset 10
                        vbox:
                            style_prefix "points_current"
                            text "Current" size 27 
                            text "Points: [player.points]\n([maintrigger[0]])" xalign 0.5 text_align 0.5
                        vbox:
                            style_prefix "points_highest"
                            text "Highest" size 27 
                            text "Points: 4107\n(scorpion)" xalign 0.5 text_align 0.5
                    text "Position: Attacker" size 30 color gui.hover_color
                    use triggerset

                    textbutton ("Edit Triggerset") action ShowMenu("triggersetEdit") xalign 0.5 yoffset -72

style points_text:
    xalign 0.5
    font "Pixelsplitter.ttf"

style points_current_text:
    is points_text
    size 20

style points_highest_text is points_current_text:
    color "fff9"


screen statBars(bar_width = 150,bar_thickness = 30, bar_spacing = 10, font_size=15, color = gui.hover_color):
    style_prefix "statBars"
    grid 2 7:
        transpose True
        yspacing bar_spacing
        xspacing 7
        text "Attack" size font_size
        text "Mobility" size font_size
        text "Skill" size font_size
        text "Defense/Support" size (font_size -1)
        text "Command" size font_size
        text "Range" size font_size
        text "Trion" size font_size

    #vbox:
        #spacing 10
        bar value player.attack xsize bar_width ysize bar_thickness range 12 yalign 0.5 
        bar value player.mobility xsize bar_width ysize bar_thickness range 12 yalign 0.5
        bar value player.skill xsize bar_width ysize bar_thickness range 12 yalign 0.5
        bar value player.defense xsize bar_width ysize bar_thickness range 12 yalign 0.5
        bar value player.command xsize bar_width ysize bar_thickness range 12 yalign 0.5
        bar value player.ranger xsize bar_width ysize bar_thickness range 12 yalign 0.5
        bar value player.trion xsize bar_width ysize bar_thickness range 12 yalign 0.5

style statBars_text:
    xalign 1.0
    yalign 0.5
    color gui.hover_color
    line_leading 0
    font "PixelSplitter.ttf"

style statsUI_text is text:
    xalign 0.0
    line_leading 0

screen chooseStats():
    tag menu

    use game_menu(_("Choose Stats"), scroll="viewport"):

        
        hbox:
            box_align 0.5
            xpos 0.5
            xanchor 0.5
            xfill True
            spacing 20
            style_prefix "statBars"
            use sampleStats(starting1,"option 1")
            use sampleStats(starting2,"option 2")
            use sampleStats(starting3,"option 3")



screen sampleStats(stat_block=player.stats, block_name = option, bar_width = 120,bar_thickness = 20, bar_spacing = 3, font_size=13):
    vbox:
        box_reverse True
        xalign 0.5
        box_align 0.5
        xsize 270
        spacing 0
        frame:
            background Frame("gui/textbox_light.png", Borders(8, 8, 12, 12, 8, 8, 12, 18))
            padding (25, 45, 25, 30)
            has vbox
            spacing 10
            add RadarChart(maximum = 5, expressions = stat_block.statsArray(True), color1 = gui.accent_color_dark, color2 = "#dddddd", size=200, show_lines = True):
                xalign 0.5
            grid 2 7:
                transpose True
                yspacing bar_spacing
                xspacing 3
                text "Attack" size font_size
                text "Mobility" size font_size
                text "Skill" size font_size
                text "Defense/Support" size font_size
                text "Command" size font_size
                text "Range" size font_size
                text "Trion" size font_size

            #vbox:
                
                #spacing 10
                bar value stat_block.attack xsize bar_width ysize bar_thickness range 13 yalign 0.5:
                    left_bar Frame("gui/bar/heart_left_new.png", 0, 0, tile="integer")
                    right_bar Frame("gui/bar/heart_right_new.png", 0, 0, tile="integer")
                bar value stat_block.mobility xsize bar_width ysize bar_thickness range 13 yalign 0.5 
                bar value stat_block.skill xsize bar_width ysize bar_thickness range 13 yalign 0.5 
                bar value stat_block.defense xsize bar_width ysize bar_thickness range 13 yalign 0.5 
                bar value stat_block.command xsize bar_width ysize bar_thickness range 13 yalign 0.5 
                bar value stat_block.ranger xsize bar_width ysize bar_thickness range 13 yalign 0.5 
                bar value stat_block.trion xsize bar_width ysize bar_thickness range 13 yalign 0.5 
        
        textbutton block_name style "gear_button" xalign 0.5 yoffset 32 action NullAction()
