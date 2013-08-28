# created by dhead666
import xbmc
import sys

action_livetv = sys.argv[1]
action_video = sys.argv[2]

if xbmc.getCondVisibility("Pvr.IsPlayingTv") or xbmc.getCondVisibility("Pvr.IsPlayingRadio"):
  action = action_livetv
else:
  action = action_video
  
xbmc.executebuiltin(action)

