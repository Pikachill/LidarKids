from qt_scrollable import *


def run_pyqt_GUI (self):
 #Step 1 Select Location (UDID) - defines udid
    if ui.Step1radioButton1.isChecked()== True:
        udid = 'BCT_3D_5G_0101001'
    elif ui.Step1radioButton2.isChecked()== True:
        udid = 'BCT_3D_5G_0101002'
    print (udid)

 #Step 2 Select Data Mode - defines mode
    if ui.Step2radioButtonMode1.isChecked()== True:
        mode = 1
    elif ui.Step2radioButtonMode2.isChecked()== True:
        mode = 2
    
 #Step 3 Enter Date and/or Time Range - defines d1,t1,d2,t2
    d1 = ui.Step3d1Enter.text() #format: YYYY-MM-DD
    t1 = ui.Step3t1Enter.text() #format: THH:MM:SS
    d2 = ui.Step3d2Enter.text()
    t2 = ui.Step3t2Enter.text()

 #Step 4 Input Threshold - defines threshold
    if ui.Step4thresholdEnter.text()=="":
        threshold = 300
    else:
        threshold = int(ui.Step4thresholdEnter.text())
    
 #Step 5 Select Aggregation Interval (Mode 2 Only) - defines a
    if ui.Step5radioButton1.isChecked()== True:
        a=1
    if ui.Step5radioButton2.isChecked()== True:
        a=2
    if ui.Step5radioButton3.isChecked()== True:
        a=3
    if ui.Step5radioButton4.isChecked()== True:
        a=4

 #Step 6 Select Output Items (Mode 2 Only) - defines f
  #vehicle directions
    #North
    if ui.Step6checknw.isChecked()== True:
        nw="nw"
    else: nw=""

    if ui.Step6checkne.isChecked()== True:
        ne="ne"
    else: ne=""

    if ui.Step6checkns.isChecked()== True:
        ns="ns"
    else: ns=""
    #South
    if ui.Step6checksw.isChecked()== True:
        sw="sw"
    else: sw=""

    if ui.Step6checkse.isChecked()== True:
        se="se"
    else: ne=""

    if ui.Step6checksn.isChecked()== True:
        sn="sn"
    else: sn=""
    #West
    if ui.Step6checkwn.isChecked()== True:
        wn="wn"
    else: wn=""

    if ui.Step6checkwe.isChecked()== True:
        we="we"
    else: we=""

    if ui.Step6checkws.isChecked()== True:
        ws="ws"
    else: ws=""
    #East
    if ui.Step6checken.isChecked()== True:
        en="en"
    else: en=""

    if ui.Step6checkew.isChecked()== True:
        ew="ew"
    else: ew=""

    if ui.Step6checkes.isChecked()== True:
        es="es"
    else: es=""

  #Pedestrian Directions
    if ui.Step6checkpednlr.isChecked()== True:
        nlr="nlr"
    else: nlr=""

    if ui.Step6checkpednrl.isChecked()== True:
        nrl="nrl"
    else: nrl=""
    
    if ui.Step6checkpedslr.isChecked()== True:
        slr="slr"
    else: slr=""

    if ui.Step6checkpedsrl.isChecked()== True:
        srl="srl"
    else: srl=""

    if ui.Step6checkpedwlr.isChecked()== True:
        wlr="wlr"
    else: wlr=""

    if ui.Step6checkpedwrl.isChecked()== True:
        wrl="wrl"
    else: wrl=""

    if ui.Step6checkpedelr.isChecked()== True:
        elr="elr"
    else: elr=""

    if ui.Step6checkpederl.isChecked()== True:
        erl="erl"
    else: erl=""
    
    selected_dir=[nw,ne,ns,sw,se,sn,wn,we,ws,en,ew,es,nlr,nrl,slr,srl,elr,erl]
    f=",".join(i for i in selected_dir if len(i) > 0) #a string that contains all the selected directions seperated by comma for API call

 #Step 7 Select Output Format
    if ui.Step7radioButtondisplay.isChecked()==True:
        print_only = True
    elif ui.Step7radioButtoncsv.isChecked()==True:
        print_only = False
    #csv file saving window should pop up here and get file name and location
 
 #return variables needs for API call
    return(udid,mode,d1,t1,d2,t2,threshold,a,f,print_only)
    



    



