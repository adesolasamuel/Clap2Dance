## Full guide on building Clap2Dance device

## 1. Hardware setup

The hardware used are:
1. Raspberry Pi
2. Microphone Module
3. Bluetooth Speaker

Before the raspberry pi can be worked on, we have to setup by installing and configuring the OS. For this setup, i am using Debian Raspbian Operating system. Load the image on the Raspberry pi the hardware will be ready to be configured. The desktop interface is shown below.


![Screenshot 2022-05-01 015552](https://user-images.githubusercontent.com/55460620/166144933-0a5ea41c-a59e-4a0f-874e-ccbc6bff0ec8.png)

Using bluetooth, the lousspeaker is connected to the Raspberry pi and the microphone is connected via the GPIO and the USB terminal.

## 2. Training the model

Using Google cloud machine learning's Teachable Machine, the background noise and the clap samples are collected and the model is trained with these data.  

![Screenshot 2022-04-30 185610](https://user-images.githubusercontent.com/55460620/166145087-c3a20ae1-0b22-4ab1-82ad-f0ff80c49085.png)

![Screenshot 2022-04-30 185627](https://user-images.githubusercontent.com/55460620/166145088-4dfdb811-637b-45e0-8109-88ef0873f2b5.png)

![Screenshot 2022-04-30 185752](https://user-images.githubusercontent.com/55460620/166145089-be45fad8-9219-4b6c-9e2c-9c554cac408e.png)

![Screenshot 2022-04-30 185919](https://user-images.githubusercontent.com/55460620/166145090-204ed794-cc74-4f35-bf22-5b6e7c7e0ff3.png)

After training the model, the model is exported as a Tensorflow Lite model with extension .tflite. The model is then used in the code to recognise clap samples

![Screenshot 2022-04-30 190248](https://user-images.githubusercontent.com/55460620/166145091-c09377aa-341c-4f1c-aed6-9f2c56ae061f.png)

![Screenshot 2022-04-30 152915](https://user-images.githubusercontent.com/55460620/166145092-c9a096ec-d67e-4fa6-a469-3f414e90b1a5.png)

![Screenshot 2022-04-30 185432](https://user-images.githubusercontent.com/55460620/166145093-6f071bf6-804e-4a98-8c9a-125ce1f7217c.png)

## 3. Setting up Twilio

To set up twilio, the module to control it is pip installed in the raspberry pi using ""pip install twilio". After twilio has been installed the functionality is tested using a sample code, twiliosms.py


![Screenshot 2022-04-30 152856](https://user-images.githubusercontent.com/55460620/166145746-6198886e-43e2-43e2-9a51-e3cdfead2365.png)

![Screenshot 2022-04-30 152757](https://user-images.githubusercontent.com/55460620/166145754-2ff92455-032d-4f45-9a59-a80bf1396d74.png)

## 4. Finished Work

![20220501_063746](https://user-images.githubusercontent.com/55460620/166146632-92e79a22-9e54-47f8-b68f-3a5ae8d2dd53.jpg)
![20220501_063751](https://user-images.githubusercontent.com/55460620/166146637-14f1216b-956d-4833-a7d1-a4797b4e7db3.jpg)
![20220501_011823](https://user-images.githubusercontent.com/55460620/166146639-69e89fb8-eabc-49cb-8cd3-1bedfc49329d.jpg)
![20220501_011841](https://user-images.githubusercontent.com/55460620/166146643-ebad357c-c1bb-4586-a348-447cd7a398fe.jpg)
