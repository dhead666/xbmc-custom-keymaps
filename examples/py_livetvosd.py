# created by dhead666
# example how to autorun an updated script from userdata when system is ro (so you can't update the original script)
import xbmc
import sys

action_livetv = sys.argv[1]
action_video = sys.argv[2]
isFirst = sys.argv[3]
py_path = xbmc.translatePath("special://userdata/py_livetvosd.py")


if int(isFirst) and os.path.isfile(py_path):
  xbmc.executebuiltin("RunScript(special://userdata/py_livetvosd.py,\""+action_livetv+"\",\""+action_video+"\",0)")
  sys.exit(0)

else:
  if xbmc.getCondVisibility("VideoPlayer.Content(LiveTV)"):
    action = action_livetv
  else:
    action = action_video
  
  xbmc.executebuiltin(action)

