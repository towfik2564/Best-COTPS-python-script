<img src="files/cotps_logo.png" align="right" />

# BEST COTPS BOT :robot: [MAY'22] 
> Hello, I am a programmer and side by side a Trader. Call me "Toffy". I've built the best bot/script for COTPS using python.

My bot is the smartest and fastest one for using python. It consumes less ram of VPS.

## Estimated profit it generates

> team bonus collection = 5 seconds
trade cycle completion = 15 seconds
total operating time needed for one cycle = 20 seconds
waiting time for next trade cycle =  2 hr = 2*3600 seconds
----------------------------------------------------------
total time needed for one complete cycle =  3620 seconds
1 month contains = 30*24*60*60 seconds = 2592000 seconds
So: in 1 month it can operate = (2592000/3620) = 716 cycles
1 cycle of cotps trade brings .1% profit
So: 716cycle can bring = 716*.1% profit

## Algorithm
starts > logs in cotps > collects team bonuses > keeps checking balance at 5mins interval > if wallet balance greater than 5 and no transaction balance left to arrive, then it starts trading > it keeps trading until wallet is lower than 5 > when trade is over it closes browser and wait for 2hrs > keep checking balance at 5mins interval > loop goes on

## Current performance
- completes one trade cycle within just 15seconds 
- takes only 5seconds for collecting team bonus before every trade cycle

## Features
- notification sending to your mobile after each successful trade cycle
- notification sending to your mobile when script/vps crashes
- notification sending to your mobile when profit arrives 

## Future upgrades:
- data export facility for last trades 

Here is the [demo of my bot](https://www.loom.com/share/e57f284c7c6e416ba894a77ce93eb83f) 