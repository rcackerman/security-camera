''' 
TODO: 
* Make sure NTP is running so we have an accurate time
* Automatically deal with time zone! (DST etc)
'''

S3_KEY = process.env.S3_KEY
S3_SECRET = process.env.S3_SECRET

MIN_DIFFERENT_FRAMES = 4 # minimum number of different frames to trigger alert

active = True # Is the security camera on? 
streak = 0 # Is there motion? 

# List of photo files
# maybe this should be a FIFO queue of length TRIGGER_LENGTH?  
pastPhotos = []

# save the S3 urls
recording = []


'''
Toggle the system on or off
Maybe with Twilio? 
'''
onOff(state): 
  active = state
  if active: 
    runApp()


'''
Save an image file to S3.
'''
saveToS3(file):
  # save the file to S3 with a timestamp
  # Do we need to get the metadata from the image? 
  # Maybe put it in a folder so we don't hit S3's file count limits? 
  
  # then save the URL for sending out later 
  recording.push(s3url)
  
  
'''
Send us a message after the recording is over. 
'''
sendAlert():
 msg = 'Motion detected!\n'
  for photo in recording:
    msg += recording + '\n'
    
  send msg # twilio? email? both? 


'''
Monitor the camera
'''
# How many FPS does this give us? 
# Should we instead run this once per second and just do nothing if we are inactive? 
# https://docs.python.org/2/library/threading.html#timer-objects
runApp():
while Active: 
  # take a photo
  pastPhotos.push(photo)
  # if there is a previous photo
    # compare it to the last photo
    # is there significant change? 
      # if yes
        streak++
        # if streak is >= than MIN_DIFFERENT_FRAMES
          Save everything to S3
          Do we need to have a filename w/timestamp by now? 
          
          # Once everything is saved: 
          pastPhotos.empty()??? # This won't work..... need to save at least one photo for comparison.
        # else 
          # queue up the different photo in case we want it
          # pastPhotos.push(photo)
      # if no significant change
        # if we had a streak, and it's over, we need to send off an alert
        sendAlert()
        
        
        streak = 0 # reset the streak

