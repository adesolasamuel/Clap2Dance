"""Main scripts to run audio classification, take recording and play the music"""

import argparse
import time

from audio_classifier import AudioClassifier
from audio_classifier import AudioClassifierOptions

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input to check for security button pin and set initial value to be pulled low (off)


def run(model: str, max_results: int, score_threshold: float,
        overlapping_factor: float, num_threads: int,
        enable_edgetpu: bool) -> None:
  """Continuously run inference on audio data acquired from the device.

  Args:
    model: Name of the TFLite audio classification model.
    max_results: Maximum number of classification results to display.
    score_threshold: The score threshold of classification results.
    overlapping_factor: Target overlapping between adjacent inferences.
    num_threads: Number of CPU threads to run the model.
    enable_edgetpu: Whether to run the model on EdgeTPU.
  """

  if (overlapping_factor <= 0) or (overlapping_factor >= 1.0):
    raise ValueError('Overlapping factor must be between 0 and 1.')

  if (score_threshold < 0) or (score_threshold > 1.0):
    raise ValueError('Score threshold must be between (inclusive) 0 and 1.')

  # Initialize the audio classification model.
  options = AudioClassifierOptions(
      num_threads=num_threads,
      max_results=max_results,
      score_threshold=score_threshold,
      enable_edgetpu=enable_edgetpu)
  classifier = AudioClassifier(model, options)

  # Initialize the audio recorder and a tensor to store the audio input.
  audio_record = classifier.create_audio_record()
  tensor_audio = classifier.create_input_tensor_audio()

  # We'll try to run inference every interval_between_inference seconds.
  # This is usually half of the model's input length to create an overlapping
  # between incoming audio segments to improve classification accuracy.
  input_length_in_second = float(len(
      tensor_audio.buffer)) / tensor_audio.format.sample_rate
  interval_between_inference = input_length_in_second * (1 - overlapping_factor)
  pause_time = interval_between_inference * 0.1
  last_inference_time = time.time()


  # Start audio recording in the background.
  audio_record.start_recording()

  # Loop until the user close the classification results plot.
  while True:
    # Wait until at least interval_between_inference seconds has passed since
    # the last inference.
    now = time.time()
    diff = now - last_inference_time
    if diff < interval_between_inference:
      time.sleep(pause_time)
      continue
    last_inference_time = now

    # Load the input audio and run classify.
    tensor_audio.load_from_audio_record(audio_record)
    categories = classifier.classify(tensor_audio)

    #OPERATION MODE 1: OPEN. The device will not send message if it is used
    
    # Check sound to play music
    if categories == clap:
        import os
        file = "/home/pi/Desktop/HacktheDanceFloor/melody.mp3"
        os.system("mpg123 " + file)
    
    #OPERATION MODE 2: CLOSE. The device will send message if it is used
        
    if GPIO.input(10) == GPIO.HIGH:
        from twilio.rest import Client 
        account_sid = 'ACf99079a874e85a959182fdd70f0667e9' 
        auth_token = '32ae4fb59a244fb9bd3b1b616a801a0b' 
        client = Client(account_sid, auth_token)
        message = client.messages.create(  
                              messaging_service_sid='MGc970af21c986e42db5ea65abce502160', 
                              body='Clap2Dance Notification: Kindly be informed that your device has been activated',
                              to='+2348033411051' 
                          ) 
 
        print(message.sid)
        
        
        
    


def main():
  parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--model',
      help='Name of the audio classification model.',
      required=False,
      default='soundclassifier_with_metadata.tflite')
  parser.add_argument(
      '--maxResults',
      help='Maximum number of results to show.',
      required=False,
      default=5)
  parser.add_argument(
      '--overlappingFactor',
      help='Target overlapping between adjacent inferences. Value must be in (0, 1)',
      required=False,
      default=0.5)
  parser.add_argument(
      '--scoreThreshold',
      help='The score threshold of classification results.',
      required=False,
      default=0.0)
  parser.add_argument(
      '--numThreads',
      help='Number of CPU threads to run the model.',
      required=False,
      default=4)
  parser.add_argument(
      '--enableEdgeTPU',
      help='Whether to run the model on EdgeTPU.',
      action='store_true',
      required=False,
      default=False)
  args = parser.parse_args()

  run(args.model, int(args.maxResults), float(args.scoreThreshold),
      float(args.overlappingFactor), int(args.numThreads),
      bool(args.enableEdgeTPU))


if __name__ == '__main__':
  main()

